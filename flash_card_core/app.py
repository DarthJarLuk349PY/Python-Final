from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__, template_folder='templates')
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

#REDEIRCT TO NEXT FILES 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/output')
def output():
    return render_template('output.html')


config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

@app.route('/')
@cache.cached(timeout=50)
def index():
    return 'Cached for 50s'


def make_key():
   """A function which is called to derive the key for a computed value.
      The key in this case is the concat value of all the json request
      parameters. Other strategy could to use any hashing function.
   :returns: unique string for which the value should be cached.
   """
   user_data = request.get_json()
   return ",".join([f"{key}={value}" for key, value in user_data.items()])

@app.route("/hello", methods=["POST"])
@cache.cached(timeout=60, make_cache_key=make_key)
def some_func():
   ...

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5500, debug=True)
