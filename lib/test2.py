import requests

# Example API endpoint (GitHub API)
url = "https://api.github.com/users/octocat"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse and print the JSON response
    user_data = response.json()
    print("User ID:", user_data["id"])
    print("Username:", user_data["name"])
else:
    print("Error:", response.status_code)
