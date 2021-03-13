from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/data')
def vaccine_data():
    return render_template('data.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
