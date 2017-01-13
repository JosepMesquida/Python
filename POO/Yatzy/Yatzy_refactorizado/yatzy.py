class Yatzy:

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score += die
        return score

    @staticmethod
    def yatzy(*dice):
        SCORE = 50
        for die in dice:
            if dice.count(die)==5:
                return SCORE
            else: 
                return 0
    
    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = 3
        return dice.count(THREE) * THREE
 
    @staticmethod
    def fours(*dice):
        FOUR = 4
        return dice.count(FOUR) * FOUR

    @staticmethod
    def fives(*dice):
        FIVE = 5
        return dice.count(FIVE) * FIVE
    
    @staticmethod
    def sixes(*dice):
        SIX = 6
        return dice.count(SIX) * SIX

    
    @staticmethod
    def pair(*dice):
        PAIR = 2
        for number in range(6, 0, -1):
            if dice.count(number) >= PAIR:
                return PAIR * number
        return 0

    @staticmethod
    def two_pair(*dice):
        score = 0
        second_number = 0
        PAIR = 2
        for number in range(6, 0, -1):
            if dice.count(number) >= PAIR:
                second_number = number
                pair1 = PAIR * number
                score += pair1
        
        if score != 0:
            return score
        else:
            return 0       
        
    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = 4
        for number in range(6, 0, -1):
            if dice.count(number) >= FOUR:
                return FOUR * number

        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        THREE = 3
        for number in range(6, 0, -1):
            if dice.count(number) >= THREE:
                return FOUR * number

        return 0
    
    @staticmethod
    def smallStraight(*dice):
        SCORE = 15
        cont = 1
        for die in dice:
            if die == cont:
                cont += 1
            else: 
                return 0

        return SCORE
             
    @staticmethod
    def largeStraight(*dice):
        SCORE = 20
        cont = 2
        for die in dice:
            if die == cont:
                cont += 1
            else: 
                return 0

        return SCORE
    

    @staticmethod
    #i'm sure that it can be more refactored
    def fullHouse(*dice):
        pair_of_three = 0
        pair_of_two = 0
        THREE = 3
        TWO = 2
        for number in range(6, 0, -1):
            if dice.count(number) == THREE:
                pair_of_three = THREE * number

            if dice.count(number) == TWO:
                pair_of_two = TWO * number

        if pair_of_three != 0 and pair_of_two != 0:
            return pair_of_two + pair_of_three
        else:
            return 0