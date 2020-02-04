#!flask/bin/python
from flask import Flask, make_response, jsonify, request
from endpoints import goatmen, goblin, ogre, orc, skeleton, troll

app = Flask(__name__)

@app.route('/api/v1.0/goblin', methods=['GET', 'POST'])
def get_goblin():
    return "Goblin!"

@app.route('/api/v1.0/goatmen', methods=['GET', 'POST'])
def get_goatmen():
    if request.method == 'POST':
        try:
            return goatmen.insert_name(str(request.form['firstName']).strip())
        except KeyError as error:
            return make_response(jsonify({'error' : 'Invalid key error.',
                'errorMessage' : 'Ensure body of the POST request only contains one dictionary value: firstName'}), 400)
        except Exception as error:
            return make_response(jsonify({'error' : 'Unhandled error.',
                'errorMessage' : 'Unknown error occured'}), 400)

    else:
        return goatmen.return_name()

@app.route('/api/v1.0/ogre', methods=['GET', 'POST'])
def get_ogre():
    return "Ogre!"

@app.route('/api/v1.0/orc', methods=['GET', 'POST'])
def get_orc():
    return "Orc!"

@app.route('/api/v1.0/skeleton', methods=['GET', 'POST'])
def get_skeleton():
    return "Skeleton!"

@app.route('/api/v1.0/troll', methods=['GET', 'POST'])
def get_troll():
    return "Troll!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



if __name__ == '__main__':
    app.run(debug=True)