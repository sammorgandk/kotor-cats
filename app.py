from flask import Flask, request

app = Flask(__name__)

@app.route('/home')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='localhost',port=5000)
