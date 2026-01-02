import json
import os

DATA_FILE = "data.json"

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

class Library:
    def __init__(self):
        self.books = self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, title, author):
        self.books.append({
            "title": title,
            "author": author,
            "borrowed": False
        })
        self.save_data()
        print("Book added successfully")

    def search_book(self, title):
        for book in self.books:
            if title.lower() in book["title"].lower():
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book["title"] == title and not book["borrowed"]:
                book["borrowed"] = True
                self.save_data()
                print("Book borrowed")
                return
        print("Book unavailable")

library = Library()

while True:
    print("\n1.Add Book 2.Search Book 3.Borrow Book 4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        library.add_book(input("Title: "), input("Author: "))
    elif choice == "2":
        library.search_book(input("Title to search: "))
    elif choice == "3":
        library.borrow_book(input("Title to borrow: "))
    elif choice == "4":
        break
