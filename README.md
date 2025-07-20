📚 Book Catalog API

A simple and well-structured RESTful API for managing a catalog of books. Built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

🚀 Features

- ✅ Add new books
- 🔄 Update existing books
- ❌ Delete books
- 📖 List all books
- 🔍 Retrieve a single book by ID
- ⚙️ Built using FastAPI, SQLAlchemy ORM, and SQLite
- 📦 Data validation with Pydantic

 🗂️ Project Structure

book-catalog/
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── models.py # SQLAlchemy database models
│ ├── schemas.py # Pydantic models (data validation)
│ └── crud.py # CRUD operations logic
├── tests/ # Unit tests (if any)
├── books.db # SQLite database
├── requirements.txt # Project dependencies
└── .gitignore

## 🛠️ Installation & Setup

1. **Clone the repository**

```bash
git remote add origin https://github.com/shagufta119/Book-Catalog-RESTful-API.git
cd book-catalog
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
🔗 API Endpoints
Method	Endpoint	Description
GET	/books/	List all books
GET	/books/{id}	Get a book by ID
POST	/books/	Add a new book
PUT	/books/{id}	Update a book by ID
DELETE	/books/{id}	Delete a book by ID
📬 Example Request (POST /books/)
json

{
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "published_year": 1988,
  "summary": "A young shepherd's journey to find treasure."
}
✅ Requirements
Python 3.8+

FastAPI

Uvicorn

SQLAlchemy

Pydantic

✨ Author
Shagufta Naseer
Web Developer & Python Programmer
📧 Shaguftatotani@gmail.com



