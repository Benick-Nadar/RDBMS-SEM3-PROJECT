import os

import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/customers")
def customers():
    connection = mysql.connector.connect(
        host="localhost",
        user=os.getenv("DB_USER", "root"),
        password=os.environ["DB_PASSWORD"],
        database="rdbms_project_sem3",
    )

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT cid, cname, cadd, cmobile, cgen, cdob, cage
            FROM customer
            ORDER BY cid
        """)
        customer_rows = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    return render_template("customers.html", customers=customer_rows)

if __name__ == "__main__":
    app.run(debug=True)