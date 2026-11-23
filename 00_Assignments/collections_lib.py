# -----------------------------------------------Stage 1
class SimpleList:
    pass

# -----------------------------------------------Stage 2
class SortedList(SimpleList):
    pass

# -----------------------------------------------Stage 3
class IntList(SimpleList):
    pass

# -----------------------------------------------Stage 4
class SortedIntList(IntList, SortedList):
    pass


# -----------------------------------------------Stage tests

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
