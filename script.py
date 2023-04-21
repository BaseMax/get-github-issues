import os
from github import Github
from dotenv import load_dotenv
import sys

load_dotenv()


if len(sys.argv) > 1:
    repository_owner = sys.argv[1]
    repository_name = sys.argv[2]
    labels = sys.argv[3].split(",")
else:
    repository_owner = os.getenv("REPO_OWNER")
    repository_name = os.getenv("REPO_NAME")
    labels = os.getenv("LABELS").split(",")

# Replace with your GitHub access token
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Create a GitHub instance using the access token
g = Github(ACCESS_TOKEN)

# Replace with your repository name and owner



state = "open"

# Get the repository object
repo = g.get_repo(f"{repository_owner}/{repository_name}")
print(repo)

# Get all the issues in the repository with the "auto-release" label
issues = repo.get_issues(labels=labels, state=state, sort='updated')

# Loop through each issue and get its comments
for issue in issues:
    print(f"Issue: {issue.title}")
    print("body: <<<", issue.body, ">>>")
    
    comments = list(issue.get_comments()).reverse()
    for comment in comments:
        print(f"\tComment: {comment.body}")

    print("\n\n")
