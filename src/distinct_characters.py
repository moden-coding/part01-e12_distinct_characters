#!/usr/bin/env python3

def distinct_characters(L):
    result = {}
    for x in L:
        result[x] = len(set(x))

    return result

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
