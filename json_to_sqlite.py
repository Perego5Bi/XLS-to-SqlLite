import sqlite3
import json

# Crea una connessione al database SQLite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Crea la tabella
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    media_voti REAL,
    esito TEXT
)
''')

# Carica i dati JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Inserisci i dati nel database
for entry in data:
    cursor.execute('''
    INSERT INTO students (name, average_grade, final_decision)
    VALUES (?, ?, ?)
    ''', (entry['name'], entry['average_grade'], entry['final_decision']))

# Salva le modifiche e chiudi la connessione
conn.commit()
conn.close()