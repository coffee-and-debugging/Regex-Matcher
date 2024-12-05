from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex = request.form['regex']

    try:
        matches = re.findall(regex, test_string)
    except re.error as e:
        matches = [f"Regex Error: {e}"]

    return render_template('results.html', matches=matches, test_string=test_string, regex=regex)

if __name__ == '__main__':
    app.run(debug=True)
