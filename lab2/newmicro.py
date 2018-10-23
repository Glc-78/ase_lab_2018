###### lab 2 ######

from flask import Flask, jsonify, request, json
app = Flask(__name__)

USERS = {'1':'Joe','2':'Wilma','3':'Noel'}

@app.route('/api', methods=['GET'])
def function_1():
    print(request)
    response = jsonify({'Hello':'World'})
    print(response)
    print(response.data)
    #return jsonify({'Hello':'World'})
    return response

@app.route('/api', methods=['DELETE'])
def function_2():
    print(request)
    response = jsonify({'This is a DELETE':'response'})
    print(response)
    return response

@app.route('/api/<string:user_id>')
def function_3(user_id):
    print(request)
    response = jsonify({'Hello': USERS[user_id]})
    #response = json.dumps({'Hello': USERS[user_id]})
    return response

if __name__ == '__main__':
    print(app.url_map)
    app.run()