import requests
from bs4 import BeautifulSoup
import pandas as pd





url = 'https://www.skysports.com/premier-league-table'
data =requests.get(url)
#print('|----------------------Team------------------------|---Games---|---win---|---Draw---|---Lost---|---GS---|---GC---|----GD----|---Points---|')
soup = BeautifulSoup(data.text,'html.parser')

pl_table = soup.find("table",class_ = 'standing-table__table callfn')

teams = []
games = []
win = []
draw = []
loss = []
GS = []
GC = []
GD = []
points = []

for team in pl_table.find_all('tbody'):
    row = team.find_all('tr')
    for team_name in row:
        pl_team = team_name.find('td',class_ = 'standing-table__cell standing-table__cell--name').text.strip()
        teams.append(pl_team)
        pl_games_played = team_name.find_all('td',class_ = 'standing-table__cell')[2].text
        games.append(pl_games_played)
        pl_win = team_name.find_all('td',class_ = 'standing-table__cell')[3].text
        win.append(pl_win)
        pl_draw = team_name.find_all('td',class_ = 'standing-table__cell')[4].text
        draw.append(pl_draw)
        pl_lost = team_name.find_all('td',class_ = 'standing-table__cell')[5].text
        loss.append(pl_lost)
        pl_GS = team_name.find_all('td',class_ = 'standing-table__cell')[6].text
        GS.append(pl_GS)
        pl_GC = team_name.find_all('td',class_ = 'standing-table__cell')[7].text
        GC.append(pl_GC)
        pl_GD = team_name.find_all('td',class_ = 'standing-table__cell')[8].text
        GD.append(pl_GD)
        pl_point = team_name.find_all('td',class_ = 'standing-table__cell')[9].text
        points.append(pl_point)



table = {}
table['Team Name'] = teams
table["Games Played"] = games
table["Games won"] = win
table["Games draw"] = draw
table["Games loss"] = loss
table["Goals Scored"] = GS
table["Goals conceded"] = GC
table["Goal difference"]= GD
table["points"] = points

df = pd.DataFrame(table)
print(df)
