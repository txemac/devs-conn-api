from starlette.status import HTTP_200_OK


def test__health(client):
    response = client.get("/_health")
    assert response.status_code == HTTP_200_OK
    assert response.json() == dict(status='OK')
