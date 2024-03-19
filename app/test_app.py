import pytest

from run import app as application

# import unit tersts

@pytest.fixture()
def app():
    application.config.update({
        "TESTING": True,
    })
    yield application


@pytest.fixture
def client(app):   
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

£ test that a 200 requerst is correctly returned as 200 as wekk as a flask binary text being returned
def test_api(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask" in response.data
