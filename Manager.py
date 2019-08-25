from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
@app.route('/Login')
def login():
    return 404
@app.route('/Register')
def register():
    return 404
if __name__ == '__main__':
    app.run(debug=True)