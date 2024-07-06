from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/api/test',methods=['GET'])
def hello_world():
    var_1 = request.args.get('a')
    var_2= request.args.get('b')
    return f"{a} - {b}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')