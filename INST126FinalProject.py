import requests
import re

def get_github_repo_info(username, repo_name):
    # Getting repository info from GitHub API
    api_url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(api_url)

    # Checking if the HTTP status code is 200 and if so, it's successful
    if response.status_code == 200:

        # If successful, this extracting the JSON content and analyzing it
        repo_info = response.json()
        return repo_info
    
    # If the HTTP status code isnt 200, then they it prints out an error message with the status code
    else:
        print(f"Error: Unable to fetch repository information. Status Code: {response.status_code}")
        return None
    
def extract_year_month(timestamp):
    # Using the regular expression "re.search" to change the "Created at" and "Last pushed at" to a cleaner output of dates
    match = re.search(r'(\d{4}-\d{2})', timestamp)
    return match.group() if match else None

def main():
    # Getting the user to input a GitHub username and respository so they can see the details of anyone they want
    github_username = input("Enter GitHub username: ")
    github_repo = input("Enter GitHub repository: ")

    # Getting repo info from GitHub API
    repo_info = get_github_repo_info(github_username, github_repo)

    # Printing out all the details on a GitHub profile like the name of it or whether people have shown appreciation (stars)
    if repo_info:
        print(f"GitHub Repository Information for {github_username}/{github_repo}:")
        print(f"Name: {repo_info['name']}")
        print(f"Description: {repo_info['description']}")
        print(f"Stars: {repo_info['stargazers_count']}")
        print(f"Forks: {repo_info['forks_count']}")
        print(f"Watchers: {repo_info['subscribers_count']}")
        print(f"Language: {repo_info['language']}")
        print(f"Created at: {extract_year_month(repo_info['created_at'])}")
        print(f"Last pushed at: {extract_year_month(repo_info['pushed_at'])}")

# This is used to show that the script is run as the main program because it's being executed directly
if __name__ == "__main__":
    main()