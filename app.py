#!flask/bin/python
from flask import Flask, make_response, jsonify, request
from endpoints import goatmen, goblin, ogre, orc, skeleton, troll, users
from database import models

app = Flask(__name__)



@app.route('/api/v1.0/goblin', methods=['GET', 'POST'])
def get_goblin():
    return "Goblin!"

@app.route('/api/v1.0/goatmen', methods=['GET', 'POST'])
def get_goatmen():
    # POST request
    if request.method == 'POST':
        try:
            # First verify the API key and return the user
            currentUser = users.verify_user(request.headers.get("x-api-key"))
            # Create new record in DB
            return goatmen.insert_name(str(request.form['firstName']).strip(),currentUser)
        except KeyError as error:
            # This catches if invalid keys were provided in request
            return make_response(jsonify({'error' : 'Invalid key error.',
                'errorMessage' : 'Ensure firstName key/value is in body'}), 400)
        except ReferenceError:
            # This catches if our verify_users function can't find the x-api-key in the DB
            return make_response(jsonify({'error' : 'unauthorised.',
                'errorMessage' : 'unknown x-api-key provided'}), 400)
        except IndexError:
            # This catches if no API key was provided in the first place
            return make_response(jsonify({'error' : 'unauthorised.',
                'errorMessage' : 'no x-api-key provided'}), 400)
        except Exception as error:
            print(error)
            # This cathcs any other unhandled exceptions
            return make_response(jsonify({'error' : 'Unhandled error.',
                'errorMessage' : 'Unknown error occured'}), 400)


    else:
        # GET request
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