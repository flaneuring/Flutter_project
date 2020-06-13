from flask_restful import Resource
from flask import request
from model import db, User


class Register(Resource):

    def get(self):
        users = User.query.all()
        user_list = []

        for i in range(0, len(users)):
            user_list.append(users[i].serialize())

        return {'status': str(user_list)}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        
        #data, errors = User.load(json_data)

        #if errors:
         #   return errors, 422

        #checks if we already have a user with the same name
        user = User.query.filter_by(username=json_data['username']).first()
        if user:
            return {'message': 'User with the same username already exists!!'}, 400

        user = User.query.filter_by(emailadress=json_data['emailadress']).first()
        if user:
            return {'message': 'Email already exists!!'}, 400


        # get username, email, password
        # check if username exists
        # check if email exists
        # create user
        # create api_key

        user = User(

            firstname = json_data['firstname'],
            lastname = json_data['lastname'],
            username = json_data['username'],
            password = json_data['password'],
            emailadress = json_data['emailadress']


        )
        


        db.session.add(user)
        db.session.commit()

        result = User.serialize(user)

        return { "status": 'success', 'data': result }, 201







