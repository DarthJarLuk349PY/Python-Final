from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/output')
def output():
    return render_template('output.html')


if __name__ == "__main__":
    app.run(host= '127.0.0.1', port=5500, debug=True)

