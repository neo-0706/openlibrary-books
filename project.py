from http.client import responses
import requests
import csv
from typing import Dict,List
from typing import TypedDict

class BookData(TypedDict):
    title: str
    author: str
    year: int
    subjects: str

def fetch_books() -> None | list[Dict]:

    params: Dict[str, str | int] ={
        'q': 'olympics',
        'limit': 50
    }

    url:str = 'https://openlibrary.org/search.json'
    try:
        response: requests.Response = requests.get( url ,params=params , timeout=30)
        
        response.raise_for_status()

        data: Dict[str , any] = response.json()
        books : List[Dict[str ,  any]] = data['docs']
        return books

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err :
        print(f'other error occurred: {err}' )

def save_to_csv(books_list: list[Dict]) -> None:
    filtered_books: List[BookData]= []

    for book in books_list:
        subjects_list = book.get('subject' , [])
        subjects_str = ', '.join(subjects_list[:3]) if subjects_list else 'unknown'
        year: int | None = book.get('first_publish_year')
        authors: List[str] = book.get('author_name' , [])
        author_name :str = authors[0] if authors else 'unknown'
        if year and year > 2000:
            filtered_books.append({ 
                'title': book.get('title', 'unknown'),
                'author': author_name,
                'year': year ,
                'subjects': subjects_str
            })
    with open ('books_after_2000.csv' , 'w' , newline='', encoding='utf-8') as f :
        writer = csv.DictWriter(f , fieldnames=['title' , 'author' , 'year' , 'subjects'])
        writer.writeheader()
        writer.writerows(filtered_books)
    print(f'{len(filtered_books)} books saved in file.')

if __name__ == "__main__":
    results = fetch_books()
    if results:
        save_to_csv(results)