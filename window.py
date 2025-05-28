import tkinter as tk
import database
from tkinter import messagebox

class NewRoot():
    # attributi di classe
    default_geometry = "400x300"
    default_root_behaviour = (False, False)

    def __init__(self, title, label_text, num_page):

        self.title = str(title)
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(NewRoot.default_geometry)
        self.root.resizable(*NewRoot.default_root_behaviour)

        # self.label_counter = label_counter
        # self.entry_counter = entry_counter
        # self.button_counter = button_counter
        self.num_page = num_page
        # self.num_button = num_button
        self.label_text = label_text
        self.create_widgets()

    def create_widgets(self):

       
        self.entry_vars = []
        z = 0
        
        if self.num_page == 0:
            button_login = tk.Button(self.root, text="Login", command=self.mostra_login)
            button_login.grid(column=0, row=0)

            button_registrazione = tk.Button(self.root, text="Registrati", command=self.mostra_registrazione)
            button_registrazione.grid(column=0, row=1)
        elif self.num_page == 1:
            for i, text in enumerate(self.label_text):
                label = tk.Label(self.root, text=text)
                label.grid(column=0, row=i)
                var = tk.StringVar()
                entry = tk.Entry(self.root, textvariable=var)
                entry.grid(column=1, row=i)
                self.entry_vars.append(var)
            button_press = tk.Button(self.root, text="press", command=self.azione_login)
            button_press.grid(column=2, row=i)
        elif self.num_page == 2:
            for i, text in enumerate(self.label_text):
                label = tk.Label(self.root, text=text)
                label.grid(column=0, row=i)
                var = tk.StringVar()
                entry = tk.Entry(self.root, textvariable=var)
                entry.grid(column=1, row=i)
                self.entry_vars.append(var)
            button_press = tk.Button(self.root, text="press", command=self.azione_registrazione)
            button_press.grid(column=2, row=i)
    
    def close_window(self):
        self.root.destroy()

    def stampa_valori(self):
        for var in self.entry_vars:
            print(var.get())

    def mostra_login(self):
        self.root.destroy()
        NewRoot("Login", ["Utente", "Pin"], 1)

    def mostra_registrazione(self):
        self.root.destroy()
        NewRoot("Registrazione", ["Utente", "Pin"], 2)

    def azione_login(self):
        username = self.entry_vars[0].get()
        pin = self.entry_vars[1].get()
        if database.verifica_utente(username, pin):
            print("l'utente è stato verificato")
        else:
            print("l'utente non è stato verificato")

    def azione_registrazione(self):
        username = self.entry_vars[0].get()
        pin = self.entry_vars[1].get()
        if database.registra_utente(username, pin):
            messagebox.showinfo("Info registrazione", f"L'utente {username} è stato registrato correttamente")
        else:
            messagebox.showwarning("Attenzione", f"l'utente {username} è gia stato inserito nel database!")

