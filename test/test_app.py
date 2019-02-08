# http://flask.pocoo.org/docs/1.0/testing/

import os
import pytest

from app import *

# This will get called before every test and can be used to set up a testing DB
@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_title(client):
    """Verify the title"""
    rv = client.get('/')
    assert b'Multiply App' in rv.data

def test_multiplication_POST(client):
    """Verify multiplication works"""
    rv = client.post('/', data={'a':5, 'b':6}) # sends a and b as post values
    assert b'30' in rv.data

    rv = client.post('/', data={'a':-5, 'b':2})
    assert b'-10' in rv.data

def test_multiplication_GET(client):
    """Verify multiplication works"""
    rv = client.get('/?a=5&b=10') # sends a and b as post values
    assert b'50' in rv.data

    rv = client.get('/?a=9&b=9')
    assert b'81' in rv.data