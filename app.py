#!flask/bin/python
from flask import Flask, make_response, jsonify, request
from endpoints import goatmen, goblin, ogre, orc, skeleton, troll, users
from database import models

app = Flask(__name__)



@app.route('/api/v1.0/goblin', methods=['GET'])
def get_goblin():
    return goblin.return_name()

@app.route('/api/v1.0/goblin/firstName', methods=['POST'])
def post_goblin_first_name():
    try:
        # First verify the API key and return the user
        currentUser = users.verify_user(request.headers.get("x-api-key"))
        # Create new record in DB
        return goblin.insert_first_name(str(request.form['firstName']).strip(),currentUser)
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
        # This catches any other unhandled exceptions
        return make_response(jsonify({'error' : 'Unhandled error.',
        'errorMessage' : 'Unknown error occured'}), 400)

@app.route('/api/v1.0/goblin/lastName', methods=['POST'])
def post_goblin_last_name():
    try:
        # First verify the API key and return the user
        currentUser = users.verify_user(request.headers.get("x-api-key"))
        # Create new record in DB
        return goblin.insert_last_name(str(request.form['lastName']).strip(),currentUser)
    except KeyError as error:
        # This catches if invalid keys were provided in request
        return make_response(jsonify({'error' : 'Invalid key error.',
        'errorMessage' : 'Ensure lastName key/value is in body'}), 400)
    except ReferenceError:
        # This catches if our verify_users function can't find the x-api-key in the DB
        return make_response(jsonify({'error' : 'unauthorised.',
        'errorMessage' : 'unknown x-api-key provided'}), 400)
    except IndexError:
        # This catches if no API key was provided in the first place
        return make_response(jsonify({'error' : 'unauthorised.',
        'errorMessage' : 'no x-api-key provided'}), 400)
    except Exception as error:
        # This catches any other unhandled exceptions
        return make_response(jsonify({'error' : 'Unhandled error.',
        'errorMessage' : 'Unknown error occured'}), 400)

@app.route('/api/v1.0/goatmen', methods=['GET'])
def get_goatmen():
    # GET request
    return goatmen.return_name()

@app.route('/api/v1.0/goatmen/firstName', methods=['POST'])
def post_goatmen_firstName():
    try:
        # First verify the API key and return the user
        currentUser = users.verify_user(request.headers.get("x-api-key"))
        # Create new record in DB
        return goatmen.insert_first_name(str(request.form['firstName']).strip(),currentUser)
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
        # This catches any other unhandled exceptions
        return make_response(jsonify({'error' : 'Unhandled error.',
        'errorMessage' : 'Unknown error occured'}), 400)

@app.route('/api/v1.0/ogre', methods=['GET'])
def get_ogre():
    return ogre.return_name()

@app.route('/api/v1.0/ogre/firstName', methods=['POST'])
def post_ogre_first_name():
    try:
        # First verify the API key and return the user
        currentUser = users.verify_user(request.headers.get("x-api-key"))
        # Create new record in DB
        return ogre.insert_first_name(str(request.form['firstName']).strip(),currentUser)
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
        # This catches any other unhandled exceptions
        return make_response(jsonify({'error' : 'Unhandled error.',
        'errorMessage' : 'Unknown error occured'}), 400)


@app.route('/api/v1.0/orc', methods=['GET'])
def get_orc():
    return orc.return_name()

@app.route('/api/v1.0/orc/firstName', methods=['POST'])
def post_orc_first_name():
    try:
        # First verify the API key and return the user
        currentUser = users.verify_user(request.headers.get("x-api-key"))
        # Create new record in DB
        return orc.insert_first_name(str(request.form['firstName']).strip(),currentUser)
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
        # This catches any other unhandled exceptions
        return make_response(jsonify({'error' : 'Unhandled error.',
        'errorMessage' : 'Unknown error occured'}), 400)

