# #!/usr/bin/env python3


# import jwt
# from flask import Flask, request, jsonify
# from models.users import User
# from models.owners import Owner
# from models.operators import Operator

# flask_app = Flask(__name__)

# SECRET_KEY = "752a138157bb5c953d4affed3c12d71a314e65399139b1723e5e9f66e80106ec"


# def token_required(func):
#     @wraps(func)
#     def wrap(*args, **kwargs):
#         try:
#             token_passed = request.headers['TOKEN']
#             if request.headers['TOKEN'] != '' and
#             request.headers['TOKEN'] is not None:
#                 try:
#                     data = jwt.decode(token_passed, SECRET_KEY,
#                                       algorithms=['HS256'])

#                     all_users = storage.all(User).values()
#                     all_operators = storage.all(Operator).values()
#                     all_owners = storage.all(Owner).values()

#                     for user in all_users:
#                         if user.email == data.get("email"):
#                             current_user = user

#                     for operator in all_operators:
#                         if operator.email == data.get("email"):
#                             current_user = operator

#                     for owner in all_owners:
#                         if owner.email == data.get("email"):
#                             current_user = owner

#                     if current_user is None:
#                         ;

#                     return func(current_user, *args, **kwargs)

#                 except jwt.exceptions.ExpiredSignatureError:
#                     return_data = {
#                         "error": "0",
#                         "message": "Token has expired"
#                     }
#                     return jsonify(return_data), 401
#                 except:
#                     return_data = {
#                         "error": "1",
#                         "message": "Invalid Token"
#                     }
#                     return jsonify(return_data), 401
#             else:
#                 return_data = {
#                     "error": "2",
#                     "message": "Token required",
#                 }
#                 return jsonify(return_data), 401
#         except Exception as e:
#             return_data = {
#                 "error": "3",
#                 "message": "An error occured"
#             }
#             return jsonify(return_data), 500

#     return wrap
