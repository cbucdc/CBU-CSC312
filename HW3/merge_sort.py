#!/usr/bin/env python3
import random
import tracked_list
import pdb


def sort(l):
    pass


def merge(l, i1, f1, i2, f2):
    # pdb.set_trace()
    c1, c2 = i1, i2
    while c1 < f1 or c2 < f2 and c1 < c2:
        print(c1, c2)
        a, b = l[c1], l[c2]
        if min(a, b) == b:
            l.swap(l[c1], l[c2])
            c1 += 1
            c2 += 1
            print("swap")
        elif max(a, b) == b:
            c2 += 1


def main():
    l = tracked_list.TrackedList(range(10))
    mid = len(l) // 2
    b = l[mid:]
    a = l[:mid]
    ll = tracked_list.TrackedList(b + a)
    print(ll)
    try:
        merge(ll, 0, mid, mid, len(ll))
    except IndexError as e:
        print(e)
        print(ll)
        quit()
    print(ll,)
    random.shuffle(l)
    l.history = []


if __name__ == '__main__':
    main()
