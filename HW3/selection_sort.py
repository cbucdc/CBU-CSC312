import random
import tracked_list


def sort(mylist: tracked_list.TrackedList):
    for i in range(len(mylist)):
        imin = i
        for j in range(i, len(mylist)):
            if mylist[j] < mylist[imin]:
                imin = j
        mylist.swap(i, imin)


def main():
    l = tracked_list.TrackedList(range(10))

    random.shuffle(l)
    print(l)
    l.history = []
    sort(l)
    print(len(l.history), "operations: ", l.history)


if __name__ == '__main__':
    main()
