import requests
from bs4 import BeautifulSoup
url = 'https://www.skysports.com/premier-league-table'
data =requests.get(url)
print('|----------Team----------|---Games---|---win---|---Draw---|---Lost---|---GS---|---GC---|----GD----|---Points---|')
soup = BeautifulSoup(data.text,'html.parser')

pl_table = soup.find("table",class_ = 'standing-table__table callfn')

for team in pl_table.find_all('tbody'):
    row = team.find_all('tr')
    for team_name in row:
        pl_team = team_name.find('td',class_ = 'standing-table__cell standing-table__cell--name').text.strip()
        print(' '),
        print (pl_team),
        print(' '*(28-len(pl_team))),
        Pl_total_matches_played = team_name.find_all('td',class_ = 'standing-table__cell')[2].text
        print (Pl_total_matches_played),
        pl_win = team_name.find_all('td',class_ = 'standing-table__cell')[3].text
        print(' '*(8-len(pl_win))),
        print(pl_win),
        pl_draw = team_name.find_all('td',class_ = 'standing-table__cell')[4].text
        print(' '*(8-len(pl_draw))),
        print(pl_draw),
        pl_lost = team_name.find_all('td',class_ = 'standing-table__cell')[5].text
        print(' '*(9-len(pl_lost))),
        print(pl_lost),
        pl_GS = team_name.find_all('td',class_ = 'standing-table__cell')[6].text
        print(' '*(8-len(pl_GS))),
        print(pl_GS),
        pl_GC = team_name.find_all('td',class_ = 'standing-table__cell')[7].text
        print(' '*(8-len(pl_GC))),
        print(pl_GC),
        pl_GD = team_name.find_all('td',class_ = 'standing-table__cell')[8].text
        print(' '*(8-len(pl_GD))),
        print(pl_GD),
        pl_point = team_name.find_all('td',class_ = 'standing-table__cell')[9].text
        print(' '*(8-len(pl_point))),
        print (pl_point)
        print('--'*56)
