import requests
import os
from dotenv import load_dotenv

API_URL = "https://www.googleapis.com/books/v1/volumes"

class Book:

    def __init__(self, title, authors, publisher):
        self.title = title 
        self.authors = authors
        self.publisher = publisher

    @classmethod
    def from_api_data(cls, item):
        info = item.get("volumeInfo", {})
        title = info.get("title", "Unknown Title")
        authors = info.get("authors", ["Unknown Author"])
        publisher = info.get("publisher", "Unknown Publisher")

        return cls(title, authors, publisher)

def search_books(api_key, query):

    params = {
        "q": query,
        "maxResults": 5,
        "key": api_key
    }

    response = requests.get(API_URL, params=params, timeout=15)

    response.raise_for_status()

    data = response.json()

    books = []

    for item in data.get("items", []):
        book = Book.from_api_data(item)
        books.append(book)

    return books


def display_books(books):

    if not books:
        print("No books found.")
        return

    for index, book in enumerate(books, start=1):

        print(f"\nBook #{index}")
        print("Title:", book.title)
        print("Authors:", ", ".join(book.authors))
        print("Publisher:", book.publisher)


def main():

    load_dotenv()

    api_key = os.getenv("GOOGLE_BOOKS_API_KEY")

    if not api_key:
        print("API Key not found. Check your .env file.")
        return

    query = input("Enter book title or author: ")

    books = search_books(api_key, query)

    display_books(books)


if __name__ == "__main__":
    main()