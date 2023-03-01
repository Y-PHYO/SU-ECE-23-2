import math
import cmath


def findGears(R1, R2, R3,d_12, d_13, known_d12, known_d13, x1_ref, y1_ref, x2_ref, y2_ref, x3_ref, y3_ref):
    if math.isclose(d_12, known_d12, rel_tol=0.1):
        # print("d12 is between the back landing gears")
        if math.isclose(d_13, known_d13, rel_tol=0.1):  # Robot is closer to  right wing
            # print("d13 is between the front and back landing gears.")
            X1, Y1 = x1_ref, y1_ref
            X2, Y2 = x2_ref, y2_ref
            X3, Y3 = x3_ref, y3_ref
            return X1, Y1, X2, Y2, X3, Y3
    elif math.isclose(d_12, known_d13, rel_tol=0.1):
        # print("d12 is between the front and back landing gears")
        if math.isclose(d_13, known_d12, rel_tol=0.1):  # Robot closer to left wing
            # print("d13 is the back landing gears")
            X1, Y1 = x2_ref, y2_ref
            X2, Y2 = x3_ref, y3_ref
            X3, Y3 = x1_ref, y1_ref
            return X1, Y1, X2, Y2, X3, Y3
        elif math.isclose(d_13, known_d13, rel_tol=0.1):
            if R1 > R2 and R1 > R3:  # Robot is closer to back of plane
                # print("d13 is between the front and back landing gears.")
                X1, Y1 = x3_ref, y3_ref
                X2, Y2 = x1_ref, y1_ref
                X3, Y3 = x2_ref, y2_ref
                return X1, Y1, X2, Y2, X3, Y3
            elif R1 < R2 and R1 < R3:  # Robot is closer to front of plane
                # print("Front of Plane")
                X1, Y1 = x3_ref, y3_ref
                X2, Y2 = x2_ref, y2_ref
                X3, Y3 = x1_ref, y1_ref
                return X1, Y1, X2, Y2, X3, Y3
            else:
                print("Move somewhere else")
        else:
            print("Move somewhere else")
    else:
        print("Move somewhere else")


def degtorad(degrees):
    return math.radians(degrees)


def squared(value):
    return round(value * value, 4)


def cos(val):
    return round(math.cos(val), 4)


def distance(X1, Y1, X2, Y2):
    a = X1 - X2
    b = Y1 - Y2
    c_2 = squared(a) + squared(b)
    return math.sqrt(c_2)


def lawOfCosines(r1, r2, angle):
    return round(math.sqrt(squared(r1) + squared(r2) - (2 * r1 * r2) * cos(angle)), 4)


def findcoeff(X1, Y1, X2, Y2, r1, r2):
    a_top = -squared(X2) + squared(X1) - squared(Y2) + squared(Y1) + squared(r2) - squared(r1)
    a_bot = 2 * (X1 - X2)
    a = a_top / a_bot

    b_top = 2 * (Y1 - Y2)
    b_bot = 2 * (X1 - X2)
    b = b_top / b_bot

    return a, b


def findquadCo(X1, Y1, r1, a, b):
    aq = squared(b) + 1
    bq = (-2 * b) * (a - X1) + -2 * Y1
    cq = squared(a) - (2 * X1 * a) + squared(X1) + squared(Y1) - squared(r1)

    return aq, bq, cq


def solveYSpecial(X1, Y1, X2, Y2, r1, r2):
    y_top = -squared(r2) + squared(r1)
    y_bottom = -2 * Y1 + 2 * Y2

    y = y_top / y_bottom

    return y


def quadEq(a, b, c):
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)

    # print('The solutions are {:.4f} and {:.4f}'.format(sol1, sol2))

    return sol1, sol2


def checkDistance(dCalc, dCos):
    if math.isclose(dCalc, dCos, rel_tol=0.01):
        # print("Close enough")
        return True
    else:
        return False


def solveX(a, b, y):
    x = a - b * y
    return x


def findAllSols(X1, Y1, X2, Y2, r1, r2):
    a, b = findcoeff(X1, Y1, X2, Y2, r1, r2)

    # print(a, b)

    A, B, C = findquadCo(X1, Y1, r1, a, b)
    # print(A, B, C)

    y_sol1, y_sol2 = quadEq(A, B, C)

    y_sol1 = round(y_sol1, 4)
    y_sol2 = round(y_sol2, 4)

    # print(y_sol1, y_sol2)

    x_sol1 = solveX(a, b, y_sol1)
    x_sol2 = solveX(a, b, y_sol2)

    # print(x_sol1, y_sol1)
    # print(x_sol2, y_sol2)
    return x_sol1, y_sol1, x_sol2, y_sol2


