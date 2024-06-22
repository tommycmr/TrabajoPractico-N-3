from flask import Flask, render_template, request, redirect, url_for, flash, Response
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


app = Flask(__name__,static_url_path='/static')
load_dotenv()

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)


@app.route('/')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(port=3000, debug=True)