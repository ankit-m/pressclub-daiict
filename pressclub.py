import re
import string

sections = {'books': ['201201100', '201301442', '201401014'],
            'campus':['201201002', '201401431', '201401425'],
            'film': ['201301126'],
            'food': ['201301130', '201401025'],
            'freeze': ['201301150'],
            'gna': ['201301112', '201301118'],
            'music': ['201301001'],
            'pcp': ['201201002', '201401403', '201301442'],
            'random':['201301027', '201401439', '201401055'],
            'sss': ['201201142', '201301029'],
            'sport': ['201301227'],
            'tachyon': ['201301099', '201301179', '201301043'],
            'vuelo': ['201301406', '201301101'],
            'warps': ['201201142', '201301042', '201401421']
            }

def checkNewArticles(titles, username):
    section = ''

    for i in sections:
        if username in sections[i]:
            section = i
            break

    for i in titles:
        title = re.sub('[\W_]+', '', i)
        if title.find(section) > 0:
            print 'You have an article: %s' % (i)
