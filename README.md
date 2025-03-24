# cloudNative_hw1: Cloudshop

`cloudShop` is a command-line marketplace platform where users can register, create listings, browse by category, and view the most popular categories. This project follows a clean layered architecture and is built using **only Python standard library features**.

---

## Installation and Execution

### ✅ Requirements
- Python 3.8 or above
- SQLite (bundled with standard Python via `sqlite3`)

---

### 📥 Clone the Project

You can clone this repository using `git`:

```bash
git clone https://github.com/wayne-yang7021/cloudNative_hw1.git
cd cloudNative_hw1
```

### How to run the app?
Open an terminal, type

```bash
make
```

The code should show something like:
```bash
sh run.sh
🔧 Initializing the database...
✅ Database initialized.
🚀 Running cloudNative_hw1...
# 
```

⚠️ If the above method doesn't work, please run:

```bash
# Step 1: Initialize the database
python -c "from persistence.database import init_db; init_db()"

# Step 2: Start the CLI application
python run.py

```

## 📚 Command Reference

| Command                                 | Description                               |
|-----------------------------------------|-------------------------------------------|
| `REGISTER <username>`                   | Registers a new user                      |
| `CREATE_LISTING <username> <title> <desc> <price> <category>` | Adds a new listing           |
| `GET_LISTING <username> <listing_id>`   | Fetches listing details by ID             |
| `GET_CATEGORY <username> <category>`    | Lists all listings in a category          |
| `GET_TOP_CATEGORY <username>`           | Returns the most popular category         |
| `DELETE_LISTING <username> <listing_id>`| Deletes a listing if user is owner        |

> Error messages like `"Error - unknown user"`, `"Error - listing does not exist"` will be shown as needed.


## 📦 Project Structure

```plaintext
cloudNative_hw1/
│
├── run.py                  # Entry point for the CLI application
├── run.sh                  # Shell script to run the project
├── Makefile                # Build script (if needed)
├── README.md               # This file
│
├── domain/                 # Domain layer (core entities)
│   └── models.py           # Domain models (User, Listing)
│
├── persistence/            # Persistence layer (data access)
│   ├── database.py         # SQLite connection + schema init
│   ├── user_repository.py  # Data access for users
│   ├── listing_repository.py # Data access for listings
│   └── category_repository.py # Data access for categories
│
├── service/                # Service layer (business logic)
│   ├── user_service.py
│   ├── listing_service.py
│   └── category_service.py
│
└── presentation/           # Presentation layer (CLI parsing)
    └── command_processor.py
```


## 🧱 Architecture

This project follows a **4-layer architecture** to ensure clean separation of concerns, maintainability, and extensibility. The design is inspired by typical backend layering (like Spring Boot) but adapted for a pure Python CLI application.

### Layer Overview
| Layer               | Description               |
|---------------------|---------------------------|
| Presentation Layer  | CLI command parsing       |
| Service Layer       | Business logic & validation |
| Persistence Layer   | SQLite data access (CRUD) |
| Domain Layer        | Core entities (User, Listing) |

---

### 1. Presentation Layer  
**Folder:** `presentation/`  
**Responsibility:**  
- Parses CLI commands from `STDIN`
- Routes commands to corresponding service functions
- Formats and prints output to `STDOUT`

**Why:** Keeps user interaction logic separate from application logic. Easy to test and replace (e.g., switch to API in the future).

---

### 2. Service Layer  
**Folder:** `service/`  
**Responsibility:**  
- Implements business logic and rules
- Validates inputs and coordinates multiple repositories
- Handles logic like ownership checks, sorting, filtering

**Why:** Central place for business logic, independent of CLI or database. Promotes reusability and testability.

---

### 3. Persistence Layer  
**Folder:** `persistence/`  
**Responsibility:**  
- Manages all SQLite database interactions
- Provides repositories to read/write `User`, `Listing`, `Category`
- Initializes schema (`init_db()`)

**Why:** Isolates raw SQL from business logic. Makes storage engine replaceable with minimal effort.

---

### 4. Domain Layer  
**Folder:** `domain/`  
**Responsibility:**  
- Defines core entities like `User` and `Listing`
- Encapsulates data


