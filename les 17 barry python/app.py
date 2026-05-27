from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# =========================
# Taak class
# =========================
class Taak:
    def __init__(self, taak_id, titel):
        self.id = taak_id
        self.titel = titel
        self.klaar = False


# =========================
# Takenlijst class
# =========================
class Takenlijst:
    def __init__(self):
        self.taken = []
        self.next_id = 1

    def add(self, titel):
        taak = Taak(self.next_id, titel)

        self.taken.append(taak)

        self.next_id += 1

    def done(self, taak_id):
        for taak in self.taken:
            if taak.id == taak_id:
                taak.klaar = True

    def delete(self, taak_id):
        self.taken = [
            taak for taak in self.taken
            if taak.id != taak_id
        ]


# Takenlijst maken
lijst = Takenlijst()


# =========================
# Homepage
# =========================
@app.get("/")
def index():
    return render_template(
        "index.html",
        taken=lijst.taken
    )


# =========================
# Toevoegen
# =========================
@app.post("/add")
def add():
    titel = request.form.get("titel", "").strip()

    if titel != "":
        lijst.add(titel)

    return redirect(url_for("index"))


# =========================
# Klaar markeren
# =========================
@app.get("/done/<int:taak_id>")
def done(taak_id):
    lijst.done(taak_id)

    return redirect(url_for("index"))


# =========================
# Verwijderen
# =========================
@app.get("/delete/<int:taak_id>")
def delete(taak_id):
    lijst.delete(taak_id)

    return redirect(url_for("index"))


# =========================
# Startpunt
# =========================
if __name__ == "__main__":
    app.run(debug=True)