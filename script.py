from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

# Replace with your GitHub access token
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Create a GitHub instance using the access token
g = Github(ACCESS_TOKEN)

# Replace with your repository name and owner
repository_owner = "AliiAHmadi"
repository_name = "Zero-Framework"
labels = ["test-label"]
state = "open"


# Get the repository object
repo = g.get_repo(f"{repository_owner}/{repository_name}")
print(repo)

# Get all the issues in the repository with the "auto-release" label
issues = repo.get_issues(labels=labels, state=state)

# Loop through each issue and get its comments
for issue in issues:
    print(f"Issue: {issue.title}")
    for comment in issue.get_comments():
        print(f"\tComment: {comment.body}")
