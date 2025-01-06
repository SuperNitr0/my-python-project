from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask"

@app.route("/db")
def db_test():
    try:
        conn = psycopg2.connect(
            dbname="mydb",
            user="myuser",
            password="mypassword",
            host="db",
            port="5432"
        )
        return "Database connected successfully!"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
