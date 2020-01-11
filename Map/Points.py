class Points:
    def __init__(self):
        self.pointsPlayer1 = 0
        self.pointsPlayer2 = 0
        self.pointsPlayer3 = 0
        self.pointsPlayer4 = 0

    def normalPointsIncrement(self, index):
        if index == 0:
            self.pointsPlayer1 += 10
        elif index == 1:
            self.pointsPlayer2 += 10
        elif index == 2:
            self.pointsPlayer3 += 10
        else:
            self.pointsPlayer4 += 10

    #ovde kasnije dodati metode za povecanje poena kada se pokupi bonus i kada se ubije neprijatelj