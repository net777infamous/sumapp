from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Warning: Adult content, you mustbe at least 18 years old to use this server"

if __name__ == '__main__':
    app.run()