def solveCircles(r1, r2, angle, X1, Y1, X2, Y2):

    dCalc = distance(X1, Y1, X2, Y2)

    dCos = lawOfCosines(r1, r2, angle)

    if checkDistance(dCalc, dCos) == True:
        # print("Distance: {:.4f} meters".format(dCalc))
        if X1 == X2 and abs(Y1) == abs(Y2):
            y = solveYSpecial(X1, Y1, X2, Y2, r1, r2)

            # print(y)

            a = 1
            b = -2 * X1
            c = squared(X1) + squared(y) - 2 * Y1 * y + squared(Y1) - squared(r1)

            x1_solve, x2_solve = quadEq(a, b, c)

            # print("Solution 1: {:.4f}, {:.4f}".format(x1_solve, y))
            # print("Solution 2: {:.4f}, {:.4f}".format(x2_solve, y))

            yother = y

            return x1_solve, y, x2_solve, yother
        else:
            x2s, y2s, x3s, y3s = findAllSols(X1, Y1, X2, Y2, r1, r2)
            # print("Solution 1: {:.4f}, {:.4f}".format(x2s, y2s))
            # print("Solution 2: {:.4f}, {:.4f}".format(x3s, y3s))
            return x2s, y2s, x3s, y3s

    else:
        print("Error solving circles")


def assignGears(x1_ref, y1_ref, x2_ref, y2_ref, x3_ref, y3_ref, r1, r2, r3, theta12, theta13):
    knownD12 = distance(x1_ref, y1_ref, x2_ref, y2_ref)  # back landing gears
    knownD13 = distance(x1_ref, y1_ref, x3_ref, y3_ref)  # front to back landing gears
    knownD13 = round(knownD13, 4)

    # print("Distance 1 to 2: {0}\nDistance 1 to 3: {1}\n".format(knownD12, knownD13))

    d12 = lawOfCosines(r1, r2, theta12)
    d13 = lawOfCosines(r1, r3, theta13)

    x1, y1, x2, y2, x3, y3 = findGears(r1, r2,r3, d12, d13, knownD12, knownD13, x1_ref, y1_ref, x2_ref, y2_ref, x3_ref, y3_ref)

    ############################

    return x1, y1, x2, y2, x3, y3


def comparePoints(X1, Y1, X2, Y2, X3, Y3, X4, Y4):
    if (X1, Y1) == (X3, Y3) or (X1, Y1) == (X4, Y4):
        print("{0}, {1} are the correct coordinates".format(X1, Y1))
        return X1, Y1
    elif (X2, Y2) == (X3, Y3) or (X2, Y2) == (X4, Y4):
        print("{0}, {1} are the correct coordinates".format(X2, Y2))
        return X2, Y2
    else:
        print("No matches were found")


def functionName(r1, r2, r3, x_1, y_1, x_2, y_2, x_3, y_3, angle12, angle13):

    theta12 = degtorad(angle12)
    theta13 = degtorad(angle13)

    x1, y1, x2, y2, x3, y3 = assignGears(x_1, y_1, x_2, y_2, x_3, y_3, r1, r2, r3, theta12, theta13)

    x1_, y1_, x2_, y2_ = solveCircles(r1, r2, theta12, x1, y1, x2, y2)

    x3_, y3_, x4_, y4_ = solveCircles(r1, r3, theta13, x1, y1, x3, y3)
    #
    # print(x1_, y1_)
    # print(x2_, y2_)
    # print(x3_, y3_)
    # print(x4_, y4_)
    #
    # print("Split")

    x1_ = round(x1_, 0)
    y1_ = round(y1_, 0)
    x2_ = round(x2_, 0)
    y2_ = round(y2_, 0)
    x3_ = round(x3_, 0)
    y3_ = round(y3_, 0)
    x4_ = round(x4_, 0)
    y4_ = round(y4_, 0)

    # print(x1_, y1_)
    # print(x2_, y2_)
    # print(x3_, y3_)
    # print(x4_, y4_)
    c_x, c_y = comparePoints(x1_, y1_, x2_, y2_, x3_, y3_, x4_, y4_)

    return c_x, c_y
