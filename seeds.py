import json
from datetime import datetime
import connect
from models import Authors, Quotes



with open('hw08/prt_1/authors.json', 'r') as fd:
    authors = json.load(fd)

with open('hw08/prt_1/quotes.json', 'r') as fd:
    quotes = json.load(fd)

authors_dict = {}

for author in authors:  
    author = Authors(fullname=author['fullname'],
            born_date=author['born_date'], 
            born_location=author['born_location'],
            description=author['description'])
    authors_dict.update({author.fullname : author})
    author.save()

print(authors_dict)
    


for quote in quotes:
        Quotes(tags=quote['tags'],
                author=authors_dict[quote['author']],
                quote=quote['quote']).save()

