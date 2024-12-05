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
    return render_template('results.html', test_string=test_string, regex=regex, matches=matches)

@app.route('/validate-email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        is_valid = re.match(email_regex, email) is not None
        return render_template('validate_email.html', email=email, is_valid=is_valid)
    return render_template('validate_email.html', email=None, is_valid=None)

if __name__ == '__main__':
    app.run(debug=True)
