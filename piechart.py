import sqlite3 as lite
import matplotlib.pyplot as plt

# Connect to the database
con = lite.connect("Database.db")
cur = con.cursor()

# Retrieve the score and attempts for a specific user
username = "s"
score_sql = "SELECT score FROM clients WHERE username=?"
attempts_sql = "SELECT attempts FROM clients WHERE username=?"
cur.execute(score_sql, (username,))
score = cur.fetchone()[0]
cur.execute(attempts_sql, (username,))
attempts = cur.fetchone()[0]

# Make a pie chart of score and attempts-score
labels = ['Score', 'Attempts-Score']
sizes = [score, attempts-score]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
