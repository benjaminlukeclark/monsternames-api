from flask import make_response, jsonify
import database.models as models
import peewee
from peewee import *
from peewee import fn
from database.models import GoblinFirstName, GoblinLastName, GoatmenFirstName, OgreFirstName, OrcFirstName, OrcLastName, SkeletonFirstName, SkeletonLastName, TrollFirstName, TrollLastName


# Base Class for all monster endpoints
class monster_endpoint:
    # Constructor
    def __init__(self, First_Name_Model, Last_Name_Model, First_Name_Present, Last_Name_Present, Monster_Name):
        # Assign params to internal attributes, ensuring we use methods to validate the data being passed through
        self._First_Name = self.__verify_param(First_Name_Present, bool)
        self._Last_Name = self.__verify_param(Last_Name_Present, bool)
        self._Monster_Name = self.__verify_param(Monster_Name, str)
        self._First_Name_Model = self.__verify_model(First_Name_Model, f"{self._Monster_Name} first name model")
        self._Last_Name_Model = self.__verify_model(Last_Name_Model, f"{self._Monster_Name} last name model")
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
            resultDic["firstName"] = FName
        if self._Last_Name:
            LName = self._First_Name_Model.select().order_by(fn.Rand()).limit(1)
            resultDic["lastName"] = LName
            if len(result) != 0:
                fullName += " " + (LName[0].lastName)
            else:
                fullName = (LName[0].lastName)
        resultDic["fullName"] = fullName
        # Disconnect from DB
        models.db.close()
        # Return json data
        return make_response(jsonify(resultDic), 200)

    # Insert first name method
    def insert_first_name(self,firstName, apiKey):
        # First verify the API key and return the user
        user = self.__verify_user(apiKey)
        # Connect to db
        models.db.connect(reuse_if_open=True)
        # First check if the record already exists
        if (self._First_Name_Model.select().where(self._First_Name_Model.firstName == firstName)).exists():
            return make_response(jsonify({'error' : 'Duplicate record', 'message' : 'Record already exists'}), 400)
        # Insert
        self._First_Name_Model.create(firstName=firstName)
        models.PostAudit.create(user=user, message=f"{self._Monster_Name} first name record '{firstName}' created")
        models.db.commit()
        models.db.close()
        # Return success
        return make_response(jsonify({'firstName' : firstName, 'message' : 'New record created'}), 200)

    # Insert last name method
    def insert_last_name(self,lastName, apiKey):
        # First verify the API key and return the user
        user = self.__verify_user(apiKey)
        # Connect to db
        models.db.connect(reuse_if_open=True)
        # First check if the record already exists
        if (self._Last_Name_Model.select().where(self._Last_Name_Model.lastName == lastName)).exists():
            return make_response(jsonify({'error' : 'Duplicate record', 'message' : 'Record already exists'}), 400)
        # Insert
        self._Last_Name_Model.create(lastName=lastName)
        models.PostAudit.create(user=user, message=f"{self._Monster_Name} last name record '{lastName}' created")
        models.db.commit()
        models.db.close()
        # Return success
        return make_response(jsonify({'lastName' : lastName, 'message' : 'New record created'}), 200)

    # Method to verify that provided param is of the expected type
    def __verify_param(self, var, expected_type):
        if (isinstance(var, expected_type)) == False:
            raise TypeError(f"{var} is not of expected type {expected_type}")
        else:
            return var
    # Method to verify that a valid model has been passed through
    def __verify_model(self, model, model_name):
        if (((isinstance(model, peewee.Model)) == False) & ((isinstance(model, None)) == False)):
            raise TypeError(f"{model_name} provided is invalid. Must either be of type peewee.Model or None.")
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


GoblinEndpoint = monster_endpoint(GoblinFirstName, GoblinLastName, True, True, "Goblin")
GoatmenEndpoint = monster_endpoint(GoatmenFirstName, None, True, False, "Goatmen")
OgreEndpoint = monster_endpoint(GoblinFirstName, OgreFirstName, True, False, "Ogre")
OrcEndpoint = monster_endpoint(OrcFirstName, OrcLastName, True, True, "Orc")
SkeletonEndpoint = monster_endpoint(SkeletonFirstName, SkeletonLastName, True, True, "Skeleton")
TrollEndpoint = monster_endpoint(TrollFirstName, TrollLastName, True, True, "Troll")
    
