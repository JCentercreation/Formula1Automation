import requests
from bs4 import BeautifulSoup

URL = 'https://www.formula1.com/en/results.html/2020/races/1048/great-britain/starting-grid.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('table', class_="resultsarchive-table")

grid_position = results.find_all('tr')
for line in grid_position:
    grid_position_info = line.find_all('td', class_="dark bold")
    grid_position_time = ''.join(str(e) for e in grid_position_info[1:2])
    grid_position_time_printable = grid_position_time[22:30]
    for l in grid_position_info:
        grid_position_driver = l.find('span', class_="hide-for-mobile")
        if grid_position_driver == None:
            continue
        else:
            print(grid_position_driver.text + " " + grid_position_time_printable)