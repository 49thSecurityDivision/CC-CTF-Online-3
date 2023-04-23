#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for, abort, Response
from werkzeug.utils import secure_filename
import os, subprocess, hashlib

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():
    response = "<p>"
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        path = os.path.join(app.config['UPLOAD_PATH'], filename)
        uploaded_file.save(path)
        os.popen(f'chmod +x {path}')

        with open("./MD5", "r") as file:
            chksum = file.read()
        theirsum = hashlib.md5(open(path, 'rb').read()).hexdigest()

        if (chksum == theirsum):
            response += "This program is approved!<br>"
            response += "Executing now!<br>"
            proc = subprocess.Popen([path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            result = proc.stdout.read()
            result = result.decode('utf-8')
            response += "<br><br>---------------------------<br>"
            response += "EXECUTION RESULT:<br>"
            response += "---------------------------<br>"
            response += result

            response += "</p>"
            return response, {'Content-Type': 'text/html'}

        if (chksum == ""):
            response += "Looks like there isn't a checksum recorded yet!<br>"
            response += "Let's test the program!<br>"
        elif (chksum != theirsum):
            response += "The uploaded program doesn't match the stored MD5!<br>"
            response += "Testing the uploaded file...<br>"

        proc = subprocess.Popen(['firejail', '--net=none', path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        result = proc.stdout.read()
        result = result.decode('utf-8')
        with open("./output.txt", "r") as file:
            expected_result = file.read()

        if (result != expected_result):
            response += "The program's output does not match the expected result!<br>"

            response += "</p>"
            return response, {'Content-Type': 'text/html'}
        else:
            response += "Wow! The program works as expected!<br>"
            response += "Storing its MD5 hash so this program can always be run on upload!<br>"

            with open("./MD5", "w") as file:
                file.write(theirsum)

            response += "<br><br>---------------------------<br>"
            response += "EXECUTION RESULT:<br>"
            response += "---------------------------<br>"
            response += "flag.txt<br>"

            response += "</p>"
            return response, {'Content-Type': 'text/html'}

    return redirect(url_for('index'))
