#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response
from flask_cors import CORS
from rugbyDAO import rugbyDAO

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

# ******* 1. Get All Records ********
@app.route('/teams', methods=['GET'])
def getAllTeams():
    results = rugbyDAO.getAllTeams()
    return jsonify(results)
# *** test *** 
# curl -i http://localhost:5000/teams

# ******* 2. Get One Record By ID ********
# where team id specified, display team details
@app.route('/teams/<string:id>', methods =['GET'])
def getTeam(id):
    foundTeam = rugbyDAO.findTeamByID(id)
    
    return jsonify(foundTeam)
# *** test ***
# curl -i http://localhost:5000/pro14/1

# ******* 3. Add Record ********
# where we want to add a new team to the league
@app.route('/teams', methods=['POST'])
def createTeam():
    if not request.json:
        abort(400)
    # check presence & formatting of other elements
    team={
        "name": request.json['name'],
        "conf": request.json['conf'],
        "country": request.json['country'],
        "points": request.json['points']
    }
    
    values = (team['name'], team['conf'], team['country'], team['points'])
    newID = rugbyDAO.createTeam(values)
    
    team['id'] = newID

    return jsonify(team)

# *** test (Mac) ***
# curl -i -H "Content-Type:application/json" -X POST -d '{"name":"NewTestTeam2","country":"Antarctica","conf":"B","points":76}' 'http://127.0.0.1:5000/teams'
# *** test (windows) ***
# curl -i -H "Content-Type:application/json" -X POST -d "{\"id\":\"15\",\"name\":\"New Test Team\",\"country\":\"Antarctica\",\"conf\":\"C\",\"points\":76}" http://localhost:5000/cars

# ******* 4. Update Record ********
# where we want to update an existing team
@app.route('/teams/<string:id>', methods =['PUT'])
def updateTeam(id):
    foundTeam = rugbyDAO.findTeamByID(id)
    
    if not foundTeam:
        abort(404)
    if not request.json:
        abort(400)
   
    reqJson = request.json
    if 'points' in reqJson and type(reqJson['points']) != int:
        abort(400)

    if 'name' in reqJson:
        foundTeam['name']  = reqJson['name']
    if 'conf' in reqJson:
        foundTeam['conf'] = reqJson['conf']  
    if 'country' in reqJson:
        foundTeam['country'] = reqJson['country']
    if 'points' in reqJson:
        foundTeam['points'] = reqJson['points']    

    values = (foundTeam['name'], foundTeam['conf'], foundTeam['country'], foundTeam['points'], foundTeam['id'])
    rugbyDAO.updateTeam(values)
    return jsonify(foundTeam)
# *** test (Mac) ***
# curl -i -H "Content-Type:application/json" -X PUT -d '{"points":0}' http://localhost:5000/pro14/1
# *** test (windows) ***
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"points\":0}" http://localhost:5000/cars/pro14/1

# ******* 5. Delete Record ********
# where we want to delete an existing team
@app.route('/teams/<string:id>', methods =['DELETE'])
def deleteTeam(id):
    rugbyDAO.deleteTeam(id)
    return  jsonify( { 'Team Deleted':True })
# *** test *** 
# curl -i -X DELETE http://localhost:5000/teams/1


# ************************************
# for Production only
# @app.errorhandler(404)
# def not_found404(error):
#     return make_response( jsonify( {'error':'Not found' }), 404)

# @app.errorhandler(400)
# def not_found400(error):
#     return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)