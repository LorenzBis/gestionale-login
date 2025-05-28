import sqlite3

def registra_utente(username, pin):
    try:
        cur.execute("INSERT INTO user (username, pin) VALUES (?, ?)", (username, pin))
        con.commit()
        print("L'utente è stato inserito correttamente")
        return True
    except sqlite3.IntegrityError:
        print("L'utente è gia stato inserito")
        return False

def verifica_utente(username, pin):
    cur.execute("SELECT * FROM user WHERE username = ? AND pin = ?", (username, pin))
    return cur.fetchone() is not None


con = sqlite3.connect("gestionale.db")
cur = con.cursor()

if __name__ == "__main__":

    try: 
        cur.execute("""CREATE TABLE IF NOT EXISTS user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    pin INTEGER
                    )""")
        con.commit()

        if verifica_utente("paolo1", 123):
            print(f"Utente verificato")
        else:
            print("Utente non verificato")

    except sqlite3.OperationalError as e:
        print(e)

    except sqlite3.IntegrityError as e:
        print(e)
