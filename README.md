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

## Steps

### 1. Create (or Clone) This Repository
If you haven’t already, clone the repo to your local machine:
```bash
git clone git@github.com:AjayrajC/Github-follower-check.git
cd Github-follower-check
```
### 2. Create a GitHub Personal Access Token
- Go to GitHub Settings.
- Click “Developer settings” → “Personal access tokens” (fine-grained or classic).
- Generate a new token with the read:user scope (minimum).
- Copy the token (PAT) immediately, GitHub won’t show it again.
### 3. Install Dependencies
- Use Python 3 to install the required packages.
- Run requirements.txt file:
```bash
python3 -m pip install -r requirements.txt
```
Otherwise, just install PyGithub directly:
```bash
python3 -m pip install PyGithub
```
### 4. Run the Script
- Run the script using Python 3:
```bash
python3 main.py
```
- When prompted, paste your Personal Access Token.
- You’ll see something like:
```
=== GitHub Follower/Following Checker (PyGithub) ===

Enter your GitHub Personal Access Token: 
Authenticated as: <YourUserName>

Total Followers: xx
Total Following: xx
Mutual Followers: xx

People Who Follow You But You Do NOT Follow Back:
  - SomeUser1
  - SomeUser2

People You Follow But They Do NOT Follow You Back:
  - SomeUser3

Mutual Followers (You Follow Each Other):
  - ...
```
    
### 5. Interpret the Results
- People Who Follow You But You Do NOT Follow Back: Users who appear in your followers list but not in your following list.
- People You Follow But They Do NOT Follow You Back: Users you follow who aren’t following you.
- Mutual Followers: Users in both lists.
### Contributing

Feel free to open an issue or submit a pull request if you have suggestions or improvements.


