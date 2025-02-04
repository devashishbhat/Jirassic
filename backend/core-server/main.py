#Running server instance: python main.py

from flask import Flask, jsonify
from flask_cors import CORS
from services.database import db
from routes.user_routes import user_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"], "methods": ["GET", "POST", "OPTIONS"]}})

# Register User's Blueprint
app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"status": "Working fine"})

@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        collections = db.list_collection_names()
        return jsonify({"message": "Connected to MongoDB", "collections": collections})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
