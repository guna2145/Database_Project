from flask import Flask
app = Flask(__name__)

@app.route('/')
def geturl():
    return "Successfully Connected"

if __name__ == "__main__":
    app.run()