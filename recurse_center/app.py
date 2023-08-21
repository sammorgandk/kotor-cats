# Write a program that runs a server that is accessible on http://localhost:4000/. 
# When your server receives a request on http://localhost:4000/set?somekey=somevalue it should store the passed key and value in memory. 
# When it receives a request on http://localhost:4000/get?key=somekey it should return the value stored at somekey.

from flask import Flask, request

app = Flask(__name__)

# data stored in memory
key_value_pairs = {}

# route for set
@app.route('/set')
def set_key_value():
    key = request.args.get('key')
    value = request.args.get('value')
    if key and value:
        key_value_pairs[key] = value
        return f"Key '{key}' is set to '{value}'"
    else:
        return "Need to set key or value", 400

# route to get values for set keys
@app.route('/get')
def get_value():
    key = request.args.get('key')
    if key in key_value_pairs:
        return key_value_pairs[key]
    else:
        return f"Value for key '{key}' has not been set", 400

# server accessible on localhost port 4000
if __name__ == '__main__':
    app.run(host='localhost', port=4000)
