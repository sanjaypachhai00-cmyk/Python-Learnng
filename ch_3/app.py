from flask import Flask, jsonify, request

app = Flask(__name__)

users = []


# GET
@app.route("/api/users", methods=["GET"])
def get_users():

    return jsonify({
        "success": True,
        "data": users
    })


# POST
@app.route("/api/users", methods=["POST"])
def add_user():

    data = request.get_json()

    users.append(data)

    return jsonify({
        "success": True,
        "message": "User added successfully",
        "data": data
    }), 201


# PUT
@app.route("/api/users/<username>", methods=["PUT"])
def update_user(username):

    data = request.get_json()

    for user in users:

        if user.get("username") == username:

            user.update(data)

            return jsonify({
                "success": True,
                "message": "User updated successfully",
                "data": user
            }), 200

    return jsonify({
        "success": False,
        "message": "User not found"
    }), 404


# DELETE
@app.route("/api/users/<username>", methods=["DELETE"])
def delete_user(username):

    for user in users:

        if user.get("username") == username:

            users.remove(user)

            return jsonify({
                "success": True,
                "message": "User deleted successfully",
                "data": user
            }), 200

    return jsonify({
        "success": False,
        "message": "User not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)