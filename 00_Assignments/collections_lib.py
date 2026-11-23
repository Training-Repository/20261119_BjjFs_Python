"""Collections library: model submission for the SimpleList assignment (Stages 1-4)."""


# ---------------------------------------------------------------- Stage 1
class SimpleList:
    def __init__(self, items):
        print("In SimpleList ctor")
        self.items = list(items)

    def add(self, item):
        self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]

    def sort(self):
        self.items.sort()

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"{type(self).__name__}({self.items!r})"


# ---------------------------------------------------------------- Stage 2
class SortedList(SimpleList):
    def __init__(self, items):
        print("In SortedList ctor")
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()


# ---------------------------------------------------------------- Stage 3
class IntList(SimpleList):
    def __init__(self, items=()):
        print("In IntList ctor")
        for x in items:
            self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)


# ---------------------------------------------------------------- Stage 4
class SortedIntList(IntList, SortedList):
    def __init__(self, items=()):
        print("In SortedIntList ctor")
        super().__init__(items)




# ---------------------------------------------------------------- Stage tests
def stage1_tests():
    refunds = [4500, 1200, 9800]
    sl = SimpleList(refunds)
    refunds.append(0)            # changing the source list must not affect sl
    sl.add(3000)
    print(sl)
    print(len(sl), sl[0], sl[-1])
    sl.sort()
    print(sl)
    print(sl[1:3])
    print([x // 100 for x in sl])
    print(3000 in sl, 7 in sl)
    print(SimpleList(()), SimpleList(range(3)))


def stage2_tests():
    s = SortedList([4500, 1200, 9800])
    print(s)
    s.add(3000)
    s.add(100)
    print(s, len(s))
    print(s[0], s[-1])           # lowest and highest refund
    print(SortedList(('ICICI', 'BFL', 'HDFC')))
    try:
        SortedList([3, '1'])
    except TypeError as e:
        print('TypeError:', e)


def stage3_tests():
    il = IntList()
    print(il, len(il))
    il.add(250)
    il.add(-75)                  # reversals are negative
    print(il)
    for bad in ([10, 20, '30'], [10, 2.5]):
        try:
            IntList(bad)
        except TypeError as e:
            print('Rejected:', e)
    try:
        il.add('100')
    except TypeError as e:
        print('Rejected:', e)
    print(il)                    # unchanged after the rejected add


def main():
    try:
        sil = SortedIntList([42, 23, 3])
        sil.add(-1234)
        print(sil)
    except BaseException as e:
        print(type(e), e)

    try:
        sil2 = SortedIntList([3, 2, '1'])
    except BaseException as e:
        print(type(e), e)

    try:
        sil = SortedIntList([42, 23, 3])
        sil.add('Something new')
    except BaseException as e:
        print(type(e), e)


if __name__ == '__main__':
    stage1_tests()
    stage2_tests()
    stage3_tests()
    print([c.__name__ for c in SortedIntList.__mro__])
    main()

    # IntList()

    # obj = SortedIntList((45, 21, 3))
    # print(f"{obj.__class__.__bases__ = }")
    # print(f"{obj.__class__.__mro__ = }")



# ANSWERS
# R1: __getitem__. Without __iter__, Python iterates by calling __getitem__(0), (1), ... until
#     IndexError; `in` falls back to that same iteration.
# R2: The error comes from list.sort() comparing str with int; it names neither the collection
#     nor the bad value, and appears only at sort time, far from where the data came in.
# R3: The check needs no instance data, so it is static. Calling it as self._validate lets a
#     subclass override the rule; a module-level function could not be overridden per class.
# R4: IntList.__init__ (validate) -> SortedList.__init__ -> SimpleList.__init__ (copy), then
#     SortedList sorts. super() follows the MRO of SortedIntList, where IntList is followed by SortedList.
# R5: IntList.add (validate) -> SortedList.add -> SimpleList.add (append), then SortedList.add sorts.
# R6: "<class 'TypeError'> '<' not supported between instances of 'str' and 'int'": super() reaches
#     SortedList, which sorts the mixed list before IntList validates. Validate before delegating.
# R7: MRO becomes SortedIntList, SortedList, IntList, SimpleList, object; output is unchanged, because
#     IntList works before super() and SortedList works after it, whichever is listed first.
