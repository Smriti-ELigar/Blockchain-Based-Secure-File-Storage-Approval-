'''AIzaSyCBt1P_Hr9RK4-P6e872pjbUoXCObGlO6U'''
from flask import Flask, request, jsonify
import sqlite3
import openai  # Assuming Gemini API is compatible with OpenAI's API style

app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyCBt1P_Hr9RK4-P6e872pjbUoXCObGlO6U"
openai.api_key = GEMINI_API_KEY

# Function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect("file_logs.db")
    conn.row_factory = sqlite3.Row
    return conn

# Function to query file availability
def check_file_status(file_hash):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT file_name, uploader, status FROM files WHERE file_hash = ?", (file_hash,))
    file_data = cur.fetchone()
    conn.close()
    return file_data

# Function to query general table content except IPFS field
def get_file_metadata():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT file_name, uploader, status FROM files")
    files = cur.fetchall()
    conn.close()
    return [dict(file) for file in files]

# Gemini API interaction
def query_gemini(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Change if needed for Gemini model
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.json.get("message")
    
    if "check file" in user_input.lower():
        file_hash = user_input.split()[-1]  # Extract file hash from query
        file_status = check_file_status(file_hash)
        if file_status:
            return jsonify({"response": f"File '{file_status['file_name']}' uploaded by {file_status['uploader']} is {file_status['status']}."})
        else:
            return jsonify({"response": "File not found or access restricted."})
    
    elif "list files" in user_input.lower():
        files = get_file_metadata()
        return jsonify({"response": files})
    
    else:
        response = query_gemini(user_input)
        return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
