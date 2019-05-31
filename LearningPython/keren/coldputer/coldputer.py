#! /usr/bin/env python3
# coldputer science problem in Kattis

import sys

def answer(temperatures):
    # count all the -s in temperatures and return the value
    return temperatures.count('-')
    
def solve():
    n = input()
    #print(n)
    temps = input()
    #print(temps)
    print(answer(temps))

def test():
    assert answer('45353 -34535345 -3452435') == 2
    assert answer('345 43545 45646 -353 -4654 -43545') ==3
    assert answer('-454354, -4545, -454, -355, -5453') == 5
    print('all test cases passed..')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        solve()
