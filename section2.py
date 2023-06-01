from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()


class Book:
    id: int
    author: str
    title: str
    pages: int

    def __init__(self, id, author, title, pages) -> None:
        self.id = id
        self.author = author
        self.title = title
        self.pages = pages


BOOKS = [
    Book(1, "test_author", "title1", 3),
    Book(2, "test_author2", "title1", 4),
    Book(3, "test_author3", "title1", 6),
]


class BookRequest(BaseModel):
    id: Optional[int] = Field(gt=0)
    author: str = Field(min_length=5)
    title: str = Field(min_length=3)
    pages: int = Field(gt=0)


@app.get("/Books")
def all_book():
    return BOOKS


@app.get("/book/{id}")
def get_book_by_id(id: int):
    for book in BOOKS:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Book id is not present.")


@app.post("/book")
def add_book(book: BookRequest):
    BOOKS.append(book)


@app.delete("/book")
def delete_book_by_id(id:int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == id:
            BOOKS.pop(i)
            break

