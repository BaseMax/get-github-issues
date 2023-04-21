import os
import sys

from dotenv import load_dotenv
from github import Github

load_dotenv()

# Check arguments and OS ENV
if len(sys.argv) > 1:
    repository_owner = sys.argv[1]
    repository_name = sys.argv[2]
    labels = sys.argv[3].split(",")
else:
    repository_owner = os.getenv("REPO_OWNER")
    repository_name = os.getenv("REPO_NAME")
    labels = os.getenv("LABELS").split(",")

# Replace with your GitHub access token
access_token  = os.getenv("ACCESS_TOKEN")

# Create a GitHub instance using the access token
github_instance = Github(access_token)

# Get the repository object
repo = github_instance.get_repo(f"{repository_owner}/{repository_name}")

# Get all the issues in the repository with the "auto-release" label
state = "open"
issues = repo.get_issues(labels=labels, state=state, sort='updated')

# Log repository
print(repo)

# Loop through each issue and get its comments
for issue in issues:
    print(f"Issue: {issue.title}")
    print("body: <<<", issue.body, ">>>")
    
    comments = list(issue.get_comments()).reverse()
    for comment in comments:
        print(f"\tComment: {comment.body}")

    print("\n\n")
