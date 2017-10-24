import random
import tracked_list


def partition(l, start, end):
    pivot = l[start]
    c1 = start
    c2 = end
    while True:
        # locate an inverted pair by moving c1 and c2
        while l[c1] < pivot:
            c1 += 1
        while l[c2] > pivot:
            c2 -= 1
        if c1 >= c2:
            return c2
        l.swap(c1, c2)


def sort_in_place(l, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(l) - 1
    if len(l) == 0:
        return l
    elif start < end:
        p = partition(l, start, end)
        sort_in_place(l, start, p)
        sort_in_place(l, p + 1, end)


def main():
    l = tracked_list.TrackedList(range(10))
    total = 0
    N = 1000
    for _ in range(N):
        random.shuffle(l)
        # print(l)
        sort_in_place(l)
        total += len(l.history)
        l.history = []
    print(total / N)
    # print(l)
if __name__ == '__main__':
    main()
