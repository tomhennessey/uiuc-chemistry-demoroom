## Script to generate demo database using text versions of 
## demo files

# to init the db, run the following commands in venv and run
# 'flask db init'
# 'flask db migrate -m "demos table" ' 
# 'flask db upgrade'
# and then run this script to populate the database

# alternatively, just run db_reset.sh

from sys import platform as _platform
from os import listdir, walk, name
from os.path import isfile, join
import itertools
from progress.bar import Bar
from app import db
from app.models import Demo

text_demos = 'app/static/demos_text/'
names = []
categories = []
texts = []
proper_names = []

# grab the no-spaced "ugly" name of a demo
def get_names():
    for f in listdir(text_demos):
        names.append(f.replace('.txt', ''))
    print("get_names done")

# Will remove posix newlines ('\n') and replace w/ spaces
def get_texts():
    for f in listdir(text_demos):
        file = open(text_demos + f, 'r', encoding='utf-8') # need to specify encoding to work on windows
        currText = file.read().replace('\n', ' ')
        texts.append(currText)
    print("get_texts done")

# grab the "good-looking" name of a demo
def get_proper_names():
    for f in listdir(text_demos):
        file = open(text_demos + f, 'r', encoding='utf-8')
        currline = " ".join(file.readline().split())
        proper_names.append(currline)
    print("get_proper_names done")

def get_categories():
    for f in listdir(text_demos):
        file = open(text_demos + f, 'r', encoding='utf-8')
        firstline = file.readline()
        # only want the last line of the file where category is
        for lastline in file:
            pass
        # get rid of extra spaces
        lastline = " ".join(lastline.split())
        # remove page number
        lastline = ''.join([i for i in lastline if not i.isdigit()])
        # get rid of spaces around slashes
        lastline = lastline.replace(' /', '/')
        lastline = lastline.replace('/ ', '/')
        # fix Liquids, Solids, and Colloids harvard comma
        lastline = lastline.replace('Liquids, Solids and Colloids', 'Liquids, Solids, and Colloids')

        # add to the list
        categories.append(lastline)
    print("get_categories done")


# goes collects elements from all lists to form database entries and adds them
def add_to_db():
    bar = Bar('Committing demos to DB', max=108)
    for (a, b, c, d) in zip(names, texts, proper_names, categories):
        dem = Demo(name=a, text=b, proper_name=c, category=d) 
        db.session.add(dem)
        db.session.commit()
        bar.next()
    bar.finish()

get_names()
get_texts()
get_proper_names()
get_categories()
add_to_db()
