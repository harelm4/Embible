
from flask import Flask, request,jsonify
from flask_cors import CORS
import webbrowser

from src.model import Model

app = Flask(__name__)
CORS(app)
# @app.route("/",methods=['GET'])
# def hello_world():
#     return render_template('index.html')

@app.route("/calc",methods=['GET'])
def calc():
    args = request.args.to_dict()
    text=args['text']
    m=Model()
    return jsonify(m.calc(text))

app.run(host="localhost", port=8000,debug=True,)
