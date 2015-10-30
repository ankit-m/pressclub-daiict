import requests
from bs4 import BeautifulSoup
import time

session = requests.Session()

def login(username, password):
    getLoginScreen = session.get('https://webmail.daiict.ac.in')
    loginRequest = session.post('https://webmail.daiict.ac.in/zimbra/', data={'loginOp':'login','username': username,'password':password, 'client': 'preferred'})
    inbox = session.get('https://webmail.daiict.ac.in/zimbra/h/search?mesg=welcome&initial=true&app=')
    soup = BeautifulSoup(inbox.text, 'html.parser')
    return soup


#can be optimized further
def getAllTitles(soup):
    titles = []
    email = soup.find(id='R0')
    counter = 0

    while email != None:
        title = email.find_all(attrs= {'class': 'Fragment'})[0].text.encode('utf-8').lower()
        titles.append(title)
        counter = counter + 1
        key = 'R' + str(counter)
        email = soup.find(id=key)

    return titles
