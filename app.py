from Flask import Flask

app = Flask(__name__)

@app.route(“/”)
Def index():
Return "Olá, <b>tudo bem</b>?"
