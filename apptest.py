from flask import Flask, request, jsonify, send_from_directory

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static', static_folder='static')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jouerflux.db'

# db = SQLAlchemy(app)


# class Firewall(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     ip_address = db.Column(db.String(120), nullable=False)

@app.route('/test-static')
def test_static():
    return send_from_directory(app.static_folder, 'swagger.json')

# @app.route('/', methods=['GET'])
# def init_firewall():
#     # init table if no db
#     db.create_all()
#     # Add an example to the database
#     example_f = Firewall(name='Example1')
#     db.session.add(example_f)
#     db.session.commit()
#     return "init database"
#
#
# @app.route('/firewall', methods=['POST'])
# def create_firewall():
#     """
#         POST /firewall
#         Adds one new firewall to db.
#         Request Body:
#             application/json:
#                 properties:
#                     name:
#                         type: string
#                 required:
#                     - name
#         Responses:
#             201:
#                 description: success message.
#                 content:
#                     application/json:
#                         example: {'message':'Firewall created'}
#             400:
#                 description: Name not empty error message.
#                 content:
#                     application/json:
#                         example: {'error':'Name cannot be empty'}
#         """
#     data = request.get_json()
#     name = data.get('name')
#
#     if not name:
#         return jsonify({'message': 'Name cannot be empty'}), 400
#
#     firewall1 = Firewall(name=name)
#
#     db.session.add(firewall1)
#     db.session.commit()
#     return jsonify({'message': f'Firewall {name} created'}), 201
#
#
# @app.route('/firewall', methods=['GET'])
# # add pagination if have time
# def get_firewalls():
#     """
#         GET /firewall
#         Returns a list of interventions.
#
#         Responses:
#             200:
#                 description: list of firewalls.
#                 content:
#                     application/json:
#                         example: [
#                             {
#                                 "id": "1"
#                                 "name": "Firewall1"
#                             },
#                             {
#                                 "id": "2"
#                                 "name": "Firewall2"
#                             }]
#             404:
#                 description: firewalls not found error message.
#                 content:
#                     application/json:
#                         example: {'message': 'empty table'}
#         """
#     firewalls = Firewall.query.all()
#     if not firewalls:
#         return jsonify({'message': 'empty table'}), 404
#
#     data = []
#     for f in firewalls:
#         firewall_data = {
#             'id': f.id,
#             'name': f.name
#         }
#         data.append(firewall_data)
#
#     return jsonify(data), 200
#
# @app.route('/firewall/<int:id>', methods=['DELETE'])
# def delete_f(id):
#     """
#         DELETE /firewall/<int:id>
#         Deletes an existing firewall from the db.
#
#         Path Parameters:
#             id (int): The ID of the firewall to delete.
#
#         Responses:
#             200:
#                 description: Success message.
#                 content:
#                     application/json:
#                         example: {'message': 'Firewall deleted'}
#             404:
#                 description: Intervention not found error message.
#                 content:
#                     application/json:
#                         example: {'message': 'Firewall not found'}
#         """
#     firewall = Firewall.query.get_or_404(id)
#     db.session.delete(firewall)
#     db.session.commit()
#     return jsonify({'message': f'firewall {id} deleted'}), 200

if __name__ == '__main__':
    app.run()
