import random


class Get:

    def __init__(self, index):
        self.index = index

    def __repr__(self):
        return "Get({})".format(self.index)


class Swap:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __repr__(self):
        return "Swap({},{})".format(self.i, self.j)


class TrackedList(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hist = []

    def swap(self, i1, i2):
        self.hist.append(Swap(i1, i2))
        self[i1], self[i2] = self[i2], self[i1]

    def __getitem__(self, index):
        self.hist.append(Get(index))
        return super().__getitem__(index)

    @property
    def history(self):
        return tuple(self.hist[:])

    @history.setter
    def history(self, data):
        if not isinstance(data, list):
            raise ValueError("history must be list")
        else:
            self.hist = data[:]


def main():
    l = TrackedList(range(10))

    print(l)
    random.shuffle(l)
    print(len(l.history), "operations: ", l.history)

if __name__ == '__main__':
    main()
