import requests
from bs4 import BeautifulSoup
import os


def webscraping(URL):
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1', class_="ResultsArchiveTitle")
    title_printable = str(title)
    print(title_printable[66:105])
    print(title_printable[225:242])

    date = soup.find('span', class_="full-date")
    print(date.get_text())

    track = soup.find('span', class_="circuit-info")
    print(track.get_text())

    if os.path.exists("Mensaje.txt"):
            os.remove("Mensaje.txt")
    file = open("Mensaje.txt", "w")
    file.close()
    file = open("Mensaje.txt", "a")
    file.write(title_printable[66:105] + "\n" + title_printable[225:242] + "\n" + date.get_text() + "\n" + track.get_text() + "\n")

    results = soup.find('table', class_="resultsarchive-table")
    grid_position = results.find_all('tr')
    for line in grid_position:
        grid_position_info = line.find_all('td', class_="dark bold")
        grid_position_time = ''.join(str(e) for e in grid_position_info[1:2])
        grid_position_time_printable = grid_position_time[22:30]
        grid_position_number = line.find('td', class_="dark")
        for l in grid_position_info:
            grid_position_driver = l.find('span', class_="hide-for-mobile")
            if grid_position_driver == None:
                continue
            else:
                message = grid_position_number.get_text() + " " + grid_position_driver.text + " " + grid_position_time_printable
                print(message)
                file.write(message + "\n")
    file.close()
                