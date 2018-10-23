from flask import Flask, jsonify
from werkzeug.routing import BaseConverter, ValidationError

USERS = {'1':'Joe','2':'Wilma','3':'Noel'}
# this creates as mutch pair 'val:id' as the items of USERS are
IDS = {val: id for id, val in USERS.items()}

class RegisteredUser(BaseConverter):

    def to_python(self, value):
        if value in USERS:
            return USERS[value]
        else:
            raise ValidationError()
    
    def to_url(self, value):
        return IDS[value]

app = Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser

@app.route('/api/person/<registered:name>')
def person(name):
    response = jsonify({'Hello':name})
    return response

if __name__ == '__main__':
    print(app.url_map)
    app.run()

