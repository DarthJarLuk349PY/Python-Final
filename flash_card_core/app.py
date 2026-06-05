from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__, template_folder='templates')
config{
    "DEBUG": True,
    "CACH_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT":300
}
app.config.from_mapping(config)
cahce = Cache(app)
#REDEIRCT TO NEXT FILES 

sudy_data = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/output')
def output():
    return render_template('output.html')


@app.route('/api/save-study', METHODS=['POST'])
@cache.cached(timeout=50)
def save_study():
    global save_study
    data = request.get_json()
    terms = data.get('terms', [])
    definitions = data.get('definitions', [])
    if len(terms) != len(definitions) or len(terms) == 0:
        return jsonify({"status": "error", "message":"Mismatch/empty data"}), 400
    study_data = dict(zip(terms, deffitions))



if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5500, debug=True)
