#!/bin/python
"""
Python v2.7.12
@author: Kunal Baweja
Facebook Hackercup 2017 - Qualification Round
Lazy-Loading: https://www.facebook.com/hackercup/problem/169401886867367/
"""

from math import ceil

def count_trips(weight, length):
    """
    @weight: list of weights of items
    count maximum trips lazy worker can make

    On every day, it is guaranteed that the total weight of all of the items
    is at least 50 pounds.
    """
    capacity = 50.0
    left = count = 0
    right = length - 1

    weight.sort()

    while left < right:

        #number of items required other than heaviest
        required = int(ceil((capacity - weight[right]) / weight[right]))
        left += required

        """
        if sufficient items then increment count otherwise we need to include
        items in other trips and can not count them in a separate trip
        """
        if left <= right:
            count += 1
        right -= 1

    return count


def main():
    """
    read Input, print output
    """
    T = int(raw_input().strip())

    for test in xrange(1, T + 1):
        N = int(raw_input().strip())
        weight = list()

        for _ in xrange(N):
            weight.append(int(raw_input().strip()))

        trips = count_trips(weight, N)
        print "Case #%d: %d" % (test, trips)


if __name__ == '__main__':
    main()
