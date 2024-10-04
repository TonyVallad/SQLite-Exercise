# SQLite Client and Order Management System

<img src="https://raw.githubusercontent.com/TonyVallad/SQLite-Exercise/refs/heads/main/resources/MCD.png" width="850"/>
MCD

This project is a simple SQLite-based management system for clients and their orders. It consists of two main components:
1. Importing client and order data from CSV files into an SQLite database.
2. Retrieving and displaying specific data related to clients and their orders based on predefined queries.

## Project Structure

```
project-directory/
│
├── resources/
│   ├── jeu-de-donnees-clients-66fed38c68779376654152.csv
│   └── jeu-de-donnees-commandes-66fe65226fdb5678959707.csv
│
├── import-from-csv.py
├── data-extraction.py
└── database.db
```

### Files

- `resources/`: This directory contains the CSV files with client and order data.
  - `jeu-de-donnees-clients-66fed38c68779376654152.csv`: CSV file containing client data.
  - `jeu-de-donnees-commandes-66fe65226fdb5678959707.csv`: CSV file containing order data.
  
- `import-from-csv.py`: This script creates an SQLite database and imports data from the CSV files into two tables: `clients` and `commandes`.

- `data-extraction.py`: This script queries the SQLite database to retrieve and display various information about clients and their orders.

- `database.db`: SQLite database file created by `import-from-csv.py`.

## Requirements

- Python 3.x
- SQLite3 (comes pre-installed with Python)

## Getting Started

### Installation

1. Clone the repository or download the project files.
2. Ensure that you have Python 3 installed on your machine.
3. Navigate to the project directory in your terminal.

### Importing Data

1. Open a terminal and run the following command to import the client and order data into the SQLite database:

   ```bash
   python import-from-csv.py
   ```

2. After running the script, the data will be imported into `database.db`.

### Querying Data

1. After importing the data, run the following command to execute various queries and retrieve client and order information:

   ```bash
   python data-extraction.py
   ```

2. The script will display:
   - List of clients who consented to marketing.
   - List of orders for client ID = 46.
   - Total purchases for client ID = 61.
   - List of clients with orders above 100€.
   - List of clients who ordered after January 1, 2023.

## Usage

You can modify the scripts to include additional functionality or queries as needed. The scripts are designed to be straightforward and easily adaptable for further development.

## License

This project is open-source and available for modification and distribution. Please feel free to contribute or use it for educational purposes.