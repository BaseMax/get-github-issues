import os
from github import Github
from dotenv import load_dotenv
import sys

load_dotenv()

def get_owner():
    owner = os.getenv("REPO_OWNER")
    if owner:
        return owner
    return sys.argv[1]



def get_repo_name():
    name = os.getenv("REPO_NAME")
    if name:
        return name
    return sys.argv[2]


def get_labels():
    labels = os.getenv("LABELS")
    if labels:
        return labels.split(",")
    print(sys.argv[3].split(","))


# Replace with your GitHub access token
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Create a GitHub instance using the access token
g = Github(ACCESS_TOKEN)

# Replace with your repository name and owner
repository_owner = get_owner()
repository_name = get_repo_name()
labels = get_labels()
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
