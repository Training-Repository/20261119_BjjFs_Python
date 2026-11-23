# Assignment: Building a Validated, Sorted Collection — Inheritance and Cooperative `super()`

**Topic:** Classes, special methods, inheritance, multiple inheritance, MRO
**Submission:** one file, `collections_lib.py`, containing all classes, the stage test blocks and an `ANSWERS` comment block at the end
**Rules:**
- Build the stages **in order**. Each stage builds on the classes you already wrote.
- Copy each stage's test block exactly as given and run it. Your output must match the **Expected output** exactly (spacing and punctuation included).
- Use only the Python standard library. Do not import anything.
- Reasoning questions need **1–2 lines** each, written as comments in the `ANSWERS` block.

---

## The scenario

The Collections Analytics team at a consumer-lending NBFC handles many small lists of numbers every day: refund amounts, EMI reversals, days-past-due counts, branch codes. Every analyst writes the same helper code again, so the team asks you to build a small, reusable collection library.

The team lead's plan:

1. Start with a **plain list wrapper** that every later class reuses.
2. Add a version that **always stays sorted**, so the lowest and highest values are always at the ends.
3. Add a version that **accepts integers only**, because amounts are kept in whole rupees and one stray string in a feed can break a report.
4. Finally, combine the two into a **sorted, integer-only list**, without writing any new methods.

---

## Stage 1 — `SimpleList`: the base wrapper

Write a class `SimpleList` that stores its items in an internal Python list named `items`.

**Requirements**

| Member | Behaviour |
|---|---|
| `__init__(self, items)` | Accepts **any iterable** (list, tuple, `range`, …) and stores its **own copy** as a list. Changing the original list afterwards must not affect the object. |
| `add(self, item)` | Appends one item at the end. |
| `__getitem__(self, index)` | Supports indexing, negative indexing and slicing, exactly as a list does. |
| `sort(self)` | Sorts the stored items in place, ascending. |
| `__len__(self)` | Returns the number of items, so `len(obj)` works. |
| `__repr__(self)` | Returns `ClassName([...])`. The class name must come from the **object's actual class**, not be typed in as `"SimpleList"`. Subclasses in later stages must print their own name with no extra code. |

Do **not** write `__iter__` or `__contains__`.

**Test block**

```python
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
```

**Expected output**

```
SimpleList([4500, 1200, 9800, 3000])
4 4500 3000
SimpleList([1200, 3000, 4500, 9800])
[3000, 4500]
[12, 30, 45, 98]
True False
SimpleList([]) SimpleList([0, 1, 2])
```

**Reasoning**
- **R1.** You did not write `__iter__` or `__contains__`, yet the `for` loop and the `in` test both work. Which method makes this possible, and how does Python use it?

---

## Stage 2 — `SortedList`: always sorted

Branch managers want the smallest and largest refund at a glance. Write `SortedList`, a subclass of `SimpleList`, whose items are **always in ascending order**.

**Requirements**
- The list must be sorted as soon as it is created.
- After every `add`, the list must still be sorted.
- Reuse the parent class: call the parent's `__init__` and `add` through `super()`, then sort. Do **not** touch `self.items` directly in this class.
- Do **not** redefine `__getitem__`, `__len__` or `__repr__`. They must work through inheritance.

**Test block**

```python
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
```

**Expected output**

```
SortedList([1200, 4500, 9800])
SortedList([100, 1200, 3000, 4500, 9800]) 5
100 9800
SortedList(['BFL', 'HDFC', 'ICICI'])
TypeError: '<' not supported between instances of 'str' and 'int'
```

**Reasoning**
- **R2.** The last test fails with a message about `'<'` that does not mention your class at all. Why is this message unhelpful to an analyst whose feed contained a stray `'1'`? (This is what Stage 3 fixes.)

---

## Stage 3 — `IntList`: integers only

