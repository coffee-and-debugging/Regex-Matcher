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
    result = None
    if request.method == 'POST':
        email = request.form.get('email', '')
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(email_regex, email):
            result = f"'{email}' is a valid email address."
        else:
            result = f"'{email}' is not a valid email address."
    return render_template('validate_email.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
