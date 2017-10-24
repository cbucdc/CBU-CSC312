import random


def myhash(n):
    return n % 10


def sort(l):
    table = [[] for _ in range(10)]
    # sort by last digit
    for i in l[::-1]:
        table[myhash(i)].append(i)
        l.pop()
    print(table)
    for n in table:
        for i in n:
            l.append(i)


def main():
    l = [random.choice(range(1000)) for i in range(100)]
    random.shuffle(l)
    print(l)
    sort(l)
    print(l)


if __name__ == '__main__':
    main()