Amounts are kept in whole rupees. Write `IntList`, a subclass of `SimpleList`, that **rejects any value that is not an `int`**.

**Requirements**
- `IntList()` with no argument creates an empty list (use a default value for `items`).
- Put the check in **one** helper method, `_validate(x)`, declared as a **static method**. It raises:
  `TypeError('IntList only supports integer values.')`
- In `__init__`, validate **every** item **before** handing the items to the parent class. If any item is invalid, no object is created.
- In `add`, validate the item **before** handing it to the parent class. A rejected `add` must leave the list unchanged.
- Reuse the parent through `super()`. Do not touch `self.items` directly.

**Test block**

```python
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
```

**Expected output**

```
IntList([]) 0
IntList([250, -75])
Rejected: IntList only supports integer values.
Rejected: IntList only supports integer values.
Rejected: IntList only supports integer values.
IntList([250, -75])
```

**Reasoning**
- **R3.** Why is `_validate` a static method rather than an instance method? What would be lost if it were a module-level function instead?

---

## Stage 4 — `SortedIntList`: combine both, write nothing new

The team now wants a list that is **sorted and integer-only**. Write `SortedIntList` so that it inherits from **both** `IntList` and `SortedList`, in that order.

**Requirements**
- The class body must be **`pass` and nothing else**. No new methods, no overrides.
- Add the `main()` function below, unchanged, and run it under the `if __name__ == '__main__':` guard.

**Test block**

```python
print([c.__name__ for c in SortedIntList.__mro__])


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
    main()
```

**Expected output**

```
['SortedIntList', 'IntList', 'SortedList', 'SimpleList', 'object']
SortedIntList([-1234, 3, 23, 42])
<class 'TypeError'> IntList only supports integer values.
<class 'TypeError'> IntList only supports integer values.
```

If your output matches but you cannot explain *why* an empty class gets both behaviours, the stage is not complete. Work through the questions below.

**Reasoning**
- **R4.** List, in order, every `__init__` that runs for `SortedIntList([42, 23, 3])`. Inside `IntList.__init__`, which class does `super()` reach, and why is it not `SimpleList`?
- **R5.** Do the same for `sil.add(-1234)`: which `add` methods run, in what order, and where does the sort happen?
- **R6.** Suppose `IntList.__init__` validated the items **after** calling `super().__init__(items)`. Predict what the second `try` block in `main()` would print, then explain the difference. Test your prediction in a scratch file, not in your submission.
- **R7.** Change the base order to `class SortedIntList(SortedList, IntList)`. Predict the new MRO and whether `main()`'s output changes, then check. Why does it behave the way it does?

---

## Stage 5 — Stretch (optional)

Each task below exposes a real weakness in the Stage 3–4 design. For each one, show the failing case, fix it, and add a short test block with its output.

1. **The one-shot iterable.** Run `print(IntList(x for x in [5, 3]))` and `print(SortedIntList(iter([42, 23, 3])))`. Both print an **empty** list, with no error. Explain why, then fix `IntList.__init__` so that any iterable works. The data must not be lost silently.
2. **Is `True` an integer?** `IntList([True, False])` is accepted. Explain why, then tighten `_validate` so that booleans are rejected with the same message.
3. **Slices lose the type.** `SortedIntList([3, 1, 2])[0:2]` returns a plain `list`. Change `SimpleList.__getitem__` so that a slice returns an object of the **same class** as the original (a `SortedIntList` slice is still a `SortedIntList`), while a single index still returns the element.

---

## Submission checklist

- [ ] All four classes are in one file, in stage order.
- [ ] Every stage's test block runs and its output matches exactly.
- [ ] `SortedList` and `IntList` use `super()` and never touch `self.items` directly.
- [ ] `SortedIntList` has `pass` as its only body.
- [ ] `ANSWERS` block has R1–R7, 1–2 lines each.
- [ ] (Optional) Stage 5 fixes, each with its own test block and output.
