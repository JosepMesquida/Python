from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.

def test_chance():
    assert 14 == Yatzy.chance(1,1,3,3,6)
    assert 21 == Yatzy.chance(4,5,5,6,1)

#Yatzy
#If all dice have the same number, the player scores 50 points.

def test_yatzy():
    assert 50 == Yatzy.yatzy(1,1,1,1,1)
    assert 0 == Yatzy.yatzy(1,1,1,2,1)

#Ones
#The player scores the sum of the dice that reads one.

def test_ones():
    assert 2 == Yatzy.ones(1,1,2,4,4)
    assert 1 == Yatzy.ones(2,3,2,5,1)
    assert 0 == Yatzy.ones(3,3,3,4,5)

#Twos
#The player scores the sum of the dice that reads two.

def test_twos():
    assert 4 == Yatzy.twos(2,3,2,5,1)
    assert 2 == Yatzy.twos(1,1,2,4,4)

#threes
#The player scores the sum of the dice that reads three.

def test_threes():
    assert 6 == Yatzy.threes(3,2,1,3,4)
    assert 12 == Yatzy.threes(3,3,3,3,4)
    assert 3 == Yatzy.threes(2,6,4,3,1)

#Fours
#The player scores the sum of the dice that reads four.

def test_fours():
    assert 4 == Yatzy.fours(3,2,1,3,4)
    assert 8 == Yatzy.fours(3,3,4,3,4)
    assert 12 == Yatzy.fours(4,6,4,3,4)

#Fives
#The player scores the sum of the dice that reads five.

def test_fives():
    assert 5 == Yatzy.fives(3,5,4,1,2)
    assert 15 == Yatzy.fives(3,5,4,5,5)
    assert 10 == Yatzy.fives(3,5,4,5,2)

#Sixes
#The player scores the sum of the dice that reads six.

def test_sixes():
    assert 6 == Yatzy.sixes(3,6,4,1,2)
    assert 12 == Yatzy.sixes(3,6,4,6,5)
    assert 18 == Yatzy.sixes(6,5,4,6,6)

#Pair
#The player scores the sum of the two highest matching dice.

def test_pair():
    assert 8 == Yatzy.pair(3,3,3,4,4)
    assert 12 == Yatzy.pair(1,1,6,2,6)
    assert 6 == Yatzy.pair(3,3,3,4,1)
    assert 6 == Yatzy.pair(3,3,3,3,1)

#Two_pairs
#If there are two pairs of dice with the same number, the player scores the sum of these dice. 

def test_two_pairs():
    assert 8 == Yatzy.two_pair(1,1,2,3,3)
    assert 2== Yatzy.two_pair(1,1,2,3,4)
    assert 6 == Yatzy.two_pair(1,1,2,2,2)

#Three_of_a_kind
#If there are three dice with the same number, the player scores the sum of these dice.

def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3,3,3,4,5)
    assert 0 == Yatzy.three_of_a_kind(3,3,4,5,6)
    assert 9 == Yatzy.three_of_a_kind(3,3,3,3,1)

#Four_of_a_kind
#If there are four dice with the same number, the player scores the sum of these dice. 

def test_four_of_a_kind():
    assert 8 == Yatzy.four_of_a_kind(2,2,2,2,5)
    assert 0 == Yatzy.four_of_a_kind(2,2,2,5,5)
    assert 8 == Yatzy.four_of_a_kind(2,2,2,2,2)

#SmallStraight
#When placed on "small straight", if the dice read (1,2,3,4,5,) the player scores 15 (the sum of all the dice).

def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1,2,3,4,5)
    assert 0 == Yatzy.smallStraight(1,2,4,3,5)

#LargeStraight
#When placed on "large straight", if the dice read (2,3,4,5,6) the player scores 20 (the sum of all the dice).

def test_largeStraight():
    assert 20 == Yatzy.largeStraight(2,3,4,5,6)
    assert 0 == Yatzy.largeStraight(1,5,3,4,5)

#FullHouse
#If the dice are two of a kind and three of a kind, the player scores the sum of all the dice.

def test_fullHouse():
    assert 8 == Yatzy.fullHouse(1,1,2,2,2)
    assert 0 == Yatzy.fullHouse(4,4,4,4,4)
    assert 0 == Yatzy.fullHouse(2,2,3,3,4)

if __name__ == '__main__':
    test_chance()
    test_yatzy()
    test_ones()
    test_twos()
    test_threes()
    test_fours()
    test_fives()
    test_sixes()
    test_pair()
    test_two_pairs()
    test_three_of_a_kind()
    test_four_of_a_kind()
    test_smallStraight()
    test_largeStraight()
    test_fullHouse()
