from flask import make_response, jsonify
import database.models as models
import peewee
from peewee import fn
from database.models import GoblinFirstName, GoblinLastName, GoatmenFirstName, OgreFirstName, OrcFirstName, OrcLastName, SkeletonFirstName, SkeletonLastName, TrollFirstName, TrollLastName
import json

# Base Class for all monster endpoints
class monster_endpoint:
    # Constructor
    def __init__(self, First_Name_Model, Last_Name_Model, First_Name_Present, Last_Name_Present, Monster_Name):
        # Assign params to internal attributes, ensuring we use methods to validate the data being passed through
        self._First_Name = self.__verify_param(First_Name_Present, True)
        self._Last_Name = self.__verify_param(Last_Name_Present, True)
        self._Monster_Name = self.__verify_param(Monster_Name, "String")
        self._First_Name_Model = self.__verify_model(First_Name_Model, "{fMonsterName} first name model".format(fMonsterName = self._Monster_Name))
        self._Last_Name_Model = self.__verify_model(Last_Name_Model, "{fMonsterName} last name model".format(fMonsterName = self._Monster_Name))
    # Return name method
    def return_name(self):
        # Connect to db
        models.db.connect(reuse_if_open=True)
        result = ""
        resultDic = {}
        # Append to result based on what names the monster has
        if self._First_Name:
            FName = self._First_Name_Model.select().order_by(fn.Rand()).limit(1)
            fullName = (FName[0].firstName)
            resultDic["firstName"] = FName[0].firstName
        if self._Last_Name:
            LName = self._Last_Name_Model.select().order_by(fn.Rand()).limit(1)
            resultDic["lastName"] = LName[0].lastName
            if len(fullName) != 0:
                fullName += " " + (LName[0].lastName)
            else:
                fullName = (LName[0].lastName)
        resultDic["fullName"] = fullName
        print(resultDic)
        # Disconnect from DB
        models.db.close()
        # Return json data
        return make_response(json.dumps(resultDic), 200)

    # Insert first name method
    def insert_first_name(self,request):
        # First verify the API key and return the user
        user = self.__verify_user(self.__return_request_api_key(request))
        # Then get the first name, handle the error exception here and return error
        # if the key is not found
        try:
            firstName = self.__return_request_first_name(request)
        except KeyError:
            return make_response(jsonify({'error' : 'Invalid key error.',
            'errorMessage' : "Ensure firstName key/value is in body"}), 400)
        # Connect to db
        models.db.connect(reuse_if_open=True)
        # First check if the record already exists
        if (self._First_Name_Model.select().where(self._First_Name_Model.firstName == firstName)).exists():
            return make_response(jsonify({'error' : 'Duplicate record', 'message' : 'First name record already exists'}), 400)
        # Insert
        self._First_Name_Model.create(firstName=firstName)
        models.PostAudit.create(user=user, message="{fMonsterName} first name record '{fFirstName}' created".format(fMonsterName = self._Monster_Name, fFirstName = firstName))
        models.db.commit()
        models.db.close()
        # Return success
        return make_response(jsonify({'firstName' : firstName, 'message' : 'New record created'}), 200)

    # Insert last name method
    def insert_last_name(self,request):
        # First verify the API key and return the user
        user = self.__verify_user(self.__return_request_api_key(request))
        # Then get the last name, handle the error exception here and return error
        # if the key is not found
        try:
            lastName = self.__return_request_last_name(request)
        except KeyError:
            return make_response(jsonify({'error' : 'Invalid key error.',
            'errorMessage' : "Ensure lastName key/value is in body"}), 400)
        # Connect to db
        models.db.connect(reuse_if_open=True)
        # First check if the record already exists
        if (self._Last_Name_Model.select().where(self._Last_Name_Model.lastName == lastName)).exists():
            return make_response(jsonify({'error' : 'Duplicate record', 'message' : 'Last name record already exists'}), 400)
        # Insert
        self._Last_Name_Model.create(lastName=lastName)
        models.PostAudit.create(user=user, message="{fMonsterName} firstlast name record '{fLastName}' created".format(fMonsterName = self._Monster_Name, fLastName = lastName))
        models.db.commit()
        models.db.close()
        # Return success
        return make_response(jsonify({'lastName' : lastName, 'message' : 'New record created'}), 200)

    # Method to verify that provided param is of the expected type
    def __verify_param(self, var, expected_type):
        if (isinstance(var, type(expected_type))) == False:
            raise TypeError("{fVar} is not of expected type {fExpectedType}".format(fVar = var, fExpectedType = expected_type))
        else:
            return var
    # Method to verify that a valid model has been passed through
    def __verify_model(self, model, model_name):
        model_type = type(model)
        if model_type == peewee.Model:
            raise TypeError("{fModelName} provided is invalid. Must either be of type peewee.Model or None.".format(fModelName = model_name))
        else:
            return model
    # Method in order to verify that the user is authorised to make a POST request
    def __verify_user(self,xApiKey):
        # If there is no xApiKey provided...
        if xApiKey is None:
            raise IndexError
        # Connect to db
        models.db.connect(reuse_if_open=True)
        # Check if the key exists
        apiKeyCheck = models.ApiKeys.select().where(models.ApiKeys.apiKey == xApiKey)
        models.db.close()
        if apiKeyCheck.exists():
            return apiKeyCheck[0].user
        else:
            raise ReferenceError
    # Function to strip first name from request form
    def __return_request_first_name(self, request):
        return str(request.form['firstName']).strip()
    # Function to strip last name from request form
    def __return_request_last_name(self,request):
        return str(request.form['lastName']).strip()
    # Function to return x-api-key from request headers
    def __return_request_api_key(self,request):
        return request.headers.get("x-api-key")


GoblinEndpoint = monster_endpoint(GoblinFirstName, GoblinLastName, True, True, "Goblin")
GoatmenEndpoint = monster_endpoint(GoatmenFirstName, None, True, False, "Goatmen")
OgreEndpoint = monster_endpoint(OgreFirstName, None, True, False, "Ogre")
OrcEndpoint = monster_endpoint(OrcFirstName, OrcLastName, True, True, "Orc")
SkeletonEndpoint = monster_endpoint(SkeletonFirstName, SkeletonLastName, True, True, "Skeleton")
TrollEndpoint = monster_endpoint(TrollFirstName, TrollLastName, True, True, "Troll")
    
