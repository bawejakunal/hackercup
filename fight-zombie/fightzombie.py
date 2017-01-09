#!/bin/python
"""
Python v2.7.12
@author: Kunal Baweja
Facebook Hackercup 2017 - Qualification Round
Fighting-the-Zombie: https://www.facebook.com/hackercup/problem/326053454264498/
"""

def parse_spell(spell):
    """
    @spell: spell description
    """
    Z = 0

    parse = spell.split('+')
    if len(parse) > 1:
        Z = int(parse[1])

    else:
        parse = spell.split('-')
        if len(parse) > 1:
            Z = 0 - int(parse[1])

    parse = parse[0].split('d')
    X, Y = map(int, parse)

    return (X, Y, Z)

def get_score_count(number, sides, target):
    """
    count number of ways to get at least target
    score
    """
    total = 0
    maxscore = number * sides
    table = [[0] * (maxscore + 1) for _ in xrange(number + 1)]

    #fill table for first dice roll
    for i in xrange(1, min(maxscore + 1, sides + 1)):
        table[1][i] = 1

    #fill table for rest of entries in table
    for dice in xrange(2, number + 1):
        for _score in xrange(1, maxscore + 1):
            for side in xrange(1, min(maxscore + 1, sides + 1)):
                table[dice][_score] += table[dice - 1][_score - side]

    #sum of ways to get score in [target, maxscore] with given dice
    for i in xrange(target, maxscore + 1):
        total += table[number][i]

    return total


def count_possible(number, sides, target):
    """
    @number: number of dice
    @sides: sides in a dice
    @target: target minimum score
    count possible rolls where score is achieved
    """

    count = 0

    #minmum possible is greater than target
    if number >= target:
        count = sides ** number

    #no dice or maximum value less than target score
    elif number == 0 or target > (sides * number):
        count = 0

    else:
        count = get_score_count(number, sides, target)

    return count


def get_prob(spell, H):
    """
    get probability of spell
    """
    X, Y, Z = parse_spell(spell)
    total = float(Y ** X)
    feasible = 0
    feasible = count_possible(X, Y, H - Z)

    return feasible / total


def main():
    """
    read input, print output
    """
    T = int(raw_input().strip())

    for zombie in xrange(1, T + 1):
        H, S = map(int, raw_input().strip().split())
        spells = raw_input().strip().split()

        prob = 0.0
        for spell in spells:
            prob = max(prob, get_prob(spell, H))

        print "Case #%d: %.6f" % (zombie, prob)


if __name__ == '__main__':
    main()
