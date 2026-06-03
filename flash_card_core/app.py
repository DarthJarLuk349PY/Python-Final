from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return "<h1>Hello World!<h1>"

@app.route('/ask')
def ask():
    return render_template('index.html')

@app.route('/flash')
def flash():
    return render_template('flash.html')


if __name__ == "__main__":
    app.run(host= '127.0.0.1', port=5500, debug=True)

