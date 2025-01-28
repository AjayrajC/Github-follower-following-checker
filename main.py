
"""
Github Follower/Following Checker
-----------------------------------
A simple script to compare your followers vs. whom you follow,
showing who follows you back and who doesn't.
"""

from github import Github

def main():
    print("=== GitHub Follower/Following Checker (PyGithub) ===\n")

    # 1. Prompt for a Personal Access Token
    pat = input("Enter your GitHub Personal Access Token: ").strip()
    if not pat:
        print("A Personal Access Token is required. Exiting.")
        return

    # 2. Create a Github instance
    g = Github(pat)

    # 3. Retrieve the authenticated user
    try:
        me = g.get_user()
        my_username = me.login
        print(f"Authenticated as: {my_username}\n")
    except Exception as e:
        print(f"Error authenticating: {e}")
        return

    # 4. Fetch all followers and following (PyGithub handles pagination)
    followers = {u.login for u in me.get_followers()}
    following = {u.login for u in me.get_following()}

    # 5. Compare
    mutual = followers & following
    only_followers = followers - following
    only_following = following - followers

    # 6. Print results
    print(f"Total Followers: {len(followers)}")
    print(f"Total Following: {len(following)}")
    print(f"Mutual Followers: {len(mutual)}")

    print("\nPeople Who Follow You But You Do NOT Follow Back:")
    if only_followers:
        for user in sorted(only_followers):
            print(f"  - {user}")
    else:
        print("  None")

    print("\nPeople You Follow But They Do NOT Follow You Back:")
    if only_following:
        for user in sorted(only_following):
            print(f"  - {user}")
    else:
        print("  None")

    print("\nMutual Followers (You Follow Each Other):")
    if mutual:
        for user in sorted(mutual):
            print(f"  - {user}")
    else:
        print("  None")


if __name__ == "__main__":
    main()
