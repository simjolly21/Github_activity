import json
import urllib.request
import sys

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    
    try:
        # Fetch data from GitHub API
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read()
                events = json.loads(data)
                
                if events:
                    print(f"Recent activity for user: {username}\n")
                    for event in events[:10]:  # Display up to 10 events
                        event_type = event['type']
                        repo_name = event['repo']['name']
                        
                        if event_type == "PushEvent":
                            commits = len(event['payload']['commits'])
                            print(f"- Pushed {commits} commit(s) to {repo_name}")
                        elif event_type == "IssuesEvent":
                            action = event['payload']['action']
                            print(f"- {action.capitalize()} an issue in {repo_name}")
                        elif event_type == "WatchEvent":
                            print(f"- Starred {repo_name}")
                        else:
                            print(f"- {event_type} event occurred in {repo_name}")
                else:
                    print(f"No recent activity found for user: {username}")
            else:
                print(f"Failed to fetch data for user: {username} (Status code: {response.status})")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"Failed to reach the server: {e.reason}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
    else:
        username = sys.argv[1]
        fetch_github_activity(username)
