# app.py
# This is a addition of 2 numbers --for workflow
def add(a, b):
    return a + b
#testing the addition
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
