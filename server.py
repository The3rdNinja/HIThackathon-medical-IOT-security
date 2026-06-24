from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins to access this Flask app

# Load the database from the text file
def load_database():
    db = {}
    try:
        with open("db.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    userid, percentage = line.split(":")
                    db[userid] = int(percentage)
    except FileNotFoundError:
        with open("db.txt", "w"):
            pass
    return db

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_user():
    userid = request.form.get("username")
    if not userid:
        return jsonify({"error": "User ID is required"}), 400

    db = load_database()
    if userid in db:
        percentage = db[userid]
        return jsonify({"userid": userid, "percentage": percentage})
    else:
        return jsonify({"error": "User ID not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
