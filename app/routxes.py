from flask_login import login_required
from flask_migrate import current
from app import app, db
from flask_login import current_user, login_user, logout_user
from app.models import User
from flask import jsonify, request


@app.route('/', methods=['GET'])
def index():
    return "Hello World"


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        post_data = request.json

        if current_user.is_authenticated:
            response = {'status': 'invalid', 'message': 'Already logged in.'}
            return jsonify(response, 200)

        # QUERY FOR GRTTING THE USER WITH THE
        user = User.query.filter_by(username=post_data.get('username')).first()

        if user is None:
            response = {
                'status': 'invalid',
                'message': 'No user found with that username.'
            }
            return jsonify(response, 404)

        if user.check_password(post_data.get('password')):
            login_user(user)
            response = {'user_id': user.id, 'username': user.username}
            return jsonify(response, 200)

        else:
            response = {'status': 'fail', 'message': 'Incorrect password.'}
            return jsonify(response, post_data.get('password'), 403)

    except:
        response = {'status': 'fail', 'message': 'Try again.'}
        return jsonify(response, 500)


# @app.route('/logout')
# # @login_required
# def logout():
#     if current_user.is_authenticated:
#         logout_user()
#         response = {
#             'status': 'success',
#             'message': 'Succesfully logged out of account.'
#         }
#         return jsonify(response, 200)
#     else:
#         response = {'status': 'invalid', 'message': 'Not logged in.'}
#         return jsonify(response, 401)


# # @app.route('/register')
# # def register():
# #     try:
# #         post_data = request.args

# #         if current_user.is_authenticated:
# #             response = {'status': 'invalid', 'message': 'Already logged in.'}
# #             return jsonify(response, 200)

# #         user = User.query.filter_by(username=post_data.get('username')).first()

# #         if user is not None:
# #             response = {
# #                 'status': 'invalid',
# #                 'message': 'Username has already been taken.'
# #             }
# #             return jsonify(response, 404)

# #         user = User.query.filter_by(username=post_data.get('email')).first()

# #         if user is not None:
# #             response = {
# #                 'status': 'invalid',
# #                 'message': 'Email has already been registered.'
# #             }
# #             return jsonify(response, 404)

# #         if post_data.get('usertype') == "alumni":

# #         if user.check_password(post_data.get('password')):
# #             login_user(user)
# #             response = {'user_id': user.id, 'username': user.username}
# #             return jsonify(response, 200)

# #         else:
# #             response = {'status': 'fail', 'message': 'Incorrect password.'}
# #             return jsonify(response, post_data.get('password'), 403)

# #     except:
# #         response = {'status': 'fail', 'message': 'Try again.'}
# #         return jsonify(response, 500)

# # from flask import jsonify, request

# from app.models import Message, Student, Recruiter, Account


# @app.route('/notifications', methods=['GET', 'POST'])
# def load_notifactions():
#     # get an request object
#     post_data = request.args

#     u = Account.query.get(post_data['user_id'])

#     m = Message(subject=post_data['subject'],
#                 content=post_data['content'],
#                 author=u)
#     db.session.add(m)
#     db.session.commit()

#     # u = Account.query.get(post_data.get('user_id'))

#     # m = Message.query.filter_by(author=u).first()

#     # manipulation and return objects defined
#     return jsonify({'status': 'success', 'message': 'succesful'}, 200)


# @app.route('/readreceipt', methods=['POST', 'GET'])
# def readReceipts():
#     response = {'status': 'success', 'message': 'Succesfull.'}
#     return jsonify(response), 500


# def fxn():
#     u = User.query.filter_by(username='sriram').first()

#     messages = Post.query.all()

#     user_messages = list()

#     for msent_message in u.recieved_messages:
#         ads = ToBeRead.query.filter_by(user_id=to_id,
#                                     entity_id=message.id,
#                                     type="message").first()
#         isPending = ads is not None
#         message['isPending'] = isPending # create new attribute
#         user_messages.push(message)

#     for msent_message in u.sent_messages:
#         user_messages.push(msent_message)
#     for msent_message in u.recieved_messages:
#         ads = ToBeRead.query.filter_by(user_id=to_id,
#                                     entity_id=message.id,
#                                     type="message").first()
#         isPending = ads is not None
#         message['isPending'] = isPending # create new attribute
#         user_messages.push(message)

#     for msent_message in u.sent_messages:
#         user_messages.push(msent_message)
#     for msent_message in u.recieved_messages:
#         ads = ToBeRead.query.filter_by(user_id=to_id,
#                                     entity_id=message.id,
#                                     type="message").first()
#         isPending = ads is not None
#         message['isPending'] = isPending # create new attribute
#         user_messages.push(message)

#     for msent_message in u.sent_messages:
#         user_messages.push(msent_message)


#     return jsonify(dict(user_messages)), 200
