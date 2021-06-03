from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.getlist('someSwitchOption001')
        with open('submit.json', 'w') as outfile:
            json.dump(data, outfile)
        return 'Thank you for submitting!'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
