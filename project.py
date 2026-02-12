import requests
import csv
import json

params={
    'q': 'olympics',
    'limit': 50
}
url = 'https://openlibrary.org/search.json'

response = requests.get( url ,params=params , timeout=30)
data = response.json()
books = data['docs']
filtered_books= []
for book in books:
    year = book.get('first_publish_year')
    if year and year > 2000:
        filtered_books.append({ 
            'title': book.get('title', 'نامشخص'),
            'author': book.get('author_name', ['نامشخص'])[0] if book.get('author_name') else 'نامشخص',
            'year': year
        })
with open ('books_after_2000.csv' , 'w' , newline='', encoding='utf-8') as f :
    writer = csv.DictWriter(f , fieldnames=['title' , 'author' , 'year'])
    writer.writeheader()
    writer.writerows(filtered_books)
print(f'{len(filtered_books)} books saved in file.')