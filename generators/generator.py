import sys
import os
import csv
import codecs
from django.template import Template, Context
from django.template import loader
from django.conf import settings


with open('businesscards_2013.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    rows = []
    for row in reader:
        info = {
            'name'     : row[0],
            'position' : row[1],
            'phone'    : row[2],
            'email'   : row[3],
            'homepage' : row[4],
            'address'  : row[5]
        }

        rows.append(info)
        #print(info)
    
    PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
    print(PROJECT_DIR)
    settings.configure(
        TEMPLATE_DIRS=(os.path.join(PROJECT_DIR, 'templates'),),
        INSTALLED_APPS=('mathfilters',)
    )
    t = loader.get_template('cards.sla')
    c = Context({
        'PAGEYPOS': 20.0012598425197,
        'PAGEHEIGHT': 155.905511811024,
        'rows': rows
    })

    f = codecs.open(os.path.join(PROJECT_DIR, 'generated_cards.sla'), "w", encoding="utf-8")
    f.write(t.render(c))
    f.close()
