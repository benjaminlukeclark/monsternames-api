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
def monster_route(func):
    def decorated(*args, **kwargs):
        try:
            # Attempt endpoint query
            return add_cors_headers(func(*args, **kwargs))
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
# Function to cors header to response
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

##### GOBLIN #####
@application.route('/api/v1.0/goblin', methods=['GET'])
@monster_route
def get_goblin():
    return GoblinEndpoint.return_name()

@application.route('/api/v1.0/goblin/firstName', methods=['POST'])
@monster_route
def post_goblin_first_name():
    return GoblinEndpoint.insert_first_name(request)

@application.route('/api/v1.0/goblin/lastName', methods=['POST'])
@monster_route
def post_goblin_last_name():
    return GoblinEndpoint.insert_last_name(request)

##### GOATMEN #####
@application.route('/api/v1.0/goatmen', methods=['GET'])
@monster_route
def get_goatmen():
    return GoatmenEndpoint.return_name()

@application.route('/api/v1.0/goatmen/firstName', methods=['POST'])
@monster_route
def post_goatmen_first_name():
    return GoatmenEndpoint.insert_first_name(request)

##### OGRE #####
@application.route('/api/v1.0/ogre', methods=['GET'])
@monster_route
def get_ogre():
    return OgreEndpoint.return_name()

@application.route('/api/v1.0/ogre/firstName', methods=['POST'])
@monster_route
def post_ogre_first_name():
    return OgreEndpoint.insert_first_name(request)

##### ORC #####
@application.route('/api/v1.0/orc', methods=['GET'])
@monster_route
def get_orc():
    return OrcEndpoint.return_name()

@application.route('/api/v1.0/orc/firstName', methods=['POST'])
@monster_route
def post_orc_first_name():
    return OrcEndpoint.insert_first_name(request)

@application.route('/api/v1.0/rc/lastName', methods=['POST'])
@monster_route
def post_orc_last_name():
    return OrcEndpoint.insert_last_name(request)

##### SKELETON #####
@application.route('/api/v1.0/skeleton', methods=['GET'])
@monster_route
def get_skeleton():
    return SkeletonEndpoint.return_name()

@application.route('/api/v1.0/skeleton/firstName', methods=['POST'])
@monster_route
def post_skeleton_first_name():
    return SkeletonEndpoint.insert_first_name(request)

@application.route('/api/v1.0/skeleton/lastName', methods=['POST'])
@monster_route
def post_skeleton_last_name():
    return SkeletonEndpoint.insert_last_name(request)

##### TROLL #####
@application.route('/api/v1.0/troll', methods=['GET'])
@monster_route
def get_troll():
    return TrollEndpoint.return_name()

@application.route('/api/v1.0/troll/firstName', methods=['POST'])
@monster_route
def post_troll_first_name():
    return TrollEndpoint.insert_first_name(request)

@application.route('/api/v1.0/troll/lastName', methods=['POST'])
@monster_route
def post_troll_last_name():
    return TrollEndpoint.insert_last_name(request)


@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Path not found, consult repo for valid endpoints',
                                 'repo' : 'https://github.com/Sudoblark/monsternames-api'}), 404)

if __name__ == '__main__':
    application.run()
