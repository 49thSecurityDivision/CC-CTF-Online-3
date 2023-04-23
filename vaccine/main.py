from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__)

def calculate_file_size(filepath):
    cmd = f"stat -c %s {filepath}"
    output = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    return output

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/filesize', methods=['POST'])
def get_file_size():
    filepath = request.form.get('filepath')
    if filepath:
        try:
            output = calculate_file_size(filepath)
        except subprocess.CalledProcessError as e:
            output = e.output
    else:
        output = "Error: No file path provided."
    return render_template('result.html', output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8091)
