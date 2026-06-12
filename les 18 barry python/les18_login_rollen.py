import json
import hashlib
from pathlib import Path



# Wachtwoord hashing

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def check_password(password: str, password_hash: str) -> bool:
    return hash_password(password) == password_hash



# User class

class User:
    def __init__(self, username: str, password_hash: str, role: str):
        self.username = username
        self.password_hash = password_hash
        self.role = role  # "admin" of "user"



# Users opslag

def load_users(filename="users.json"):
    path = Path(filename)

    if not path.exists():
        return {}

    data = json.loads(path.read_text(encoding="utf-8"))

    users = {}

    for username, u in data.items():
        users[username] = User(
            u["username"],
            u["password_hash"],
            u["role"]
        )

    return users


def save_users(users, filename="users.json"):
    data = {}

    for username, u in users.items():
        data[username] = {
            "username": u.username,
            "password_hash": u.password_hash,
            "role": u.role
        }

    Path(filename).write_text(
        json.dumps(data, indent=2),
        encoding="utf-8"
    )



# Standaard users maken

def ensure_default_users() -> None:
    users = load_users()

    if users:
        return

    admin = User(
        "admin",
        hash_password("admin123"),
        "admin"
    )

    user = User(
        "user",
        hash_password("user123"),
        "user"
    )

    save_users({
        admin.username: admin,
        user.username: user
    })



# Login

def login(users):
    print("
=== LOGIN ===")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    u = users.get(username)

    if not u:
        print("Onbekende gebruiker.")
        return None

    if not check_password(password, u.password_hash):
        print("Wachtwoord klopt niet.")
        return None

    print(f"Ingelogd als {u.username} ({u.role}).")

    return u



# Taken opslag

def load_taken(filename="taken.json"):
    path = Path(filename)

    if not path.exists():
        return []

    return json.loads(path.read_text(encoding="utf-8"))


def save_taken(taken, filename="taken.json"):
    Path(filename).write_text(
        json.dumps(taken, indent=2),
        encoding="utf-8"
    )



# Taken tonen

def toon_taken(taken, current_user):
    print("
Taken:")

    if current_user.role == "admin":
        zichtbaar = taken
    else:
        zichtbaar = [
            t for t in taken
            if t["owner"] == current_user.username
        ]

    if not zichtbaar:
        print("(Geen taken)")
        return []

    for i, t in enumerate(zichtbaar, start=1):
        status = "✅" if t["klaar"] else "⬜"

        if current_user.role == "admin":
            extra = f" (owner: {t["owner"]})"
        else:
            extra = ""

        print(f"{i}. {status} {t["titel"]}{extra}")

    return zichtbaar



# Main programma

def main():
    ensure_default_users()

    users = load_users()
    taken = load_taken()

    current_user = login(users)

    if not current_user:
        return

    while True:
        print("
=== TAKEN (LOGIN & ROLLEN) ===")
        print("1) Toon taken")
        print("2) Voeg taak toe")
        print("3) Markeer taak als klaar")
        print("4) Verwijder taak")
        print("0) Stoppen")

        keuze = input("Kies: ").strip()

        # -------------------------
        # Toon taken
        # -------------------------
        if keuze == "1":
            toon_taken(taken, current_user)

        # -------------------------
        # Voeg taak toe
        # -------------------------
        elif keuze == "2":
            titel = input("Taak titel: ").strip()

            if titel == "":
                print("Titel mag niet leeg zijn.")
                continue

            taken.append({
                "titel": titel,
                "klaar": False,
                "owner": current_user.username
            })

            save_taken(taken)

            print("Taak toegevoegd.")

        # -------------------------
        # Markeer klaar
        # -------------------------
        elif keuze == "3":
            zichtbaar = toon_taken(taken, current_user)

            try:
                nr = int(input("Welke taak (nummer): "))
            except ValueError:
                print("Ongeldig nummer.")
                continue

            if not (1 <= nr <= len(zichtbaar)):
                print("Taaknummer bestaat niet.")
                continue

            taak = zichtbaar[nr - 1]
            taak["klaar"] = True

            save_taken(taken)

            print("Taak gemarkeerd als klaar.")

        # -------------------------
        # Verwijder taak
        # -------------------------
        elif keuze == "4":
            zichtbaar = toon_taken(taken, current_user)

            try:
                nr = int(input("Welke taak verwijderen (nummer): "))
            except ValueError:
                print("Ongeldig nummer.")
                continue

            if not (1 <= nr <= len(zichtbaar)):
                print("Taaknummer bestaat niet.")
                continue

            taak = zichtbaar[nr - 1]
            taken.remove(taak)

            save_taken(taken)

            print("Taak verwijderd.")

        # -------------------------
        # Stoppen
        # -------------------------
        elif keuze == "0":
            print("Tot ziens!")
            break

        else:
            print("Ongeldige keuze.")


# -------------------------
# Startpunt
# -------------------------
if __name__ == "__main__":
    main()