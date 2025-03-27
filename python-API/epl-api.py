import requests
from prettytable import PrettyTable

# API base URL and key
API_BASE_URL = "https://api.football-data.org/v4"
API_KEY = "836608fc40774107af854e17e41fe6c9"

# Headers for the API request
HEADERS = {
    "X-Auth-Token": API_KEY
}

def get_epl_standings():
  
    # Fetch the current standings of the English Premier League (EPL).
  
    endpoint = f"{API_BASE_URL}/competitions/PL/standings"
    response = requests.get(endpoint, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        standings = data.get("standings", [])
        if standings:
            table = standings[0].get("table", [])
            for team in table:
                print(f"{team['position']}. {team['team']['name']} - {team['points']} points")
        else:
            print("No standings data available.")
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.reason}")

def get_epl_matches():
    # Fetch upcoming matches in the English Premier League (EPL).

    endpoint = f"{API_BASE_URL}/competitions/PL/matches"
    response = requests.get(endpoint, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        matches = data.get("matches", [])
        for match in matches:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            match_date = match['utcDate']
            print(f"{home_team} vs {away_team} on {match_date}")
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.reason}")

if __name__ == "__main__":
    print("EPL Standings:")
    get_epl_standings()
    print("\nUpcoming EPL Matches:")
    get_epl_matches()


def display_epl_table():
    # Fetch and display the EPL standings in a table format using PrettyTable.
    endpoint = f"{API_BASE_URL}/competitions/PL/standings"
    response = requests.get(endpoint, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        standings = data.get("standings", [])
        if standings:
            table = standings[0].get("table", [])
            pretty_table = PrettyTable()
            pretty_table.field_names = ["Position", "Team", "Points", "Played Games", "Goal Difference"]
            
            for team in table:
                pretty_table.add_row([
                    team['position'],
                    team['team']['name'],
                    team['points'],
                    team['playedGames'],
                    team['goalDifference']
                ])
            
            print(pretty_table)
        else:
            print("No standings data available.")
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.reason}")

if __name__ == "__main__":
    print("\nEPL Table:")
    display_epl_table()


def display_epl_player_stats():
    # Fetch and display EPL player stats in a table format using PrettyTable.
    endpoint = f"{API_BASE_URL}/competitions/PL/scorers"
    response = requests.get(endpoint, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        scorers = data.get("scorers", [])
        if scorers:
            pretty_table = PrettyTable()
            pretty_table.field_names = ["Rank", "Player", "Team", "Goals"]
            
            for rank, scorer in enumerate(scorers, start=1):
                pretty_table.add_row([
                    rank,
                    scorer['player']['name'],
                    scorer['team']['name'],
                    scorer['numberOfGoals']
                ])
            
            print(pretty_table)
        else:
            print("No player stats data available.")
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.reason}")