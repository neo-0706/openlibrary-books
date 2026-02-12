import requests
import csv
import json

params={
    'q': 'fiction',
    'limit': 50
}
url = 'https://openlibrary.org/search.json'

response = requests.get( url ,params=params , timeout=30)
data = response.json()
books = data['docs']
filtered_books= {}
for book in books:
    if book['first_publish_year'] > 2000:
        filtered_books['title'] = book['']
        filtered_books['year'] = book['first_publish_year']
    
with open ()
# for book in data:
#     print(book['reading_log_entries']['work']['first_publish_year'])