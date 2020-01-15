
class Enemy:
    def __init__(self):
        self.coordinateForEnemies = []
        self.coordinateMethod(firstX=422, firstY=347, stepX=32, stepY=30.5)

    def coordinateMethod(self, firstX, firstY, stepX, stepY):
        #first
        self.coordinateForEnemies.append((firstX - (stepX*12), firstY - (stepY*10)))
        self.coordinateForEnemies.append((firstX - (stepX*7), firstY - (stepY*10)))
        self.coordinateForEnemies.append((firstX - (stepX*1), firstY - (stepY*10)))
        self.coordinateForEnemies.append((firstX + (stepX*2), firstY - (stepY*10)))
        self.coordinateForEnemies.append((firstX + (stepX*8), firstY - (stepY*10)))
        self.coordinateForEnemies.append((firstX + (stepX*13), firstY - (stepY*10)))

        #second
        self.coordinateForEnemies.append((firstX - (stepX*12), firstY - (stepY*6)))
        self.coordinateForEnemies.append((firstX - (stepX*7), firstY - (stepY*6)))
        self.coordinateForEnemies.append((firstX - (stepX*4), firstY - (stepY*6)))
        self.coordinateForEnemies.append((firstX - (stepX*1), firstY - (stepY*6)))
        self.coordinateForEnemies.append((firstX + (stepX*2), firstY - (stepY*6)))
        self.coordinateForEnemies.append((firstX + (stepX*5), firstY - (stepY*6)))
        self.coordinateForEnemies.append((firstX + (stepX*8), firstY - (stepY*6)))
        self.coordinateForEnemies.append((firstX + (stepX*13), firstY - (stepY*6)))

        #third
        self.coordinateForEnemies.append((firstX - (stepX * 12), firstY - (stepY * 3)))
        self.coordinateForEnemies.append((firstX - (stepX * 7), firstY - (stepY * 3)))
        self.coordinateForEnemies.append((firstX - (stepX * 4), firstY - (stepY * 3)))
        self.coordinateForEnemies.append((firstX - (stepX * 1), firstY - (stepY * 3)))
        self.coordinateForEnemies.append((firstX + (stepX * 2), firstY - (stepY * 3)))
        self.coordinateForEnemies.append((firstX + (stepX * 5), firstY - (stepY * 3)))
        self.coordinateForEnemies.append((firstX + (stepX * 8), firstY - (stepY * 3)))
        self.coordinateForEnemies.append((firstX + (stepX * 13), firstY - (stepY * 3)))

        #foruth
        self.coordinateForEnemies.append((firstX - (stepX * 4), firstY))
        self.coordinateForEnemies.append((firstX - (stepX * 1), firstY))
        self.coordinateForEnemies.append((firstX - (stepX * 0), firstY))
        self.coordinateForEnemies.append((firstX + (stepX * 1), firstY))
        self.coordinateForEnemies.append((firstX + (stepX * 2), firstY))
        self.coordinateForEnemies.append((firstX + (stepX * 5), firstY))

        #fifth
        self.coordinateForEnemies.append((firstX - (stepX * 2), firstY + (stepY * 2)))
        self.coordinateForEnemies.append((firstX - (stepX * 1), firstY + (stepY * 2)))
        self.coordinateForEnemies.append((firstX - (stepX * 0), firstY + (stepY * 2)))
        self.coordinateForEnemies.append((firstX + (stepX * 1), firstY + (stepY * 2)))
        self.coordinateForEnemies.append((firstX + (stepX * 2), firstY + (stepY * 2)))
        self.coordinateForEnemies.append((firstX + (stepX * 3), firstY + (stepY * 2)))

        #sixth---middle
        self.coordinateForEnemies.append((firstX - (stepX * 7), firstY + (stepY * 3)))
        self.coordinateForEnemies.append((firstX - (stepX * 2), firstY + (stepY * 3)))
        self.coordinateForEnemies.append((firstX - (stepX * 1), firstY + (stepY * 3)))
        self.coordinateForEnemies.append((firstX - (stepX * 0), firstY + (stepY * 3)))
        self.coordinateForEnemies.append((firstX + (stepX * 1), firstY + (stepY * 3)))
        self.coordinateForEnemies.append((firstX + (stepX * 2), firstY + (stepY * 3)))
        self.coordinateForEnemies.append((firstX + (stepX * 3), firstY + (stepY * 3)))
        self.coordinateForEnemies.append((firstX + (stepX * 8), firstY + (stepY * 3)))

        #seventh
        self.coordinateForEnemies.append((firstX - (stepX * 2), firstY + (stepY * 4)))
        self.coordinateForEnemies.append((firstX - (stepX * 1), firstY + (stepY * 4)))
        self.coordinateForEnemies.append((firstX - (stepX * 0), firstY + (stepY * 4)))
        self.coordinateForEnemies.append((firstX + (stepX * 1), firstY + (stepY * 4)))
        self.coordinateForEnemies.append((firstX + (stepX * 2), firstY + (stepY * 4)))
        self.coordinateForEnemies.append((firstX + (stepX * 3), firstY + (stepY * 4)))

        #eighth
        self.coordinateForEnemies.append((firstX - (stepX * 4), firstY + (stepY * 6)))
        self.coordinateForEnemies.append((firstX - (stepX * 1), firstY + (stepY * 6)))
        self.coordinateForEnemies.append((firstX - (stepX * 0), firstY + (stepY * 6)))
        self.coordinateForEnemies.append((firstX + (stepX * 1), firstY + (stepY * 6)))
        self.coordinateForEnemies.append((firstX + (stepX * 2), firstY + (stepY * 6)))
        self.coordinateForEnemies.append((firstX + (stepX * 5), firstY + (stepY * 6)))

        #nineth
        self.coordinateForEnemies.append((firstX - (stepX * 12), firstY - (stepY * 9)))
        self.coordinateForEnemies.append((firstX - (stepX * 7), firstY - (stepY * 9)))
        self.coordinateForEnemies.append((firstX - (stepX * 4), firstY - (stepY * 9)))
        self.coordinateForEnemies.append((firstX - (stepX * 1), firstY - (stepY * 9)))
        self.coordinateForEnemies.append((firstX + (stepX * 2), firstY - (stepY * 9)))
        self.coordinateForEnemies.append((firstX + (stepX * 5), firstY - (stepY * 9)))
        self.coordinateForEnemies.append((firstX + (stepX * 8), firstY - (stepY * 9)))
        self.coordinateForEnemies.append((firstX + (stepX * 13), firstY - (stepY * 9)))

        #tenth
        self.coordinateForEnemies.append((firstX - (stepX * 12), firstY - (stepY * 12)))
        self.coordinateForEnemies.append((firstX - (stepX * 7), firstY - (stepY * 12)))
        self.coordinateForEnemies.append((firstX - (stepX * 4), firstY - (stepY * 12)))
        self.coordinateForEnemies.append((firstX - (stepX * 1), firstY - (stepY * 12)))
        self.coordinateForEnemies.append((firstX + (stepX * 2), firstY - (stepY * 12)))
        self.coordinateForEnemies.append((firstX + (stepX * 5), firstY - (stepY * 12)))
        self.coordinateForEnemies.append((firstX + (stepX * 8), firstY - (stepY * 12)))
        self.coordinateForEnemies.append((firstX + (stepX * 13), firstY - (stepY * 12)))

        #eleventh
        self.coordinateForEnemies.append((firstX - (stepX * 12), firstY - (stepY * 16)))
        self.coordinateForEnemies.append((firstX - (stepX * 7), firstY - (stepY * 16)))
        self.coordinateForEnemies.append((firstX - (stepX * 1), firstY - (stepY * 16)))
        self.coordinateForEnemies.append((firstX + (stepX * 2), firstY - (stepY * 16)))
        self.coordinateForEnemies.append((firstX + (stepX * 8), firstY - (stepY * 16)))
        self.coordinateForEnemies.append((firstX + (stepX * 13), firstY - (stepY * 16)))
        '''for i in range(62):
            if 0 <= i < 6:
                if i == 0:
                    self.coordinateForEnemies.append((firstX, firstY))
                elif i == 1:
                    self.coordinateForEnemies.append((firstX + (stepX*5), firstY))
                elif i == 2:
                    self.coordinateForEnemies.append((firstX + (stepX*11), firstY))
                elif i == 3:
                    self.coordinateForEnemies.append((firstX + (stepX*14), firstY))
                elif i == 4:
                    self.coordinateForEnemies.append((firstX + (stepX*20), firstY))
                elif i == 5:
                    self.coordinateForEnemies.append((firstX + (stepX*25), firstY))
            elif 6 <= i < 14:
                if i == 6:
                    self.coordinateForEnemies.append((firstX, firstY + (stepY*4)))
                elif i == 7:
                    self.coordinateForEnemies.append((firstX + (stepX*5), firstY + (stepY*4)))
                elif i == 8:
                    self.coordinateForEnemies.append((firstX + (stepX*8), firstY + (stepY*4)))
                elif i == 9:
                    self.coordinateForEnemies.append((firstX + (stepX*11), firstY + (stepY*4)))
                elif i == 10:
                    self.coordinateForEnemies.append((firstX + (stepX*14), firstY + (stepY*4)))
                elif i == 11:
                    self.coordinateForEnemies.append((firstX + (stepX*17), firstY + (stepY*4)))
                elif i == 12:
                    self.coordinateForEnemies.append((firstX + (stepX*20), firstY + (stepY*4)))
                elif i == 13:
                    self.coordinateForEnemies.append((firstX + (stepX*25), firstY + (stepY*4)))
            elif 14 <= i < 22:
                if i == 14:
                    self.coordinateForEnemies.append((firstX, firstY + (stepY*7)))
                elif i == 15:
                    self.coordinateForEnemies.append((firstX + (stepX*5), firstY + (stepY*7)))
                elif i == 16:
                    self.coordinateForEnemies.append((firstX + (stepX*8), firstY + (stepY*7)))
                elif i == 17:
                    self.coordinateForEnemies.append((firstX + (stepX*11), firstY + (stepY*7)))
                elif i == 18:
                    self.coordinateForEnemies.append((firstX + (stepX*14), firstY + (stepY*7)))
                elif i == 19:
                    self.coordinateForEnemies.append((firstX + (stepX*17), firstY + (stepY*7)))
                elif i == 20:
                    self.coordinateForEnemies.append((firstX + (stepX*20), firstY + (stepY*7)))
                elif i == 21:
                    self.coordinateForEnemies.append((firstX + (stepX*25), firstY + (stepY*7)))
            elif 22 <= i < 28:
                if i == 22:
                    self.coordinateForEnemies.append((firstX + (stepX*8), firstY + (stepY*10)))
                elif i == 23:
                    self.coordinateForEnemies.append((firstX + (stepX*11), firstY + (stepY*10)))
                elif i == 24:
                    self.coordinateForEnemies.append((firstX + (stepX*12), firstY + (stepY*10)))
                elif i == 25:
                    self.coordinateForEnemies.append((firstX + (stepX*13), firstY + (stepY*10)))
                elif i == 26:
                    self.coordinateForEnemies.append((firstX + (stepX*14), firstY + (stepY*10)))
                elif i == 27:
                    self.coordinateForEnemies.append((firstX + (stepX*17), firstY + (stepY*10)))
            elif 28 <= i < 30:
                if i == 28:
                    self.coordinateForEnemies.append((firstX + (stepX * 10), firstY + (stepY*12)))
                elif i == 29:
                    self.coordinateForEnemies.append((firstX + (stepX * 15), firstY + (stepY*12)))
            elif 30 <= i < 32:
                if i == 30:
                    self.coordinateForEnemies.append((firstX + (stepX * 5), firstY + (stepY * 13)))
                elif i == 31:
                    self.coordinateForEnemies.append((firstX + (stepX * 20), firstY + (stepY * 13)))
            elif 32 <= i < 34:
                if i == 32:
                    self.coordinateForEnemies.append((firstX + (stepX * 10), firstY + (stepY * 14)))
                elif i == 33:
                    self.coordinateForEnemies.append((firstX + (stepX * 15), firstY + (stepY * 14)))
            elif 34 <= i < 40:
                if i == 34:
                    self.coordinateForEnemies.append((firstX + (stepX * 8), firstY + (stepY * 16)))
                elif i == 35:
                    self.coordinateForEnemies.append((firstX + (stepX * 11), firstY + (stepY * 16)))
                elif i == 36:
                    self.coordinateForEnemies.append((firstX + (stepX * 12), firstY + (stepY * 16)))
                elif i == 37:
                    self.coordinateForEnemies.append((firstX + (stepX * 13), firstY + (stepY * 16)))
                elif i == 38:
                    self.coordinateForEnemies.append((firstX + (stepX * 14), firstY + (stepY * 16)))
                elif i == 39:
                    self.coordinateForEnemies.append((firstX + (stepX * 17), firstY + (stepY * 16)))
            elif 40 <= i < 48:
                if i == 40:
                    self.coordinateForEnemies.append((firstX + (stepX * 5), firstY + (stepY * 19)))
                elif i == 41:
                    self.coordinateForEnemies.append((firstX + (stepX * 5), firstY + (stepY * 19)))
                elif i == 42:
                    self.coordinateForEnemies.append((firstX + (stepX * 8), firstY + (stepY * 19)))
                elif i == 43:
                    self.coordinateForEnemies.append((firstX + (stepX * 11), firstY + (stepY * 19)))
                elif i == 44:
                    self.coordinateForEnemies.append((firstX + (stepX * 14), firstY + (stepY * 19)))
                elif i == 45:
                    self.coordinateForEnemies.append((firstX + (stepX * 17), firstY + (stepY * 19)))
                elif i == 46:
                    self.coordinateForEnemies.append((firstX + (stepX * 20), firstY + (stepY * 19)))
                elif i == 47:
                    self.coordinateForEnemies.append((firstX + (stepX * 25), firstY + (stepY * 19)))
            elif 48 <= i < 56:
                if i == 48:
                    self.coordinateForEnemies.append((firstX, firstY + (stepY * 22)))
                elif i == 49:
                    self.coordinateForEnemies.append((firstX + (stepX * 5), firstY + (stepY * 22)))
                elif i == 50:
                    self.coordinateForEnemies.append((firstX + (stepX * 8), firstY + (stepY * 22)))
                elif i == 51:
                    self.coordinateForEnemies.append((firstX + (stepX * 11), firstY + (stepY * 22)))
                elif i == 52:
                    self.coordinateForEnemies.append((firstX + (stepX * 14), firstY + (stepY * 22)))
                elif i == 53:
                    self.coordinateForEnemies.append((firstX + (stepX * 17), firstY + (stepY * 22)))
                elif i == 54:
                    self.coordinateForEnemies.append((firstX + (stepX * 20), firstY + (stepY * 22)))
                elif i == 55:
                    self.coordinateForEnemies.append((firstX + (stepX * 25), firstY + (stepY * 22)))
            elif 56 <= i < 62:
                if i == 56:
                    self.coordinateForEnemies.append((firstX, firstY + (stepY*26)))
                elif i == 57:
                    self.coordinateForEnemies.append((firstX + (stepX * 5), firstY + (stepY*26)))
                elif i == 58:
                    self.coordinateForEnemies.append((firstX + (stepX * 11), firstY + (stepY*26)))
                elif i == 59:
                    self.coordinateForEnemies.append((firstX + (stepX * 14), firstY + (stepY*26)))
                elif i == 60:
                    self.coordinateForEnemies.append((firstX + (stepX * 20), firstY + (stepY*26)))
                elif i == 61:
                    self.coordinateForEnemies.append((firstX + (stepX * 25), firstY + (stepY*26)))'''
        # print(self.coordinateForEnemies)


# e = Enemy()