#!flask/bin/python
from flask import Flask, make_response, jsonify, request, render_template
from endpoints.monster_endpoints import GoblinEndpoint, GoatmenEndpoint, OgreEndpoint, OrcEndpoint, SkeletonEndpoint, TrollEndpoint 


application = Flask(__name__)



#################################################
#                                               #
#                                               #
#                   Website                     #
#                                               #
#                                               #
#                                               #
#################################################

# Home page of the website
@application.route('/')
def home():
    return render_template('home.html')

@application.route('/contribute')
def contribute():
    return render_template('contribute.html')


@application.route('/endpoints')
def endpoints():
    return render_template('endpoints.html')


#################################################
#                                               #
#                                               #
#                   API                         #
#                                               #
#                                               #
#                                               #
#################################################
API_Base_v1 = "/api/v1.0/"
First_Name_Key_Message = "Ensure firstName key/value is in body"
Last_Name_Key_Message = "Ensure lastName key/value is in body"
Get_Key_Message = "No key required for GET request"

# Decorator for all monster route functions providing endpoint functionality
def monster_route(func, key_error_message):
    def decorated(*args, **kwargs):
        try:
            # Attempt endpoint query
            return add_cors_headers(func(*args, **kwargs))
        except KeyError:
            # This catches if invalid keys were provided in request
            return add_cors_headers(make_response(jsonify({'error' : 'Invalid key error.',
            'errorMessage' : key_error_message}), 400))
        except ReferenceError:
            # This catches if our verify_users function can't find the x-api-key in the DB
            return add_cors_headers(make_response(jsonify({'error' : 'unauthorised.',
            'errorMessage' : 'unknown x-api-key provided'}), 400))
        except IndexError:
            # This catches if no API key was provided in the first place
            return add_cors_headers(make_response(jsonify({'error' : 'unauthorised.',
            'errorMessage' : 'no x-api-key provided'}), 400))
        except Exception:
            # This catches any other unhandled exceptions
            return add_cors_headers(make_response(jsonify({'error' : 'Unhandled error.',
            'errorMessage' : 'Unknown error occured'}), 400))
    return decorated

# Function to strip first name from request form
def return_request_first_name(request):
    return str(request.form['firstName']).strip()
# Function to strip last name from request form
def return_request_last_name(request):
    return str(request.form['lastName']).strip()
# Function to return x-api-key from request headers
def return_request_api_key(request):
    return request.headers.get("x-api-key")
# Function to cors header to response
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

##### GOBLIN #####
@application.route('/api/v1.0/goblin', methods=['GET'])
def get_goblin():
    return monster_route(GoblinEndpoint.return_name(),Get_Key_Message)

@application.route('/api/v1.0/goblin/firstName', methods=['POST'])
def post_goblin_first_name():
    return monster_route(GoblinEndpoint.insert_first_name(return_request_first_name(request),return_request_api_key(request)), First_Name_Key_Message)

@application.route('/api/v1.0/goblin/lastName', methods=['POST'])
def post_goblin_last_name():
    return monster_route(GoblinEndpoint.insert_last_name(return_request_last_name(request),return_request_api_key(request)), Last_Name_Key_Message)

##### GOATMEN #####
@application.route('/api/v1.0/goatmen', methods=['GET'])
def get_goatmen():
    return monster_route(GoatmenEndpoint.return_name(),Get_Key_Message)

@application.route('/api/v1.0/goatmen/firstName', methods=['POST'])
def post_goatmen_first_name():
    return monster_route(GoatmenEndpoint.insert_first_name(return_request_first_name(request),return_request_api_key(request)), First_Name_Key_Message)

##### OGRE #####
@application.route('/api/v1.0/ogre', methods=['GET'])
def get_ogre():
    return monster_route(GoatmenEndpoint.return_name(),Get_Key_Message)

@application.route('/api/v1.0/ogre/firstName', methods=['POST'])
def post_ogre_first_name():
    return monster_route(OgreEndpoint.insert_first_name(return_request_first_name(request),return_request_api_key(request)), First_Name_Key_Message)

##### ORC #####
@application.route('/api/v1.0/orc', methods=['GET'])
def get_orc():
    return monster_route(OrcEndpoint.return_name(),Get_Key_Message)

@application.route('/api/v1.0/orc/firstName', methods=['POST'])
def post_orc_first_name():
    return monster_route(OrcEndpoint.insert_first_name(return_request_first_name(request),return_request_api_key(request)), First_Name_Key_Message)

@application.route('/api/v1.0/rc/lastName', methods=['POST'])
def post_orc_last_name():
    return monster_route(OrcEndpoint.insert_last_name(return_request_last_name(request),return_request_api_key(request)), Last_Name_Key_Message)

##### SKELETON #####
@application.route('/api/v1.0/skeleton', methods=['GET'])
def get_skeleton():
    return monster_route(SkeletonEndpoint.return_name(),Get_Key_Message)

@application.route('/api/v1.0/skeleton/firstName', methods=['POST'])
def post_skeleton_first_name():
    return monster_route(SkeletonEndpoint.insert_first_name(return_request_first_name(request),return_request_api_key(request)), First_Name_Key_Message)

@application.route('/api/v1.0/skeleton/lastName', methods=['POST'])
def post_skeleton_last_name():
    return monster_route(SkeletonEndpoint.insert_last_name(return_request_last_name(request),return_request_api_key(request)), Last_Name_Key_Message)

##### TROLL #####
@application.route('/api/v1.0/troll', methods=['GET'])
def get_troll():
    return monster_route(TrollEndpoint.return_name(),Get_Key_Message)

@application.route('/api/v1.0/troll/firstName', methods=['POST'])
def post_troll_first_name():
    return monster_route(TrollEndpoint.insert_first_name(return_request_first_name(request),return_request_api_key(request)), First_Name_Key_Message)

@application.route('/api/v1.0/troll/lastName', methods=['POST'])
def post_troll_last_name():
    return monster_route(TrollEndpoint.insert_last_name(return_request_last_name(request),return_request_api_key(request)), Last_Name_Key_Message)


@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Path not found, consult repo for valid endpoints',
                                 'repo' : 'https://github.com/Sudoblark/monsternames-api'}), 404)

if __name__ == '__main__':
    application.run()
