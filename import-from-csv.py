import sqlite3
import csv

# File paths for CSV files
clients_file_path = 'resources/jeu-de-donnees-clients-66fed38c68779376654152.csv'
commandes_file_path = 'resources/jeu-de-donnees-commandes-66fe65226fdb5678959707.csv'

# Create a SQLite connection and cursor
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create Clients Table with constraints
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        Client_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nom TEXT NOT NULL,
        Prénom TEXT NOT NULL,
        Email TEXT NOT NULL UNIQUE,
        Téléphone TEXT,
        Date_Naissance DATE,
        Adresse TEXT,
        Consentement_Marketing INTEGER NOT NULL CHECK (Consentement_Marketing IN (0, 1))
    )
''')

# Create Commandes Table with constraints
cursor.execute('''
    CREATE TABLE IF NOT EXISTS commandes (
        Commande_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Client_ID INTEGER NOT NULL,
        Date_Commande DATE NOT NULL,
        Montant_Commande REAL NOT NULL,
        FOREIGN KEY (Client_ID) REFERENCES clients(Client_ID) ON DELETE CASCADE
    )
''')

# Function to insert data into a table
def insert_data_from_csv(file_path, table_name, cursor, conn):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row
        placeholders = ','.join('?' * len(headers))
        query = f"INSERT INTO {table_name} ({','.join(headers)}) VALUES ({placeholders})"
        
        for row in reader:
            cursor.execute(query, row)
        conn.commit()

# Insert data into clients table
insert_data_from_csv(clients_file_path, 'clients', cursor, conn)

# Insert data into commandes table
insert_data_from_csv(commandes_file_path, 'commandes', cursor, conn)

# Close the connection
conn.close()

print("\n\033[1;32mData imported successfully into SQLite database.\033[0m\n")
