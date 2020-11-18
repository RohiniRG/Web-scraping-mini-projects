from bs4 import BeautifulSoup
import requests

req = requests.get('https://en.wikipedia.org/wiki/Breaking_Bad')

# to check for valid URL
if req.status_code == 200:

    info_dict = {}  # to store data

    soup = BeautifulSoup(req.text, 'html.parser')  # for parsing through the html text

    info_table = soup.find('table', class_="infobox vevent")
    # change class_ according to the category of wikipedia from the page source

    for tr in info_table.find_all('tr'):

        try:
            if tr.find('th'):
                info_dict[tr.find('th').text] = tr.find('td').text

        except AttributeError:  # to prevent None type error
            pass

    for x, y in info_dict.items():
        print(x, " : ", y)

else:
    print('Invalid URL')
