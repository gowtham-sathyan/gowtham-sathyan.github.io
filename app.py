from flask import Flask,send_file
from flask_cors import CORS, cross_origin
app=Flask(__name__)
cors=CORS(app)

@app.route('/')
@cross_origin()
def main():
    return send_file('index.html')
if __name__ == '__main__':
    app.run(debug=True)