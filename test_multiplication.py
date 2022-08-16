import pytest

@pytest.fixture
def value():
   input = 39
   return input
@pytest.mark.priya()
def test_multiplication_11(value):
    x=0
    for i in range(1,value):
        x=x+i
    print(x)
