import sqlite3


# Database verbinden / maken
def connect_db():
    return sqlite3.connect("taken.db")


# Tabel maken
def init_db():
    conn = connect_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS taken (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titel TEXT NOT NULL,
            klaar INTEGER NOT NULL DEFAULT 0
        )
    """)

    conn.close()


# Taak toevoegen
def add_taak(titel):
    conn = connect_db()

    conn.execute(
        "INSERT INTO taken (titel, klaar) VALUES (?, 0)",
        (titel,)
    )

    conn.commit()
    conn.close()


# Taken ophalen
def get_taken():
    conn = connect_db()

    rows = conn.execute(
        "SELECT id, titel, klaar FROM taken"
    ).fetchall()

    conn.close()

    return rows


# Taak als klaar markeren
def markeer_klaar(taak_id):
    conn = connect_db()

    conn.execute(
        "UPDATE taken SET klaar = 1 WHERE id = ?",
        (taak_id,)
    )

    conn.commit()
    conn.close()


# Taak verwijderen
def verwijder_taak(taak_id):
    conn = connect_db()

    conn.execute(
        "DELETE FROM taken WHERE id = ?",
        (taak_id,)
    )

    conn.commit()
    conn.close()


# Taken tonen
def toon_taken():
    taken = get_taken()

    if not taken:
        print("(Geen taken)")
        return

    print("\nTaken:")

    for taak_id, titel, klaar in taken:
        status = "✅" if klaar == 1 else "⬜"
        print(f"{taak_id}. {status} {titel}")


# Main programma
def main():
    init_db()

    while True:
        print("\n=== TAKENPLANNER (SQLITE) ===")
        print("1) Toon taken")
        print("2) Voeg taak toe")
        print("3) Markeer taak als klaar")
        print("4) Verwijder taak")
        print("0) Stoppen")

        keuze = input("Kies: ").strip()

        if keuze == "1":
            toon_taken()

        elif keuze == "2":
            titel = input("Taak titel: ").strip()

            if titel == "":
                print("Titel mag niet leeg zijn.")
            else:
                add_taak(titel)
                print("Taak toegevoegd!")

        elif keuze == "3":
            toon_taken()

            taak_id = input("Welke ID klaar zetten: ").strip()

            if taak_id.isdigit():
                markeer_klaar(int(taak_id))
                print("Taak gemarkeerd als klaar!")
            else:
                print("Ongeldig ID.")

        elif keuze == "4":
            toon_taken()

            taak_id = input("Welke ID verwijderen: ").strip()

            if taak_id.isdigit():
                verwijder_taak(int(taak_id))
                print("Taak verwijderd!")
            else:
                print("Ongeldig ID.")

        elif keuze == "0":
            print("Tot ziens!")
            break

        else:
            print("Ongeldige keuze.")


# Startpunt
if __name__ == "__main__":
    main()