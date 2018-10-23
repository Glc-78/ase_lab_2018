from flask import Blueprint, jsonify, request

teams = Blueprint('teams', __name__)

__DEVS = ['Tarek','Bob']
__OPS = ['Bill']
__TEAMS = {1: __DEVS, 2: __OPS}

@teams.route('/teams')
def get_all():
    return jsonify(__TEAMS)

@teams.route('/teams/<int:team_id>')
def get_team(team_id):
    return jsonify(__TEAMS[team_id])


