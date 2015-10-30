import re
import string

sections = {'gdg': ['201301132', '201301156'],
            'warpsandwefts':['201301100', '201301089'],

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
