from functions import  salary,hello_who

def test_hello_who_max():
    assert hello_who('Max') == 'Hello,Max'
    assert 1 == 1
    assert hello_who('Brat') == 'Hello,Brat'
def test_salary():
    assert salary(4, 5) == 40
    assert(3,2) !=12
