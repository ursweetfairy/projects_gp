import funkcje
import pytest

def test_add():
    assert funkcje.add(2,4) == 6
    assert not funkcje.add (2,3) == 6
  
def test_if_palindrom(): 
    assert funkcje.if_palindrom("kamilslimak")
    assert funkcje.if_palindrom("ala")
    assert not funkcje.if_palindrom("wiadro")
    assert not funkcje.if_palindrom("kamyk")

def test_valid_triangle():
    assert funkcje.if_valid_triangle(2,3,4)
    assert funkcje.if_valid_triangle(5,9,5)

def test_invalid_triangle():
    assert not funkcje.if_valid_triangle(1,1,2)
    assert not funkcje.if_valid_triangle(-2,0,1)

def test_divide(capsys):
    funkcje.divide(4,2)
    out, err = capsys.readouterr()
    assert out == '2.0\n'

def test_divide_exception(capsys):
    funkcje.divide(4,0)
    out, err = capsys.readouterr()
    assert out == 'Nie dziel przez 0\n'

@pytest.mark.parametrize(
    "strings, expected",
    [
        (['kot', 'dziobak', 'pies'], ['kot', 'pies', 'dziobak']),
        (["minecraft", "roblox", "cs"], ['cs', 'roblox', 'minecraft'])
    ])
def test_sort_strings_by_len(strings, expected):
    assert funkcje.sort_strings_by_length(strings) == expected

def test_prime_number():
    assert funkcje.if_prime(5) 
    assert not funkcje.if_prime(4)
    assert not funkcje.if_prime(1)
    assert not funkcje.if_prime(0) 
    assert not funkcje.if_prime(-1) 

def test_calculate_mean():
    assert funkcje.calculate_mean([1,3,8]) == 4

def test_calculate_mean_empty_list(): 
    assert funkcje.calculate_mean([]) == -1

def test_calculate_mean_incorect_data(): 
    assert funkcje.calculate_mean([1,2,'kot']) == -2
