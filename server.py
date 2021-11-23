import csv
from flask import Flask, render_template, request, redirect
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>.html')
def index_html(page_name=None):
    return render_template(f'{page_name}.html')


def write_to_file(data):
    with open('database.txt', 'a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f'\n{email},{subject},{message}')


def write_to_csv(data_dict):
    with open('database.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['email', 'subject', 'message'])
        writer.writerow(data_dict)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database.'
    return 'Something wrong happened. Try again! thanks.'
