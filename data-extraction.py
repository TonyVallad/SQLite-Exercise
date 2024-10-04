import sqlite3

# Create a SQLite connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# 1. Show the list of clients who consented to marketing
print("\n\033[1;34mList of clients who consented to marketing:\033[0m")
cursor.execute('''
    SELECT Client_ID, Nom, Prénom, Email 
    FROM clients 
    WHERE Consentement_Marketing = 1
''')
clients_consent_marketing = cursor.fetchall()
for client in clients_consent_marketing:
    # Format output as specified
    print(f"{client[0]} - {client[1]}, {client[2]} - {client[3]}")

# 2. Show the list of orders for client id=46
print("\n\033[1;34mList of orders for client ID = 46:\033[0m")
cursor.execute('''
    SELECT * 
    FROM commandes 
    WHERE Client_ID = 46
''')
orders_client = cursor.fetchall()
for order in orders_client:
    print(f"Commande no {order[0]} - {order[2]} - Amount {order[3]}")

# 3. Show the sum of all purchases for client id=61
print("\n\033[1;34mSum of all purchases for client 61:\033[0m")
cursor.execute('''
    SELECT SUM(Montant_Commande) 
    FROM commandes 
    WHERE Client_ID = 61
''')
total_purchases_client = cursor.fetchone()[0]
print(f"Total purchases for client ID = 61: {total_purchases_client}")

# 4. Show the list of clients with orders above 100€
print("\n\033[1;34mClients with orders above 100€:\033[0m")
cursor.execute('''
    SELECT c.Client_ID, c.Nom, c.Prénom, COUNT(*) as nb_orders 
    FROM clients c
    JOIN commandes o ON c.Client_ID = o.Client_ID
    WHERE o.Montant_Commande > 100
    GROUP BY c.Client_ID, c.Nom, c.Prénom
''')
clients_above_100 = cursor.fetchall()
for client in clients_above_100:
    # Format output as specified
    print(f"{client[0]} - {client[1]}, {client[2]} - {client[3]} orders")

# 5. Show the list of clients who ordered after 2023-01-01
print("\n\033[1;34mClients who ordered after 2023-01-01:\033[0m")
cursor.execute('''
    SELECT DISTINCT c.Client_ID, c.Nom, c.Prénom 
    FROM clients c
    JOIN commandes o ON c.Client_ID = o.Client_ID
    WHERE o.Date_Commande > '2023-01-01'
''')
clients_after_date = cursor.fetchall()
for client in clients_after_date:
    # Format output as specified
    print(f"{client[0]} - {client[1]}, {client[2]}")

print()

# Close the connection
conn.close()