@app.route('/api/v1.0/orc/lastName', methods=['POST'])
def post_orc_last_name():
    try:
        # First verify the API key and return the user
        currentUser = users.verify_user(request.headers.get("x-api-key"))
        # Create new record in DB
        return orc.insert_last_name(str(request.form['lastName']).strip(),currentUser)
    except KeyError as error:
        # This catches if invalid keys were provided in request
        return make_response(jsonify({'error' : 'Invalid key error.',
        'errorMessage' : 'Ensure lastName key/value is in body'}), 400)
    except ReferenceError:
        # This catches if our verify_users function can't find the x-api-key in the DB
        return make_response(jsonify({'error' : 'unauthorised.',
        'errorMessage' : 'unknown x-api-key provided'}), 400)
    except IndexError:
        # This catches if no API key was provided in the first place
        return make_response(jsonify({'error' : 'unauthorised.',
        'errorMessage' : 'no x-api-key provided'}), 400)
    except Exception as error:
        # This catches any other unhandled exceptions
        return make_response(jsonify({'error' : 'Unhandled error.',
        'errorMessage' : 'Unknown error occured'}), 400)


@app.route('/api/v1.0/skeleton', methods=['GET'])
def get_skeleton():
    return skeleton.return_name()

@app.route('/api/v1.0/skeleton/firstName', methods=['POST'])
def post_skeleton_first_name():
    try:
        # First verify the API key and return the user
        currentUser = users.verify_user(request.headers.get("x-api-key"))
        # Create new record in DB
        return skeleton.insert_first_name(str(request.form['firstName']).strip(),currentUser)
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
        # This catches any other unhandled exceptions
        return make_response(jsonify({'error' : 'Unhandled error.',
        'errorMessage' : 'Unknown error occured'}), 400)

@app.route('/api/v1.0/skeleton/lastName', methods=['POST'])
def post_skeleton_last_name():
    try:
        # First verify the API key and return the user
        currentUser = users.verify_user(request.headers.get("x-api-key"))
        # Create new record in DB
        return skeleton.insert_last_name(str(request.form['lastName']).strip(),currentUser)
    except KeyError as error:
        # This catches if invalid keys were provided in request
        return make_response(jsonify({'error' : 'Invalid key error.',
        'errorMessage' : 'Ensure lastName key/value is in body'}), 400)
    except ReferenceError:
        # This catches if our verify_users function can't find the x-api-key in the DB
        return make_response(jsonify({'error' : 'unauthorised.',
        'errorMessage' : 'unknown x-api-key provided'}), 400)
    except IndexError:
        # This catches if no API key was provided in the first place
        return make_response(jsonify({'error' : 'unauthorised.',
        'errorMessage' : 'no x-api-key provided'}), 400)
    except Exception as error:
        # This catches any other unhandled exceptions
        return make_response(jsonify({'error' : 'Unhandled error.',
        'errorMessage' : 'Unknown error occured'}), 400)


@app.route('/api/v1.0/troll', methods=['GET'])
def get_troll():
    return troll.return_name()

@app.route('/api/v1.0/troll/firstName', methods=['POST'])
def post_troll_first_name():
    try:
        # First verify the API key and return the user
        currentUser = users.verify_user(request.headers.get("x-api-key"))
        # Create new record in DB
        return troll.insert_first_name(str(request.form['firstName']).strip(),currentUser)
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
        # This catches any other unhandled exceptions
        return make_response(jsonify({'error' : 'Unhandled error.',
        'errorMessage' : 'Unknown error occured'}), 400)

@app.route('/api/v1.0/troll/lastName', methods=['POST'])
def post_troll_last_name():
    try:
        # First verify the API key and return the user
        currentUser = users.verify_user(request.headers.get("x-api-key"))
        # Create new record in DB
        return troll.insert_last_name(str(request.form['lastName']).strip(),currentUser)
    except KeyError as error:
        # This catches if invalid keys were provided in request
        return make_response(jsonify({'error' : 'Invalid key error.',
        'errorMessage' : 'Ensure lastName key/value is in body'}), 400)
    except ReferenceError:
        # This catches if our verify_users function can't find the x-api-key in the DB
        return make_response(jsonify({'error' : 'unauthorised.',
        'errorMessage' : 'unknown x-api-key provided'}), 400)
    except IndexError:
        # This catches if no API key was provided in the first place
        return make_response(jsonify({'error' : 'unauthorised.',
        'errorMessage' : 'no x-api-key provided'}), 400)
    except Exception as error:
        # This catches any other unhandled exceptions
        return make_response(jsonify({'error' : 'Unhandled error.',
        'errorMessage' : 'Unknown error occured'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



if __name__ == '__main__':
    app.run(debug=True)