# lotto.py
# @rslarkin

import random


def main():
    # roll lotto numbers and bonus number
    num1 = random.randrange(1, 100)
    num2 = random.randrange(1, 100)
    num3 = random.randrange(1, 100)
    num4 = random.randrange(1, 100)
    num5 = random.randrange(1, 100)
    num6 = random.randrange(1, 100)
    num7 = random.randrange(1, 100)
    bonuslotto = [num7]

    # make sure no numbers are identical with the exception of the bonus number
    if (num1 == num2) or (num1 == num3) or (num1 == num4) or (num1 == num5) or (num1 == num6):
        num1 = random.randrange(1, 100)
    if (num2 == num1) or (num2 == num3) or (num2 == num4) or (num2 == num5) or (num2 == num6):
        num2 = random.randrange(1, 100)
    if (num3 == num1) or (num3 == num2) or (num3 == num4) or (num3 == num5) or (num3 == num6):
        num3 = random.randrange(1, 100)
    if (num4 == num1) or (num4 == num2) or (num4 == num3) or (num4 == num5) or (num4 == num6):
        num4 = random.randrange(1, 100)
    if (num5 == num1) or (num5 == num2) or (num5 == num3) or (num5 == num4) or (num5 == num6):
        num5 = random.randrange(1, 100)
    if (num6 == num1) or (num6 == num2) or (num6 == num3) or (num6 == num4) or (num6 == num5):
        num6 = random.randrange(1, 100)

    # sort the numbers except the bonus number - always last
    lotto = sorted([num1, num2, num3, num4, num5, num6])
    # print the numbers
    print(lotto, bonuslotto)


main()
