
import pytest
import json
import beerapi


@pytest.fixture()
def app():
    beerapi.app.testing = True
    app = beerapi.app.test_client()
    return app


def test_root(app):
    assert json.loads(app.get('/').data.decode()) == {}
