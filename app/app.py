from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/ping')
def pong():
    return jsonify({"answer": "pong"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
