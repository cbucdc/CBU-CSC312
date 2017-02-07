#!/usr/bin/env python3
import random
import tracked_list
import pdb


def sort(l, start=None, stop=None):
    if start is None:
        start = 0
    if stop is None:
        stop = len(l)
    mid = (start + stop) // 2
    length = stop - start

    if length < 2:
        return

    elif length == 2:
        if l[start] > l[stop - 1]:
            l.swap(start, stop - 1)
        return
    else:
        sort(l, start, mid)
        sort(l, mid, stop)
        merge(l, start, mid, mid, stop)
        # print(start, mid, mid, stop)
        return


def merge(l, i1, f1, i2, f2):
    # pdb.set_trace()
    c1, c2 = i1, i2
    # assert f1 - i1 > 1 and f2 - i2 > 1
    # if not (f1 - i1 > 1 and f2 - i2 > 1):
    #     return
    while (c1 < f1 or c2 < f2) and c1 != c2:
        # if c1 >= f1 or c2 >= f2:
        #     break
        print("merge", c1, f1, c2, f2, l)
        a, b = l[c1], l[c2]
        if c1 + 1 == f1:
            c2 += 1
        elif c2 + 1 == f2:
            c2 += 1
        elif a > b:
            l.swap(c1, c2)
        elif c2 - c1 == 1:
            c2 += 1
        elif a < b:
            c1 += 1


def main():
    l = tracked_list.TrackedList(range(10))

    print("merge test")
    mid = len(l) // 2 + 1
    b = l[mid:]
    a = l[:mid]
    ll = tracked_list.TrackedList(b + a)
    # print(ll)
    # merge(ll, 0, mid, mid, len(ll))
    # print(ll)
    ll = tracked_list.TrackedList([1, 3, 2, 4, 5])
    print(ll)
    merge(ll, 0, 3, 3, 5)
    print(ll)

    print("Perform sort")
    random.shuffle(l)
    l.history = []
    sort(l)
    print(l)


if __name__ == '__main__':
    main()
