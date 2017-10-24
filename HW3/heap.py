#!/usr/bin/env python3
import random
import tracked_list
import pydot
import pdb


def validate(heap):
    for i in range(len(heap)):
        if heap[i] > heap[i // 2]:
            return False
    return True


def cmp(a, b, descending=False):
    if descending:
        return a > b
    else:
        return b < a


def heapify(l):
    # for i in range(len(l)):
    #     k = i
    #     while cmp(l[k], l[k // 2], descending):
    #         l.swap(k, k // 2)
    #         k = k // 2
    # print(l)
    start = i_parent(len(l) - 1)
    while start >= 0:
        sink(l, start)
        start -= 1


def i_left_child(parent):
    return 2 * parent + 1


def i_right_child(parent):
    return 2 * parent + 2


def i_parent(i_child):
    return (i_child - 1) // 2


def sink(l, i, end=None):
    if end is None:
        end = len(l) - 1
    root = i
    # pdb.set_trace()
    while i_left_child(root) <= end:
        child = i_left_child(root)
        swap = root
        lswap = l[swap]
        lchild = l[child]
        try:
            if lswap < lchild:
                swap = child
        except IndexError as e:
            print("swap {} child {} {}".format(swap, child, len(l)))
            raise e
        if child + 1 <= end and lswap < l[child + 1]:
            swap = child + 1
        if swap == root:
            return
        else:
            l.swap(root, swap)
            root = swap


def sort(l):
    heapify(l)
    end = len(l) - 1
    while end > 0:
        l.swap(0, end)
        end -= 1
        sink(l, 0, end)


def profile(n, N):
    n = 31
    myheap = tracked_list.TrackedList(range(n))
    random.shuffle(myheap)
    heapify(myheap)
    myheap.history = []
    # print(myheap.history)
    # print(myheap, validate(myheap))
    s = 0
    N = 100
    for _ in range(N):
        myheap.history = []
        random.shuffle(myheap)
        heapify(myheap)
        s += len(myheap.history)
        if not validate(myheap):
            raise ValueError("ALGO ERROR!")
    return s / N


def main():
    N = 14
    # print("Avg. ops to heapify list of length {}: {}".format(n, profile(n, N)))
    for n in range(N):
        myheap = tracked_list.TrackedList(range(int(2**n)))
        myheap.history = []
        random.shuffle(myheap)
        myheap.history = []
        heapify(myheap)
        sort(myheap)
        print(2**n, len(myheap.history), sep='\t')

    g = pydot.Dot(graph_type="digraph")
    for i in range(1, len(myheap)):
        g.add_edge(pydot.Edge(myheap[(i + 1) // 2 - 1], myheap[i]))
    # print(myheap)
    # print(myheap)

    g.write_png("graph.png")
if __name__ == '__main__':
    main()
