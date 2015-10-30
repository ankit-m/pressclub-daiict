import webmail
import getpass
import pressclub

username = 'pressclub'
password = getpass.getpass('Pressclub Password: ')
soup = webmail.login(username, password)
titles = webmail.getAllTitles(soup);

roll = input('Please enter your ID: ')
pressclub.checkNewArticles(titles, roll)
