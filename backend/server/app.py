from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from database.db_manager import DatabaseManager
from session.auth import SessionManager

# Loading in environment file
load_dotenv()

# Initializing flask app
app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


# Setting up CORS
CORS(app)

# Instantiating components
database_manager = DatabaseManager(
    sql_host=os.getenv('SQL_HOST'),
    sql_uname=os.getenv('SQL_USER'),
    sql_pw=os.getenv('SQL_PASSWD'),
    sql_db=os.getenv('SQL_DB'),
    mongo_host=os.getenv('MONGO_HOST'),
    mongo_uname=os.getenv('MONGO_USER'),
    mongo_pw=os.getenv('MONGO_PASSWD'),
)

session_manager = SessionManager(
    secret_key=os.getenv('SECRET_KEY'),
)

# -------------- Server Routes
@app.route('/', methods=['GET'])
def root():
    '''
        Root url, to test whether the server is running
    '''
    return jsonify({"msg": "Hello There"})

# --- Authentication Routes
@app.route('/login', methods=['POST'])
def login():
    email = request.get_json()['email']
    password = request.get_json()['password']

    if email == '' or password == '' or not isinstance(email, str) or not isinstance(password, str):
        return jsonify({'error': 'Invalid email or password'}), 400

    return session_manager.login(email, password, database_manager)

@app.route('/signup', methods=['POST'])
def signup():
    return jsonify({'error': 'Feature not available'}), 500

# --- Profile Management Routes
@app.route('/profile/get', methods=['POST'])
@session_manager.validateJWT
def getAccInfo():
    return jsonify({'error': 'Feature not available'}), 500

@app.route('/profile/change', methods=['POST'])
@session_manager.validateJWT
def changeAccInfo():
    return jsonify({'error': 'Feature not available'}), 500

@app.route('/profile/addperson', methods=['POST'])
@session_manager.validateJWT
def addPersonToAcc():
    return jsonify({'error': 'Feature not available'}), 500

# --- Policy Management Routes
@app.route('/profile/policy/get', methods=['POST'])
@session_manager.validateJWT
def getPolInfo():
    return jsonify({'error': 'Feature not available'}), 500

@app.route('/profile/policy/cancel', methods=['POST'])
@session_manager.validateJWT
def cancelPol():
    return jsonify({'error': 'Feature not available'}), 500

@app.route('/profile/policy/renew', methods=['POST'])
@session_manager.validateJWT
def renewPol():
    return jsonify({'error': 'Feature not available'}), 500

# --- Policy Purchase Routes
@app.route('/shop', methods=['GET'])
def shopPol():
    return jsonify({'error': 'Feature not available'}), 500

@app.route('/shop', methods=['POST'])
@session_manager.validateJWT
def buyPol():
    return jsonify({'error': 'Feature not available'}), 500

# --- Policy Claim Routes
@app.route('/claim', methods=['POST'])
@session_manager.validateJWT
def claimPol():
    return jsonify({'error': 'Feature not available'}), 500

@app.route('/claim/track', methods=['POST'])
@session_manager.validateJWT
def trackClaim():
    return jsonify({'error': 'Feature not available'}), 500

if __name__ == '__main__':
    app.run(debug=True)
