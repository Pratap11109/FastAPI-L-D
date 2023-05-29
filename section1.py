from fastapi import FastAPI, Body


app = FastAPI()

BOOKS = [
    {"title":"t1", "author": "a1", "subject": "math"},
    {"title":"t2", "author": "a2", "subject": "science"},
    {"title":"t3", "author": "a3", "subject": "history"},
    {"title":"t4", "author": "a1", "subject": "math"}
]

@app.get("/books")
def all_book():
    return BOOKS


@app.get("/book/{title}")
def book_by_title(title: str):
    for book in BOOKS:
        if book["title"].casefold() == title.casefold():
            return book
    return {}

@app.post("/book")
def add_book(new_book = Body()):
    BOOKS.append(new_book)
    return new_book


@app.put("/book/{title}")
def update_book(title:str, author:str):
    for book in BOOKS:

        if book["title"].casefold() == title.casefold():
            book["author"] = author
            return book
    return {} 

@app.get("/books/{author}")
def books_author_pp(author:str):
    ans = []
    for book in BOOKS:
        if book["author"].casefold() == author.casefold():
            ans.append(book)
    
    return ans

@app.get("/books/qp/")
def books_author_qp(author:str):
    ans = []
    for book in BOOKS:
        if book["author"].casefold() == author.casefold():
            ans.append(book)
    
    return ans

@app.delete("/delete/book")
def delete_book(title:str):
    ans = None
    for book in BOOKS.copy():
        if book["title"].casefold() == title.casefold():
            BOOKS.remove(book)

    return BOOKS

