#!flask/bin/python
from flask import Flask, make_response, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/goblin')
def get_goblin():
    return "Goblin!"

@app.route('/api/v1.0/goatmen')
def get_goatmen():
    return "Goatmen!"

@app.route('/api/v1.0/ogre')
def get_ogre():
    return "Ogre!"

@app.route('/api/v1.0/orc')
def get_orc():
    return "Orc!"

@app.route('/api/v1.0/skeleton')
def get_skeleton():
    return "Skeleton!"

@app.route('/api/v1.0/troll')
def get_troll():
    return "Troll!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



if __name__ == '__main__':
    app.run(debug=True)