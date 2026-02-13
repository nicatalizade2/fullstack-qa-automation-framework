import requests
import yaml
import json
# config = yaml.safe_load(open('config.yaml'))
# base_url = config['api_base_url']
def test_get_users(api):
    response = api.get("/posts/1")

    assert response.status_code == 200

    data = response.json()
    print("\nDEBUG DATA:", json.dumps(data, indent=4))

    assert len(data) > 0
    assert 'title' in data

def test_create_user(api):
    create = {
        "title": "Nicat's Post",
        "body": "QA Engineer content",
        "userId": 1
    }

    response = api.post("/posts", data=create)

    assert response.status_code == 201
    data = response.json()

    assert data['title'] == create['title']

    for key in create:
        assert data[key] == create[key]

def test_single_user(api):
    response = api.get('/posts/2')
    assert response.status_code == 200
    data = response.json()

    assert data['title'] == 'qui est esse'
    assert data['id'] == 2