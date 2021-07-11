
# percobaan pertama pakai flask

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Assalammualaikum"

app.run(port=8000)