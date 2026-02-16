# 📚 OpenLibrary Books Fetcher

A Python script that fetches 50 books from the OpenLibrary API, filters books published after the year 2000, and saves the results in a CSV file.

## 🚀 Features

- Fetches book data from OpenLibrary public API
- Filters books with `first_publish_year > 2000`
- Extracts: **Title**, **Author**, **Year**
- Saves output to `books_after_2000.csv`
- Handles missing data gracefully (defaults: 'Unknown')

## 🛠 Requirements

- Python 3.x
- `requests` library

Install dependencies:

```bash
pip install requests
```

## 📦 Usage

1. Clone or download this repository
2. Run the script:

```bash
python3 project.py
```

3. The result will be saved as `books_after_2000.csv`

## 📄 Output Example

| title | author | year |
|-------|--------|------|
| The Hunger Games | Suzanne Collins | 2008 |
| Harry Potter and the Deathly Hallows | J.K. Rowling | 2007 |
| Twilight | Stephenie Meyer | 2005 |

## 🧠 How It Works
- Sends a GET request to `https://openlibrary.org/search.json`
- Retrieves 50 books (query: `olympics`)
- Filters books with `first_publish_year > 2000`
- **Automatically creates `books_after_2000.csv` file and saves the filtered data**
- Uses `csv.DictWriter` to write data in CSV format

## 📁 Project Structure

```
.
├── project.py          # Main script
├── books_after_2000.csv      # Output file (generated)
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies
```

## 👤 Author

**Mohammad Hosein shahsavand Baghdadi**  
[GitHub Profile](https://github.com/neo-0706)

## 📌 Note

This project was created as part of a university assignment.  
OpenLibrary API is free and open for public use.
