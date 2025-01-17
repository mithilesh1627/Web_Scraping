# Web Scraping and MongoDB Integration Projects

This repository contains a collection of Python scripts for web scraping and MongoDB integration. Each script demonstrates different techniques for extracting data from websites and storing it in MongoDB. The projects include book scraping, movie data scraping, and exporting database content to JSON format.

## Projects

### 1. Export Database Class
**File:** `Export_Database_class.py`

A Python class to export MongoDB collections to JSON files. It connects to a MongoDB database, retrieves data from collections, and writes the data to JSON files.

**Key Functions:**
- `json_encoder(obj)`: Handles serialization of ObjectId to JSON.
- `Export_database(DatabaseName, export_path)`: Exports the specified database to JSON files at the given path.

### 2. Get Book Details
**File:** `Get_Book_Details.py`

A web scraping script that extracts book details from an online bookstore. The data is stored in MongoDB collections based on book categories.

**Key Functions:**
- `get_book_details(url, soup, availability=False)`: Scrapes book details from the provided URL and stores them in MongoDB.
- `insertInMongoDB(document, book_category_name)`: Inserts scraped data into MongoDB.

### 3. Scrap All Books
**File:** `Scrap_all_Books.py`

A comprehensive web scraping script that iterates through all book categories on the website, scrapes details of each book, and stores the data in MongoDB.

**Key Functions:**
- `next_page(url, current_page, total_page)`: Navigates through paginated book listings.
- `get_next_page(book_category_name, url)`: Handles the retrieval of book details for all pages in a category.

### 4. Top 250 Movies with PyMongo
**File:** `Top250Movies_pymongo.py`

A script that scrapes the top 250 movies from IMDb and stores the movie details, including rank, name, release year, poster URL, and rating, into a MongoDB collection.

**Key Functions:**
- `insertInMongoDB(dictionary)`: Inserts movie data into MongoDB.

### 5. Travel Book Scraping with MongoDB
**File:** `Travel_Book_scraping_with_mongodb.py`

A focused web scraping script for extracting travel book details from an online bookstore. It converts the price from EUR to INR and stores the data in MongoDB.

**Key Functions:**
- `insertInMongoDB(dictionary)`: Inserts travel book data into MongoDB.
- `currency_converter(amount)`: Converts currency from EUR to INR.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```
2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the scripts:** Modify the script parameters as needed and execute them using Python.

## Prerequisites

- Python 3.x
- MongoDB installed and running locally
- Required Python packages (listed in `requirements.txt`)

## Usage

1. Set up your MongoDB connection string in the scripts.
2. Run the scripts to scrape data and store it in MongoDB.
3. Use the export script to save the scraped data as JSON files.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

