from flask import Flask, request, redirect, session, render_template_string
import json
import hashlib
from pathlib import Path

app = Flask(**name**)
app.secret_key = "supersecretkey"

USERS_FILE = "users.json"
TAKEN_FILE = "taken.json"

def hash_password(password):
return hashlib.sha256(password.encode()).hexdigest()

def check_password(password, password_hash):
return hash_password(password) == password_hash

def ensure_users():
if Path(USERS_FILE).exists():
return

users = [
    {
        "username": "admin",
        "password": hash_password("admin123"),
        "role": "admin"
    },
    {
        "username": "user",
        "password": hash_password("user123"),
        "role": "user"
    }
]

Path(USERS_FILE).write_text(
    json.dumps(users, indent=2),
    encoding="utf-8"
)


def load_users():
return json.loads(Path(USERS_FILE).read_text(encoding="utf-8"))

def load_taken():
if not Path(TAKEN_FILE).exists():
return []


return json.loads(Path(TAKEN_FILE).read_text(encoding="utf-8"))


def save_taken(taken):
Path(TAKEN_FILE).write_text(
json.dumps(taken, indent=2),
encoding="utf-8"
)

LOGIN_HTML = """

<h1>Login</h1>

<form method="post">
    <input name="username" placeholder="Username"><br><br>
    <input type="password" name="password" placeholder="Password"><br><br>
    <button type="submit">Login</button>
</form>

<p style="color:red">{{ error }}</p>
"""

INDEX_HTML = """

<h1>Welkom {{ user }}</h1>

<p>Rol: {{ role }}</p>

<a href="/logout">Logout</a>

<hr>

<form method="post" action="/add">
    <input name="titel" placeholder="Nieuwe taak">
    <button type="submit">Toevoegen</button>
</form>

<hr>

<ul>
{% for t in taken %}
<li>
    {{ "groen" if t["klaar"] else "qit" }}
    {{ t["titel"] }}
    ({{ t["owner"] }})


{% if not t["klaar"] %}
    <a href="/done/{{ loop.index0 }}">Klaar</a>
{% endif %}

{% if role == "admin" %}
    <a href="/delete/{{ loop.index0 }}">Verwijder</a>
{% endif %}
```

</li>
{% endfor %}
</ul>
"""

@app.route("/login", methods=["GET", "POST"])
def login():
users = load_users()

```
if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]

    for user in users:
        if (
            user["username"] == username
            and check_password(password, user["password"])
        ):
            session["user"] = user["username"]
            session["role"] = user["role"]
            return redirect("/")

    return render_template_string(
        LOGIN_HTML,
        error="Foute login"
    )

return render_template_string(
    LOGIN_HTML,
    error=""
)


@app.route("/")
def index():
if "user" not in session:
return redirect("/login")


taken = load_taken()

if session["role"] != "admin":
    taken = [
        t for t in taken
        if t["owner"] == session["user"]
    ]

return render_template_string(
    INDEX_HTML,
    taken=taken,
    user=session["user"],
    role=session["role"]
)


@app.post("/add")
def add():
if "user" not in session:
return redirect("/login")

```
titel = request.form["titel"].strip()

if titel:
    taken = load_taken()

    taken.append({
        "titel": titel,
        "klaar": False,
        "owner": session["user"]
    })

    save_taken(taken)

return redirect("/")


@app.get("/done/[int:i](int:i)")
def done(i):
if "user" not in session:
return redirect("/login")


taken = load_taken()

if i < len(taken):
    taken[i]["klaar"] = True
    save_taken(taken)

return redirect("/")


@app.get("/delete/[int:i](int:i)")
def delete(i):
if "user" not in session:
return redirect("/login")


if session["role"] != "admin":
    return redirect("/")

taken = load_taken()

if i < len(taken):
    taken.pop(i)
    save_taken(taken)

return redirect("/")


@app.get("/logout")
def logout():
session.clear()
return redirect("/login")

if **name** == "**main**":
ensure_users()
app.run(debug=True)
