import requests
import pandas as pd
from tabulate import tabulate
from colorama import Fore, Back, Style, init 
import json


def colorize_row(row):
    if row['Position'] <= 4:
        return [Fore.RED + str(x) + Style.RESET_ALL for x in list(row.values())]
    elif row['Position'] == 5:
        return [Fore.GREEN + str(x) + Style.RESET_ALL for x in list(row.values())]
    elif row['Position'] == 6:
        return [Fore.YELLOW + str(x) + Style.RESET_ALL for x in list(row.values())]
    else:
        return [Fore.WHITE + str(x) + Style.RESET_ALL for x in list(row.values())]

def get_data():    
    # API URL and Key (Replace 'YOUR_API_KEY' with your actual key)
    with open ('cred.json', 'r') as file:
        cred = json.load(file)
    api_url = cred['URL']
    headers = {'X-Auth-Token': cred['API-KEY']}
    # Fetch the data
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()    
        # Parse the data to extract relevant fields
        standings = data['standings'][0]['table']  # Access the standings table
        table_data = []
        for team in standings:
            table_data.append({
                "Position": team['position'],
                "Team": team['team']['name'],
                "Played": team['playedGames'],
                "Win": team['won'],
                "Draw": team['draw'],
                "Loss": team['lost'],
                "Points": team['points']
            })
    
        # Create DataFrame
        df = pd.DataFrame(table_data)
        colored_data = [colorize_row(row) for row in df.to_dict(orient="records")]
        headers = df.columns
        print(tabulate(colored_data, headers=headers, tablefmt="psql"))
    else:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")


       
    
if __name__ == "__main__":
    get_data()
    


