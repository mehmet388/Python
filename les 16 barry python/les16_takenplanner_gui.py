import tkinter as tk
from tkinter import messagebox
import json
from pathlib import Path


# =========================
# Taak class
# =========================
class Taak:
    def __init__(self, titel, klaar=False):
        self.titel = titel
        self.klaar = klaar

    def to_dict(self):
        return {
            "titel": self.titel,
            "klaar": self.klaar
        }

    @staticmethod
    def from_dict(data):
        return Taak(
            data["titel"],
            data["klaar"]
        )


# =========================
# Takenlijst class
# =========================
class Takenlijst:
    def __init__(self):
        self.taken = []
        self.filename = "taken_gui.json"

    def voeg_toe(self, titel):
        taak = Taak(titel)
        self.taken.append(taak)

    def markeer_klaar(self, index):
        if 0 <= index < len(self.taken):
            self.taken[index].klaar = True

    def verwijder(self, index):
        if 0 <= index < len(self.taken):
            self.taken.pop(index)

    def save(self):
        data = [taak.to_dict() for taak in self.taken]

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):
        if not Path(self.filename).exists():
            return

        with open(self.filename) as f:
            data = json.load(f)

        self.taken = [Taak.from_dict(d) for d in data]


# =========================
# GUI App
# =========================
class TakenApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Takenplanner")

        # Takenlijst
        self.lijst = Takenlijst()
        self.lijst.load()

        # Entry
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(padx=10, pady=5)

        # Buttons frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        # Buttons
        self.btn_add = tk.Button(
            btn_frame,
            text="Toevoegen",
            command=self.on_add
        )
        self.btn_add.grid(row=0, column=0, padx=5)

        self.btn_done = tk.Button(
            btn_frame,
            text="Klaar",
            command=self.on_done
        )
        self.btn_done.grid(row=0, column=1, padx=5)

        self.btn_delete = tk.Button(
            btn_frame,
            text="Verwijderen",
            command=self.on_delete
        )
        self.btn_delete.grid(row=0, column=2, padx=5)

        self.btn_save = tk.Button(
            btn_frame,
            text="Opslaan",
            command=self.on_save
        )
        self.btn_save.grid(row=0, column=3, padx=5)

        # Listbox
        self.listbox = tk.Listbox(
            self.root,
            width=60,
            height=12
        )
        self.listbox.pack(padx=10, pady=5)

        # Taken tonen
        self.refresh_listbox()

    # =========================
    # Listbox vernieuwen
    # =========================
    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)

        for taak in self.lijst.taken:
            status = "✅" if taak.klaar else "⬜"
            self.listbox.insert(
                tk.END,
                f"{status} {taak.titel}"
            )

    # =========================
    # Geselecteerde taak
    # =========================
    def get_selected_index(self):
        selectie = self.listbox.curselection()

        if not selectie:
            return None

        return selectie[0]

    # =========================
    # Toevoegen
    # =========================
    def on_add(self):
        titel = self.entry.get().strip()

        if titel == "":
            messagebox.showwarning(
                "Fout",
                "Titel mag niet leeg zijn."
            )
            return

        self.lijst.voeg_toe(titel)

        self.entry.delete(0, tk.END)

        self.refresh_listbox()

    # =========================
    # Klaar markeren
    # =========================
    def on_done(self):
        idx = self.get_selected_index()

        if idx is None:
            messagebox.showinfo(
                "Info",
                "Selecteer eerst een taak."
            )
            return

        self.lijst.markeer_klaar(idx)

        self.refresh_listbox()

    # =========================
    # Verwijderen
    # =========================
    def on_delete(self):
        idx = self.get_selected_index()

        if idx is None:
            messagebox.showinfo(
                "Info",
                "Selecteer eerst een taak."
            )
            return

        self.lijst.verwijder(idx)

        self.refresh_listbox()

    # =========================
    # Opslaan
    # =========================
    def on_save(self):
        self.lijst.save()

        messagebox.showinfo(
            "Opgeslagen",
            "Taken zijn opgeslagen!"
        )

    # =========================
    # App starten
    # =========================
    def run(self):
        self.root.mainloop()


# =========================
# Startpunt
# =========================
if __name__ == "__main__":
    app = TakenApp()
    app.run()