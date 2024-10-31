# Github_activity
This is the problem link: https://roadmap.sh/projects/github-user-activity

## Explanation

1. Command-line Argument: The script expects a GitHub username to be passed as an argument when running the script.

        python github_activity.py <username>

2. Fetching Data: The `urllib.request.urlopen()` function sends a GET request to the GitHub API for the specified user's events.

3. Handling JSON Data: The API returns data in JSON format, which is decoded using `json.loads()`.

4. Displaying the Activity: The script checks the type of event (e.g., PushEvent, IssuesEvent, etc.) and formats the output accordingly.

5. Error Handling: The script handles errors such as:

    - Invalid username (handled via HTTPError),
    - Network issues (handled via URLError),
    - Other exceptions (caught in a general Exception block).

## Running the Script

To run the script, save it as github_activity.py, and then execute it from the terminal with a GitHub username:

    python github_activity.py kamranahmedse

## Example Output

    Recent activity for user: kamranahmedse

    - Pushed 3 commit(s) to kamranahmedse/developer-roadmap
    - Opened an issue in kamranahmedse/developer-roadmap
    - Starred kamranahmedse/developer-roadmap


