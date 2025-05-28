# Gestionale Login con Tkinter + SQLite

Un semplice gestionale con interfaccia grafica realizzato in Python, che permette all'utente di:

- Effettuare il **login** con username e pin
- **Registrarsi** creando un nuovo account
- Salvare e verificare i dati tramite un **database SQLite locale**

---

## 🖼️ Interfaccia

L'interfaccia è realizzata con `tkinter` e presenta 3 schermate principali:

1. **Schermata iniziale**
   - Scegli se effettuare il login o registrarti

2. **Login**
   - Inserisci `username` e `pin`
   - Se le credenziali sono corrette, visualizza un messaggio di successo

3. **Registrazione**
   - Inserisci `username` e `pin`
   - Se l'utente non esiste già, viene registrato nel database

---

## 🛠️ Struttura del progetto

```
gestionale-login/
├── prova1_window.py     # Avvio dell'interfaccia
├── window.py            # Classe per gestire la GUI
├── database.py          # Funzioni di interazione con SQLite
├── gestionale.db        # Database locale (opzionale da includere)
└── README.md
```

---

## 💾 Requisiti

- Python 3.8+
- Nessuna libreria esterna: usa solo `tkinter` e `sqlite3` (entrambe built-in)

---

## ▶️ Avvio

```bash
python prova1_window.py
```

---

## 📌 Note

- Il database viene creato automaticamente alla prima esecuzione (`gestionale.db`)
- Le credenziali vengono salvate in chiaro (senza hashing) per semplicità
- È consigliabile **non includere `gestionale.db`** nel repository (`.gitignore`)

---

## 🚀 Prossimi sviluppi (idee)

- Hashing delle password (es. con `hashlib`)
- Aggiunta di un'interfaccia grafica più avanzata (con `customtkinter` o `ttk`)
- Creazione di un'area riservata post-login
- Logica di logout e gestione multiutente

---

## 👨‍💻 Autore

**Lorenzo B.**  
Progetto realizzato per studio e portfolio personale.
