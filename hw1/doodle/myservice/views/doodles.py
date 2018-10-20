from flakon import JsonBlueprint
from flask import request, jsonify, abort
from myservice.classes.poll import Poll, NonExistingOptionException, UserAlreadyVotedException

doodles = JsonBlueprint('doodles', __name__)

_ACTIVEPOLLS = {} # list of created polls
_POLLNUMBER = 0 # index of the last created poll

@doodles.route('/doodles', methods=['GET','POST'])
def all_polls():

    if request.method == 'POST':
        result = create_doodle(request)

    elif request.method == 'GET':
        result = get_all_doodles(request)
    
    return result


@doodles.route('/doodles/<id>', methods=['GET','DELETE','PUT'])
def single_poll(id):

    global _ACTIVEPOLLS

    exist_poll(id)

    if request.method == 'GET':
        result = jsonify(_ACTIVEPOLLS[id].serialize())

    elif request.method == 'DELETE':
        result = jsonify(winners=_ACTIVEPOLLS[id].get_winners())
        del _ACTIVEPOLLS[id] 

    elif request.method == 'PUT':
        result = jsonify(winners=vote(id, request))   

    return result

@doodles.route('/doodles/<id>/<person>', methods=['GET','DELETE'])
def person_poll(id, person):
    
    exist_poll(id)

    if request.method == 'GET':
        votedoptions = _ACTIVEPOLLS[id].get_voted_options(person)
        result = jsonify({'votedoptions':votedoptions})

    if request.method == 'DELETE':
        removed = _ACTIVEPOLLS[id].delete_voted_options(person)
        result = jsonify({'removed': removed})

    return result
       

def vote(id, request):

    json_data = request.get_json()
    person = json_data['person']
    vote = json_data['option']

    try:
        result = _ACTIVEPOLLS[id].vote(person, vote)
        print(result)
    except UserAlreadyVotedException:
        abort(400)
    except NonExistingOptionException:
        abort(400)

    return result


def create_doodle(request):

    global _ACTIVEPOLLS, _POLLNUMBER

    json_data = request.get_json()
    title = json_data['title']
    options = json_data['options']
    _POLLNUMBER += 1
    _ACTIVEPOLLS[str(_POLLNUMBER)] = Poll(_POLLNUMBER, title, options)

    return jsonify({'pollnumber': _POLLNUMBER})


def get_all_doodles(request):
    global _ACTIVEPOLLS
    return jsonify(activepolls = [e.serialize() for e in _ACTIVEPOLLS.values()])

def exist_poll(id):
    if int(id) > _POLLNUMBER:
        abort(404) # error 404: Not Found, i.e. wrong URL, resource does not exist
    elif not(id in _ACTIVEPOLLS):
        abort(410) # error 410: Gone, i.e. it existed but it's not there anymore