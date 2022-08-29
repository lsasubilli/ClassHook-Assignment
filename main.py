from flask import Flask

app = Flask(__name__)

@app.route('/app')
def home():
    return "Hello Cosmos..."

if __name__ == '_main_':
    app.run(debug = True)


