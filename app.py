from flask import Flask, jsonify, request
import redis
from utils import fetch_all_users_from_db, update_user_in_db, delete_user_from_db

app = Flask(__name__)
cache = redis.Redis(host='localhost', port=6379, db=0)

CACHE_TIMEOUT = 600  # Cache timeout in seconds (10 minutes)

@app.route('/users', methods=['GET'])
def get_users():
    cached_users = cache.get('users')
    if cached_users:
        return jsonify(eval(cached_users.decode('utf-8')))

    users = fetch_all_users_from_db()
    cache.set('users', str(users), ex=CACHE_TIMEOUT)
    return jsonify(users)

@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    update_user_in_db(user_id, data)
    cache.delete('users')  # Invalidate the cache
    return 'User updated successfully', 200

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    delete_user_from_db(user_id)
    cache.delete('users')  # Invalidate the cache
    return 'User deleted successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
