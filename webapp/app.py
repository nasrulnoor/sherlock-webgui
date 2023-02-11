from flask import Flask, render_template, request
import subprocess
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        sherlock_output = subprocess.run(['sherlock', username], stdout=subprocess.PIPE).stdout.decode('utf-8')
        return render_template('index.html', sherlock_output=sherlock_output)
    return render_template('index.html')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
