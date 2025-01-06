import requests
import json
import pandas as pd

def get_data():
    # URL of the JSON file
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the JSON content to a file
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(response.json(), file, indent=4)  # Save with formatting
        print("JSON file downloaded and saved as 'data.json'")
    else:
        print(f"Failed to download JSON file. HTTP Status Code: {response.status_code}")

def get_teams():
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    team = data['teams']
    df = pd.DataFrame(team)
    table = df[['name','played','points','short_name']]
    print(table)

def main():
    ...



if __name__ == "__main__":
    get_teams()


