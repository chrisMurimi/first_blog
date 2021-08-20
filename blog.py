from flask import Flask, render_template, url_for, request
import sqlite3

db_local = 'users.db'


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    blog_data = queryFromDb()
    return render_template('home.html', title='home', blog_data=blog_data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/review')
def review():
    return render_template('review.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/addblog', methods =['POST', 'GET'])
def addblog():
    if request.method == 'POST':
        title = request.form['title'],
        content = request.form['content']
        my_db = sqlite3.connect(db_local)
        my_cursor = my_db.cursor()
        sql_tag = "INSERT INTO users (title,content) VALUES(?,?)"
        my_cursor.execute(sql_tag, (str(title), content))
        my_db.commit()
        return render_template('success.html')
    return render_template('addblog.html')


def queryFromDb():
    my_db = sqlite3.connect(db_local)
    my_cursor = my_db.cursor()
    my_cursor.execute('''
                      SELECT * FROM users''')

    blog_data = my_cursor.fetchall()
    return blog_data


if __name__ == '__main__':
    app.run(debug=True)
