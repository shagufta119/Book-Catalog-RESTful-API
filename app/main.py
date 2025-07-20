"""
Entry point for the Book Catalog API application.
Handles initialization and routing of the API service.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app import crud, models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="📚 Book Catalog ", description= "A RESTFUL API that allows users to manage books:")

@app.get("/books/", response_model=list[schemas.BookRead], summary="📚 List All Books", tags=["Books"])
async def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.get("/books/{book_id}", response_model=schemas.BookRead, summary="📖 Get Book Details", tags=["Books"])
async def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.post("/books/", response_model=schemas.BookRead, summary="➕ Create a New Book", tags=["Books"])
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

@app.put("/books/{book_id}", response_model=schemas.BookRead, summary="✏️ Update Book", tags=["Books"])
async def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    updated_book = crud.update_book(db=db, book_id=book_id, book=book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@app.delete("/books/{book_id}", summary="🗑️ Delete Book", tags=["Books"])
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
