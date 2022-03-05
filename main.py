from flask import Flask, request
from flask_restful import Api, Resource
from pydantic import constr, BaseModel
from pydantic.dataclasses import dataclass
from flask_pydantic import validate


app = Flask(__name__)
api = Api(app)


users = [
    {
        "id": 1,
        "first_name": "alex",
        "age": 31
    },
    {
        "id": 2,
        "first_name": "bob",
        "age": 32
    },
    {
        "id": 3,
        "first_name": "carl",
        "age": 33
    },
]

class UserModel(BaseModel):
    first_name: str
    age: int = None


class UserDTO(BaseModel):
    id: int
    first_name: str
    age: int


class UserList(Resource):
    def get(self):
        return users

    @validate(body=UserDTO)
    def post(self):
        user = {"id": users[-1]["id"] + 1}
        user.update(request.json)
        users.append(user)

        return user


class User(Resource):
    def get(self, user_id):
        user = list(filter(lambda x: x["id"] == int(user_id), users))
        return user[0] if user else {}

    @validate(body=UserModel)
    def put(self, user_id):
        user_id = int(user_id)
        user_index = [index for (index, item) in enumerate(
            users) if item["id"] == user_id]
        if user_index:
            user_index = user_index[0]
            user = {"id": users[user_index]["id"]}
            user.update(request.json)
            users[user_index] = user
            return users[user_index]
        else:
            return {}

    def delete(self, user_id):
        user_id = int(user_id)
        user_index = [index for (index, item) in enumerate(
            users) if item["id"] == user_id]
        user_index = user_index[0] if user_index else None
        if user_index:
            result = users[user_index]
            del users[user_index]
            return result
        else:
            return {}


api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<user_id>')

if __name__ == '__main__':
    app.run(debug=True)
