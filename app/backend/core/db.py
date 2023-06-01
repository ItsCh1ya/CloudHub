import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('database.db', check_same_thread=False) # it just works
cur = con.cursor()

# Create the table
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                email TEXT UNIQUE
            )''')

# Save the changes and close the connection
con.commit()

# Function to register a new user
def register(username: str, password: str, email: str):    
    cur.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
    con.commit()
    return cur.lastrowid

# Function to log in an existing user
def login(email: str, password: str):
    cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cur.fetchone()
    if user:
        print("Login successful!")
        return user
    else:
        print("Invalid username or password.")
        raise Exception("Invalid username or password.")