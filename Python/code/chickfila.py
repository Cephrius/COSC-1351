
def buyOrNot(num):
    if num < 6:
        print(f"It is possible to buy {num} nuggets")
    elif num % 6 == 0 or num % 9 == 0 or num % 20 == 0:
        print(f"It is possible to buy {num} nuggets")
    else:
        print("It is not possible to order")

buyOrNot(12)


def make_bricks(small, big, goal):
    if goal > big*5 + small:
        return False
    elif small > 0 and make_bricks(small - 1, big, goal - 1):
        return True
    elif big > 0 and make_bricks(small , big - 1, goal - 5):
        return True
    return False
def make_bricks(small, big, goal):
    if goal > big * 5 + small:
        return False

    elif goal:
        return False

    return True
