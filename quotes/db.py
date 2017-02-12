import sqlite3

conn = sqlite3.connect('quotes/quotes.db')
c = conn.cursor()

def store(tweetContent, scores):
    c.execute('''INSERT INTO tweets(CONTENT) VALUES (?)''', (tweetContent,))
    tweetid = c.lastrowid
    for word, score in scores:
        c.execute('''INSERT INTO scores(TWEETID, WORD, SCORE) VALUES (?,?,?)''',
            (tweetid, word, score))

    conn.commit()

def scoreSearch(word, size=1):
    scores = c.execute('''SELECT * FROM scores WHERE WORD = ?''', (word,)).fetchall()

    if len(scores) == 0:
        return ['No quotes found!']

    sortedScores = sorted(scores, key=lambda x: x[3])

    quotes = []
    for i in range(size):
        quoteIndex = sortedScores[i][1]
        quote = c.execute('''SELECT * FROM tweets WHERE ID = ?''', (quoteIndex,)).fetchone()
        quotes.append(quote[1])
    return quotes



def BUILD():
    c.execute('''CREATE TABLE tweets (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CONTENT TEXT
    )''')

    c.execute('''CREATE TABLE scores (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TWEETID INT,
        WORD TEXT,
        SCORE INT
    )''')

    conn.commit()
