# In the domain of converging journeys, numbers progress based on a unique formula. Specifically, following n is n plus the sum of its digits. For example, 12345 is followed by 12360, since 1+2+3+4+5 = 15. If the first number is k we will call it journey k.

# For example, journey 480 is the sequence beginning {480, 492, 507, 519, ...} and journey 483 is the sequence beginning {483, 498, 519, ...}.

# People may cross paths in their lives, and this happens when two journeys share some of the same values. For example: journey 480 meets journey 483 at 519, meets journey 507 at 507, and never meets journey 481.

# Every journey will eventually meet journey 1, journey 3 or journey 9. Write a program which inputs a single integer n (1 ≤ n ≤ 16384), and outputs the value where journey n first meets one of these three journeys.


def converging_journeys(n):
    journeys = [1, 3, 9]
    for i in journeys:
        common_element = compare_journeys(journey(i), journey(n))
        if common_element is not None:
            return((i, common_element))

def journey(number):
    converging = [number]
    while 1 <= number <= 50000:
        digits = [int(digit) for digit in str(number)]
        k = number + sum(digits)
        converging.append(k)
        number = k

    return converging

def compare_journeys(j1, j2):
    for i in j1:
        if i in j2:
            return i
    return None
