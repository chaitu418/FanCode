import requests
import pytest

# Constants for the API endpoints and FanCode city boundary
USERS_API = 'http://jsonplaceholder.typicode.com/users'
TODOS_API = 'http://jsonplaceholder.typicode.com/todos'
FANCODE_LAT_MIN = -40
FANCODE_LAT_MAX = 5
FANCODE_LNG_MIN = 5
FANCODE_LNG_MAX = 100


@pytest.fixture(scope="module")
def get_users():
    response = requests.get(USERS_API)
    return response.json()


@pytest.fixture(scope="module")
def get_todos():
    response = requests.get(TODOS_API)
    return response.json()


def is_fancode_city(user):
    lat = float(user['address']['geo']['lat'])
    lng = float(user['address']['geo']['lng'])
    return FANCODE_LAT_MIN <= lat <= FANCODE_LAT_MAX and FANCODE_LNG_MIN <= lng <= FANCODE_LNG_MAX


def get_user_todos_list(user_id, todos):
    return [todo for todo in todos if todo['userId'] == user_id]


def test_fancode_users_list_todos_completion(get_users, get_todos):
    users = get_users
    todos = get_todos

    fancode_users_list = [user for user in users if is_fancode_city(user)]

    for user in fancode_users_list:
        user_todos_list = get_user_todos_list(user['id'], todos)
        if not user_todos_list:
            continue

        completed_todos = [todo for todo in user_todos_list if todo['completed']]
        completion_percentage = (len(completed_todos) / len(user_todos_list)) * 100

        print(f"\nUser --> {user['name']} with User ID -->{user['id']} has completed {completion_percentage:.2f}% of their todos.")
        assert completion_percentage > 50, f"User {user['name']} ({user['id']}) has not completed more than half of their todos."

