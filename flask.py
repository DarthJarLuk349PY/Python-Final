import flask 

app = flask(__name__)

@app.route('/')
def index():
    return "Hello World"
if __name__ == "__main___":
    app.run(debug=True)

    
