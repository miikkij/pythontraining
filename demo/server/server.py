from flask import Flask, request
app = Flask(__name__)

@app.route('/api/user/login', methods=['POST'])
def login():
    if request.json['password'] == 'pass':
        resp = app.response_class(status=200)
        resp.headers['session'] = 'abc'
        return resp
    else:
        return ('', 401)

@app.route('/api/user', methods=['GET'])
def user():
    if request.headers['session'] == 'abc':
        return ('', 200)
    else:
        return ('', 401)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)
