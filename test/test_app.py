# http://flask.pocoo.org/docs/1.0/testing/

import os
import pytest

from reading_level import *

# This will get called before every test and can be used to set up a testing DB
@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_title(client):
    """Verify the title"""
    rv = client.get('/')
    assert b'Reading Level Calculator' in rv.data

def test_text_GET(client):
    """Verify text works"""
    rv = client.get('/?text=hello') # sends a and b as post values
    print(rv.data)
    assert b'8.4' in rv.data

    rv = client.get('/?text=+')
    print(rv.data)
    assert b'-15.59' in rv.data

def test_json_GET(client):
    """Verify json works"""
    rv = client.get('/?json=1&text=hello') # sends a and b as post values
    print(rv.data)
    assert b'8.4' in rv.data

    rv = client.get('/?json=1&text=+')
    print(rv.data)
    assert b'-15.59' in rv.data
