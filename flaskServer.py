#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='../')
# CORS(app)

pro14 = [
    {
        "id":"1",
        "name":"Leinster Rugby",
        "country":"Ireland",
        "conf":"A",
        "points":33
    },
    {
        "id":"2",
        "name":"Ulster Rugby",
        "country":"Ireland",
        "conf":"A",
        "points":25
    },
    {
        "id":"3",
        "name":"Toyota Cheetahs",
        "country":"South Africa",
        "conf":"A",
        "points":21
    },
    {
        "id":"4",
        "name":"Glasgow Warriors",
        "country":"Scotland",
        "conf":"A",
        "points":15
    },
    {
        "id":"5",
        "name":"Dragons",
        "country":"Wales",
        "conf":"A",
        "points":9
    },
    {
        "id":"6",
        "name":"Ospreys",
        "country":"Wales",
        "conf":"A",
        "points":7
    },
    {
        "id":"7",
        "name":"Zebre Rugby Club",
        "country":"Italy",
        "conf":"A",
        "points":7
    },
    {
        "id":"8",
        "name":"Munster Rugby",
        "country":"Ireland",
        "conf":"B",
        "points":25
    },
    {
        "id":"9",
        "name":"Connacht Rugby",
        "country":"Ireland",
        "conf":"B",
        "points":24
    },
    {
        "id":"10",
        "name":"Edinburgh Rugby",
        "country":"Scotland",
        "conf":"B",
        "points":23
    },
    {
        "id":"11",
        "name":"Scarlets",
        "country":"Wales",
        "conf":"B",
        "points":21
    },
    {
        "id":"12",
        "name":"Cardiff Blues",
        "country":"Wales",
        "conf":"B",
        "points":15
    },
    {
        "id":"13",
        "name":"Benetton Rugby",
        "country":"Italy",
        "conf":"B",
        "points":14
    },
    {
        "id":"14",
        "name":"Isuzu Southern Kings",
        "country":"South Africa",
        "conf":"B",
        "points":6
    }
]

nextID = 15

# ******* Comment Out or =Redirect Later *******
# where no team details specified after hostname
# @app.route('/')
# def get_home():
#     return "This server hosts the list of PRO14 Rugby teams"
# *** test *** 
# curl -i http://localhost:5000/

# ******* 1. Get All Records ********
# where name of league specified, return all teams in that league
@app.route('/pro14', methods=['GET'])
def getAll():
    return jsonify(pro14)
# *** test *** 
# curl -i http://localhost:5000/pro14

# ******* 2. Get One Record By ID ********
# where league name specified, followed by team id, display team details
@app.route('/pro14/<string:id>', methods =['GET'])
def getTeam(id):
    foundTeams = list(filter(lambda t : t['id'] == id, pro14))
    if len(foundTeams) == 0:
        return jsonify({}),204
    return jsonify(foundTeams[0])
# *** test ***
#curl -i http://localhost:5000/cars/test

# ******* 3. Add Record ********
# where we want to add a new team to the league
@app.route('/pro14', methods=['POST'])
def createTeam():
    global nextID
    if not request.json:
        abort(400)
    # check presence & formatting of other elements
    team={
        "id": str(nextID),
        "name": request.json['name'],
        "country": request.json['country'],
        "conf": request.json['conf'],
        "points": request.json['points']
    }
    nextID += 1
    pro14.append(team)
    return jsonify(team),201

# *** test (Mac) ***
# curl -i -H "Content-Type:application/json" -X POST -d '{"name":"NewTestTeam","country":"Antarctica","conf":"B","points":76}' 'http://127.0.0.1:5000/pro14'
# *** test (windows) ***
# curl -i -H "Content-Type:application/json" -X POST -d "{\"id\":\"15\",\"name\":\"New Test Team\",\"country\":\"Antarctica\",\"conf\":\"C\",\"points\":76}" http://localhost:5000/cars

# ******* 4. Update Record ********
# where we want to update an existing team
@app.route('/pro14/<string:id>', methods =['PUT'])
def updateTeam(id):
    foundTeams=list(filter(lambda t : t['id'] == id, pro14))
    if len(foundTeams) == 0:
        abort(404)
    foundTeam = foundTeams[0]
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'points' in reqJson and type(reqJson['points']) != int:
        abort(400)
    if 'name' in reqJson:
        foundTeam['name']  = reqJson['name']
    if 'country' in reqJson:
        foundTeam['country'] = reqJson['country']
    if 'conf' in reqJson:
        foundTeam['conf'] = reqJson['conf']  
    if 'points' in reqJson:
        foundTeam['points'] = reqJson['points']    
  
    return jsonify(foundTeam)
# *** test (Mac) ***
# curl -i -H "Content-Type:application/json" -X PUT -d '{"points":0}' http://localhost:5000/pro14/1
# *** test (windows) ***
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"points\":0}" http://localhost:5000/cars/pro14/1

# ******* 5. Delete Record ********
# where we want to delete an existing team
@app.route('/pro14/<string:id>', methods =['DELETE'])
def deleteTeam(id):
    foundTeams = list(filter (lambda t : t['id'] == id, pro14))
    if len(foundTeams) == 0:
        abort(404)
    pro14.remove(foundTeams[0])
    return  jsonify( { 'done':True })
# *** test *** 
# curl -i -X DELETE http://localhost:5000/pro14/15


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