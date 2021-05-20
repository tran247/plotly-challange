#flask 

from flask import Flask, jsonify, render_template
#import pyscopg2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
# def home():
#     return jsonify(jsondata)

if __name__ =="__main__":
    app.run(debug=True)