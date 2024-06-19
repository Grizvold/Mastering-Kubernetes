from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to dummy-app!"

@app.route('/api', methods=['GET'])
def api():
    response = {
        'message': 'This is a response from dummy-app API!'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
