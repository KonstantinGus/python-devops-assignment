from app import add, classify_temperature


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(3,4) == 7

def test_temperature_boundaries() -> None:
    assert classify_temperature(-1) == "freezing"
    assert classify_temperature(0) == "cool"
    assert classify_temperature(19.9) == "cool"
    assert classify_temperature(20) == "warm"