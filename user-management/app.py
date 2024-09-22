from flask import Flask, request, jsonify
import boto3
import uuid

app = Flask(__name__)

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UsersTable')


# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()  # Get data sent in the request body
    user_id = str(uuid.uuid4())  # Generate a unique ID for the user

    # Put the user data into the DynamoDB table
    table.put_item(
        Item={
            'user_id': user_id,
            'email': data['email'],
            'password': data['password'],  # Normally, you'd hash this
            'name': data['name']
        }
    )
    return jsonify({'message': 'User created successfully', 'user_id': user_id}), 201


# Get a user by ID
@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    response = table.get_item(Key={'user_id': user_id})
    user = response.get('Item')

    if not user:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(user)


# Update a user
@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    try:
        table.update_item(
            Key={'user_id': user_id},
            UpdateExpression="SET #n = :n, email = :e",
            ExpressionAttributeNames={
                '#n': 'name'  # Use #n as a placeholder for the reserved keyword
            },
            ExpressionAttributeValues={
                ':n': data.get('name'),
                ':e': data.get('email')
            }
        )
        return jsonify({'message': 'User updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Error updating user'}), 500

# Delete a user
@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        table.delete_item(Key={'user_id': user_id})
        return jsonify({'message': 'User deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Error deleting user'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
