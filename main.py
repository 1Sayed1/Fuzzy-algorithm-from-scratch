"""""
This function will take a list of membership degrees in
each fuzzy set and a list of the corresponding fuzzy sets. Then, the function
should defuzzify these memberships and return a crisp value.

"""""


def defuzzify(memberships, fuzzySets):
    pred = 0
    for i in range(len(memberships)):
        centroid = sum(memberships[i]) / len(memberships[i])
        pred += centroid * fuzzySets[i]
    crispOutput = pred / sum(fuzzySets)
    return crispOutput


#########################################################

"""""
This function
will take a list of fuzzy sets (each fuzzy set is an inner list) and a crisp value.
Then, the function should fuzzify this crisp value and return a list of membership
degrees.

"""""


def fuzzify(fuzzySets, crispValue):
    memberships = []

    for s in range(len(fuzzySets)):
        f = 0
        index = 0
        if len(fuzzySets[s]) == 3:
            for i in range(3):
                if fuzzySets[s][i] == crispValue:
                    f = 1
                    index = i
                    break
                elif fuzzySets[s][i] > crispValue:
                    f = 2
                    index = i
                    break
            if f == 0:
                memberships.append(0)
            elif f == 1:
                if index == 1:
                    memberships.append(1)
                else:
                    memberships.append(0)
            elif f == 2:
                if index == 1:
                    x1 = fuzzySets[s][index]
                    y1 = index
                    x2 = fuzzySets[s][index - 1]
                    y2 = index - 1
                    m = (y1 - y2) / (x1 - x2)

                    b = y1 - (m * x1)
                    memberships.append((m * crispValue) + b)
                elif index == 2:
                    x1 = fuzzySets[s][index]
                    y1 = 0
                    x2 = fuzzySets[s][index - 1]
                    y2 = index - 1
                    m = (y1 - y2) / (x1 - x2)

                    b = y1 - (m * x1)
                    memberships.append((m * crispValue) + b)

                else:
                    memberships.append(0)

        elif len(fuzzySets[s]) == 4:
            for i in range(4):
                if fuzzySets[s][i] == crispValue:
                    f = 1
                    index = i
                    break
                elif fuzzySets[s][i] > crispValue:
                    f = 2
                    index = i
                    break
            if f == 0:
                memberships.append(0)
            elif f == 1:
                if index == 1 or index == 2:
                    memberships.append(1)
                else:
                    memberships.append(0)
            elif f == 2:
                if index == 1:
                    x1 = fuzzySets[s][index]
                    y1 = index
                    x2 = fuzzySets[s][index - 1]
                    y2 = index - 1
                    m = (y1 - y2) / (x1 - x2)
                    b = y1 - (m * x1)
                    memberships.append((m * crispValue) + b)
                elif index == 2:
                    memberships.append(1)
                elif index == 3:
                    x1 = fuzzySets[s][index]
                    y1 = 0
                    x2 = fuzzySets[s][index - 1]
                    y2 = 1
                    m = (y1 - y2) / (x1 - x2)
                    b = y1 - (m * x1)
                    memberships.append((m * crispValue) + b)
                else:
                    memberships.append(0)

    return memberships


#############################################################
Age = [[0, 0, 21, 40], [40, 49, 59], [59, 69, 70], [70, 79, 80, 89]]
AgeList = fuzzify(Age, 79)

BP = [[0, 0, 75, 90], [90, 100, 120], [120, 163, 200, 200]]
BPList = fuzzify(BP, 163)

Cholesterol = [[0, 0, 50, 200], [190, 215, 239], [240, 265, 320], [280, 365, 500, 500]]
CholesterolList = fuzzify(Cholesterol, 365)

Diabetes = [[0, 70, 199], [199, 230, 400]]
DiabetesList = fuzzify(Diabetes, 230)

BMI = [[0, 0, 11, 18.5], [18.5, 20, 24.9], [24, 27, 30], [30, 35, 40, 40]]
BMIList = fuzzify(BMI, 35)


# Rule_1
Rule1List = [AgeList[1], BPList[1], CholesterolList[0], DiabetesList[0], BMIList[1]]
Rule_1 = min(Rule1List)

# Rule_2
Rule2List = [AgeList[2], BPList[1], CholesterolList[1], DiabetesList[0], BMIList[2]]
Rule_2 = min(Rule2List)

# Rule_3
Rule3List = [AgeList[0], BPList[1], CholesterolList[1], DiabetesList[0], BMIList[2]]
Rule_3 = min(Rule3List)

#Rule123
Rule123 = max(Rule_1, Rule_2, Rule_3)

# Rule_4
Rule4List = [AgeList[2], BPList[2], CholesterolList[3], DiabetesList[1], BMIList[3]]
Rule_4 = min(Rule4List)

# Rule_5
Rule5List = [AgeList[3], BPList[2], CholesterolList[2], DiabetesList[0], BMIList[3]]
Rule_5 = min(Rule5List)

#Rule45
Rule45 = max(Rule_4, Rule_5)

# Rule_6
Rule6List = [AgeList[3], BPList[2], CholesterolList[3], DiabetesList[1], BMIList[3]]
Rule_6 = min(Rule6List)


Health = [[0, 0, 0.3, 1.7], [1.5, 2, 2.5], [2.4, 3, 4, 4]]
fanMemDegrees = [Rule123, Rule45, Rule_6]

print(defuzzify(Health, fanMemDegrees))
