#! /usr/bin/env python3
import sys

def answer(stones):
    whites, blacks = 0,0
    for stone in stones:
        if stone == "W":
            whites += 1
        else:
            blacks += 1

    if whites > blacks or blacks > whites:
        return 0
    else:
        return 1
   
def solve():
    stones = str(input())
    print(answer(stones))

def test():
    assert answer("WWWWWWWWWWWB") == 0
    assert answer("BBBBBBBBBBBW") == 0
    assert answer("WBWBWBWBWBWB") == 1
    assert answer("WWWWWBBBBB") == 1
    print("all test cases passed...")
   
if __name__=="__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
