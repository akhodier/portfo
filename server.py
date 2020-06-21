import os
import csv
from flask import Flask, render_template, send_from_directory, url_for, request, redirect
app = Flask(__name__)
print(__name__)


@app.route('/<string:pagename>')
def html_page(pagename):

    return render_template(pagename)


@app.route('/')
def homepage():

    return render_template("index.html")


def write_to_database(data):
    with open("database.txt", mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def writetocsv(data):
    with open("database.csv", mode='a', newline='') as databasecsv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            databasecsv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_database(data)
        writetocsv(data)
        print(data)
        return redirect("/thankyou.html")
    else:
        return 'Something wrong'
    #    if valid_login(request.form['username'],
    #                   request.form['password']):
    #        return log_the_user_in(request.form['username'])
    #    else:
    #        error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid

   # return 'test submit'  # render_template('login.html', error=error)
