def fetch_all_users_from_db():
    # Mock database fetch
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]

def update_user_in_db(user_id, data):
    # Mock database update
    print(f'Updating user {user_id} with data: {data}')

def delete_user_from_db(user_id):
    # Mock database delete
    print(f'Deleting user {user_id}')
