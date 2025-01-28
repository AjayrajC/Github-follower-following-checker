# GitHub Follower/Following Checker

A simple Python 3 script that uses [PyGithub](https://github.com/PyGithub/PyGithub) to:
- Authenticate to GitHub with a Personal Access Token (PAT).
- Fetch all your followers and everyone you follow.
- Compare the lists and show:
  - Who follows you, but you do NOT follow back.
  - Who you follow, but they do NOT follow you back.
  - Who is in mutual follow (both ways).

## Features
- Simple command-line interaction.
- Automatically handles pagination (via PyGithub).
- Displays results in a concise summary.

## Requirements
- Python **3.x** (preferably 3.6+).
- [PyGithub](https://github.com/PyGithub/PyGithub) (`pip install PyGithub`).
- A GitHub **Personal Access Token** (PAT) with at least the `read:user` scope.

## Getting Started

### 1. Create (or Clone) This Repository
If you haven’t already, clone the repo to your local machine:
```bash
git clone git@github.com:AjayrajC/Github-follower-check.git
cd Github-follower-check
