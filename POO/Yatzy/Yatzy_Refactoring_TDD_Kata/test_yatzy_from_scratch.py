from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.

def test_chance():
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

def test_yatzy():
    assert 50 == Yatzy.yatzy(1,1,1,1,1)
    assert 0 == Yatzy.yatzy(1,1,1,2,1)

def test_ones():
    assert 2 == Yatzy.ones(1,1,2,4,4)
    assert 1 == Yatzy.ones(2,3,2,5,1)
    assert 0 == Yatzy.ones(3,3,3,4,5)

def test_twos():
    assert 4 == Yatzy.twos(2,3,2,5,1)
    assert 2 == Yatzy.twos( 1,1,2,4,4)

def test_pair():
    assert 8 == Yatzy.pair(3,3,3,4,4)
    assert 12 == Yatzy.pair(1,1,6,2,6)
    assert 6 == Yatzy.pair(3,3,3,4,1)
    assert 6 == Yatzy.pair(3, 3, 3, 3, 1)

def test_two_pairs():
    assert 8 == Yatzy.two_pair(1,1,2,3,3)
    assert 0 == Yatzy.two_pair(1,1,2,3,4)
    assert 6 == Yatzy.two_pair(1,1,2,2,2)

if __name__ == '__main__':
    test_two_pairs()
