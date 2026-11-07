#!/usr/bin/env python3
"""Refresh the numbers in README.md from the GitHub API.

Each number in the README sits between markers:  <!--s:key-->value<!--/s-->
The markers are HTML comments, so they are invisible on the rendered page.
Any API failure aborts the run without touching the file.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

USER = "hieptl"
README = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
if not TOKEN:
    sys.exit("GITHUB_TOKEN is not set")

REPOS = {
    "openhands": "OpenHands/OpenHands",
    "canvas": "OpenHands/agent-canvas",
    "enterprise": "OpenHands/enterprise",
    "sdk": "OpenHands/software-agent-sdk",
    "automation": "OpenHands/automation",
    "extensions": "OpenHands/extensions",
    "cloud": "OpenHands/OpenHands-Cloud",
    "goldilocks": "FairwindsOps/goldilocks",
    "netflix": "hieptl/netflix-clone",
}


def api(path, method="GET", body=None):
    url = path if path.startswith("http") else "https://api.github.com" + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + TOKEN)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", USER + "-profile-stats")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def merged_prs(repo=None):
    q = f"is:pr is:merged author:{USER}"
    if repo:
        q += f" repo:{repo}"
    result = api("/search/issues?per_page=1&q=" + urllib.parse.quote(q))
    if result.get("incomplete_results"):
        raise RuntimeError(f"incomplete search results for {q!r}")
    time.sleep(2)  # stay well inside the search rate limit
    return int(result["total_count"])


def repo_info(repo):
    info = api(f"/repos/{repo}")
    return int(info["stargazers_count"]), int(info["forks_count"])


def contributions():
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          totalCommitContributions
          totalPullRequestReviewContributions
        }
      }
    }"""
    result = api("/graphql", "POST", {"query": query, "variables": {"login": USER}})
    if "errors" in result:
        raise RuntimeError(result["errors"])
    c = result["data"]["user"]["contributionsCollection"]
    return int(c["totalCommitContributions"]), int(c["totalPullRequestReviewContributions"])


def fmt_int(n):
    return f"{n:,}"


def fmt_stars(n):
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def fmt_stars_short(n):
    return f"{n // 1000}k+" if n >= 1000 else str(n)


def main():
    values = {"total_prs": fmt_int(merged_prs())}
    for key, repo in REPOS.items():
        if key != "netflix":
            values[f"{key}_prs"] = fmt_int(merged_prs(repo))
        stars, forks = repo_info(repo)
        values[f"{key}_stars"] = fmt_stars(stars)
        values[f"{key}_stars_short"] = fmt_stars_short(stars)
        values[f"{key}_forks"] = fmt_int(forks)
    commits, reviews = contributions()
    values["commits_year"] = fmt_int(commits)
    values["reviews_year"] = fmt_int(reviews)

    with open(README, encoding="utf-8") as f:
        text = f.read()

    seen = set()

    def replace(match):
        key = match.group(1)
        if key not in values:
            raise KeyError(f"README marker {key!r} has no fetched value")
        seen.add(key)
        return f"<!--s:{key}-->{values[key]}<!--/s-->"

    new_text = re.sub(r"<!--s:([a-z_]+)-->.*?<!--/s-->", replace, text)
    if not seen:
        sys.exit("no markers found in README.md")

    # The merged-PR badge carries the total inside its image URL.
    badge_value = urllib.parse.quote(values["total_prs"], safe="")
    new_text, n = re.subn(r"(Merged%20PRs-)[^-]+(-2EA44F)", rf"\g<1>{badge_value}\g<2>", new_text)
    if n != 1:
        sys.exit(f"expected one merged-PR badge, found {n}")

    if new_text == text:
        print("README.md already up to date")
        return
    with open(README, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("README.md updated:")
    for key in sorted(seen):
        print(f"  {key} = {values[key]}")


if __name__ == "__main__":
    main()
