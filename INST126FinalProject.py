import requests
from bs4 import BeautifulSoup
import re

def get_github_repo_info(nickelliott19, JOUR472_fall2023):
    # Getting repository info from GitHub API
    api_url = f"https://api.github.com/repos/{nickelliott19}/{JOUR472_fall2023}"
    response = requests.get(api_url)

    if response.status_code == 200:
        repo_info = response.json()
        return repo_info
    else:
        print(f"Error: Unable to fetch repository information. Status Code: {response.status_code}")
        return None

def extract_commit_activity(nickelliott19, JOUR472_fall2023):
    # Getting commit activity using BeautifulSoup
    commit_activity_url = f"https://github.com/{nickelliott19}/{JOUR472_fall2023}/graphs/commit-activity"
    response = requests.get(commit_activity_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Getting the commit activity info using regular expressions
        commit_activity_text = soup.find("a", class_="js-selected-navigation-item.selected").text
        commit_activity = re.findall(r'(\d+)\s+contributions\s+in the last year', commit_activity_text)
        return commit_activity[0] if commit_activity else None
    else:
        print(f"Error: Unable to fetch commit activity. Status Code: {response.status_code}")
        return None

def main():
    # Github Repo Info
    github_username = "nickelliott19"
    github_repo = "JOUR472_fall2023"

    # Getting repo info from GitHub API
    repo_info = get_github_repo_info(github_username, github_repo)

    if repo_info:
        print(f"GitHub Repository Information for {github_username}/{github_repo}:")
        print(f"Name: {repo_info['name']}")
        print(f"Description: {repo_info['description']}")
        print(f"Stars: {repo_info['stargazers_count']}")
        print(f"Forks: {repo_info['forks_count']}")
        print(f"Watchers: {repo_info['subscribers_count']}")
        print(f"Language: {repo_info['language']}")
        print(f"Created at: {repo_info['created_at']}")
        print(f"Last pushed at: {repo_info['pushed_at']}")

        # Getting and printing the commit activity
        commit_activity = extract_commit_activity(github_username, github_repo)
        if commit_activity:
            print(f"\nCommit Activity in the Last Year: {commit_activity} contributions")
        else:
            print("Commit activity information not available.")
    else:
        print("Exiting due to an error.")

if __name__ == "__main__":
    main()