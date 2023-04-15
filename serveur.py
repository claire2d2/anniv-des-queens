from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    queen = request.form['queen']
    partner = request.form.get('partner',0)
    comments = request.form['commentaires']

    # Save data to SQLite3 database
    with sqlite3.connect('/home/claireyuan_song/data.db') as conn:
        cursor = conn.cursor()

        # Define the SQL command to create the table
        create_table_sql = """
        CREATE TABLE rsvp (
            name TEXT NOT NULL PRIMARY KEY,
            queen TEXT,
        partner INTEGER,
        comments TEXT
        )
        """

        # Execute the SQL command to create the table
        try:
            cursor.execute(create_table_sql)
        except:
            print("table already exists. skipping creation...")

        # Commit the changes to the database
        conn.commit()

        cursor.execute('INSERT INTO rsvp (name, queen, partner, comments) VALUES (?, ?, ?, ?)', (name, queen, partner, comments))
        conn.commit()

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=False)
