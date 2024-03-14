import webbrowser
from flask import Flask

webbrowser.open("http://localhost:5000")

app = Flask(__name__)

@app.route('/')
def index():
    print("asasa")

if __name__ == '__main__':
    app.run(debug=True)