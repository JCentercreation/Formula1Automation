import time
import requests
from bs4 import BeautifulSoup

date = time.gmtime()
day = date[2]
month = date[1]
year = date[0]
hour = date[3]
minute = date[4]
second = date[5]
weekday = date[6]

weekdaytranslator = {
    0:"Monday",
    1:"Tuesday",
    2:"Wednesday",
    3:"Thusday",
    4:"Friday",
    5:"Saturday",
    6:"Sunday",
}

def DefineEvent():
    if day == 6 and month == 12:
        URL = 'https://www.formula1.com/en/results.html/2020/races/1060/bahrain/starting-grid.html'
    elif day == 13 and month == 12:
        URL = 'https://www.formula1.com/en/results.html/2020/races/1061/abu-dhabi/starting-grid.html'
    else:
        URL = 'https://www.formula1.com/en/results.html/2020/races/1059/bahrain/starting-grid.html'

    return URL


def CheckAvailability(URL): 
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    noresults = soup.find('p', class_="no-results")
    if noresults == None:
        print("Results Available")
        return True
    else:
        print("No Available Results")
        return False