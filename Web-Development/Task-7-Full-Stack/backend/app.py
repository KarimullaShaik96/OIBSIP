from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
    conn.close()

    return jsonify([dict(task) for task in tasks])


@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Task title is required"}), 400

    conn = get_db_connection()

    cursor = conn.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )

    conn.commit()

    task_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "id": task_id,
        "title": title,
        "completed": 0
    }), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    completed = 1 if data.get("completed") else 0

    conn = get_db_connection()

    conn.execute(
        "UPDATE tasks SET completed = ? WHERE id = ?",
        (completed, task_id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Task updated successfully"})


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db_connection()

    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Task deleted successfully"})


if __name__ == "__main__":
    initialize_database()

    print("=" * 50)
    print("       OIBSIP FULL STACK TASK MANAGER")
    print("=" * 50)
    print("Server running at: http://127.0.0.1:5000")

    app.run(debug=True)