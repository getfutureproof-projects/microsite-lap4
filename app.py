from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'This is futureproof'

@app.route('/skills', methods=['GET'])
def skills():
    if request.method == 'GET':
        return jsonify({'Skills you should have now': ['HTML', 'CSS', 'JS', 'DBs', 'React']})

@app.route('/future')
def future():
    if request.method == 'GET':
        return jsonify({'After the Python week I will know': ['Python', 'Flask', 'Django', 'Data Science', 'Know how to appreciate Python properly']})


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Opps...{err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_server_error(err):
    return jsonify({"message": f"{err}. It's not you, it's us. Press F to pay respects"}), 500

if __name__ == '__main__':
    app.run(debug=True)
