from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Cloud! Day la bai Lab 3 - Phan 1 cua toi.'