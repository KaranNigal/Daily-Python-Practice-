# Rudder Analytics Round 2 — Answer Guide

Runnable implementations are in [round_2_solutions.py](./round_2_solutions.py);
SQL answers are in [round_2_sql_solutions.sql](./round_2_sql_solutions.sql).
Function names retain the question numbers (for example, `strings_01_reverse`
and `lists_40_marks_above_average`). Python functions return results instead of
printing them, so they can be reused and tested. The pattern functions return
one string per output row.

Use Python 3.10 or newer. Install the optional data-analysis dependencies with
`python -m pip install -r requirements.txt`, then run the regression suite from
this directory with `python -m unittest -v test_round_2_solutions`.

## 12. Predict the Output

1. `3.5 3 -4 1`
2. `False` (binary floating-point approximation makes the left side slightly
   different from `0.3`).
3. `[1, 2, 3]` (`a` and `b` refer to the same list).
4. `[1, 2]` (`b` is an independent shallow copy).
5. `[1, 2] [1, 2]` (the mutable default list is shared by calls).
6. The slice prints an empty line; indexing raises `IndexError`.
7. Raises `TypeError`: strings are immutable.
8. `False True False True`
9. `True False` (`==` compares values; `is` compares object identity).
10. `[[1, 0, 0], [1, 0, 0], [1, 0, 0]]` (all three rows refer to the same list).
11. `4` (the loop variable remains bound after the loop).
12. `['a', 'b', 'c'] abc`
13. `<class 'str'>` (`input()` returns text, including when the user types `5`).
14. `10` (the assignment inside `f` is local to that function).
15. `[0, 4, 8]`
16. `abbb ` (the second printed value is an empty string, so a trailing space
    appears before the newline).
17. Raises `TypeError`: tuples are immutable.
18. `0 2`
19. `[10, 7, 4, 1]`
20. Length is `3`; the set contains `{1, 2, 3}`. Set display order is not
    guaranteed.
21. `banana 1`
22. Prints `0`, `1`, `2`, and then `done`, each on its own line.
23. `512` (exponentiation is right-associative: `2 ** (3 ** 2)`).
24. `2 3`
25. `15 55`

## 13. Core Concepts

1. **List, tuple, set, dictionary:** A list is ordered and mutable; a tuple is
   ordered and immutable; a set stores unique hashable values without positional
   indexing; a dictionary maps unique hashable keys to values and preserves
   insertion order.
2. **Mutable vs immutable:** Mutable objects can be changed in place (such as
   lists, dictionaries, and sets). Immutable objects cannot (such as integers,
   strings, and tuples); an apparent update creates a new object/value.
3. **`==` vs `is`:** `==` asks whether values compare equal. `is` asks whether
   both names refer to the exact same object. Use `is None` for the `None`
   singleton, not for ordinary value comparisons.
4. **`*args` and `**kwargs`:** `*args` collects extra positional arguments into
   a tuple; `**kwargs` collects extra keyword arguments into a dictionary.
5. **Lambda:** A lambda is a small anonymous expression function, for example
   `square = lambda number: number * number`.
6. **List comprehension:** A concise way to build a list from an iterable.
   `squares = [n * n for n in numbers]` is equivalent to appending `n * n` in a
   `for n in numbers` loop.
7. **Shallow vs deep copy:** A shallow copy creates a new outer container but
   keeps references to nested objects. A deep copy recursively copies nested
   objects too (`copy.copy` vs `copy.deepcopy`).
8. **Exception flow:** `try` encloses risky code; a matching `except` handles
   an exception; `else` runs only when the `try` block succeeds; `finally` runs
   whether the operation succeeds or fails (commonly for cleanup).
9. **OOP:** A class defines a type and its behavior; an object is an instance.
   Inheritance reuses or specializes a base class; polymorphism lets different
   object types provide the same interface. Example:
   ```python
   class Greeter:
       def __init__(self, name):
           self.name = name

       def greet(self):
           return f"Hello, {self.name}"
   ```
10. **List vs set search:** Membership testing in a list is O(n) in the worst
    case. Membership testing in a hash set is O(1) average, O(n) worst case.
11. **Stack vs queue:** A stack is last-in, first-out (LIFO); a queue is
    first-in, first-out (FIFO). With a list: stack `append`/`pop`; queue
    `append`/`pop(0)` (a `collections.deque` is more efficient for queues).
12. **Generator / `yield`:** A generator lazily produces values. A function
    containing `yield` returns an iterator and suspends its local state after
    each yielded value, resuming on the next request.
13. **`append` vs `extend`:** `append(x)` adds `x` as one item. `extend(items)`
    iterates over `items` and adds each item.
14. **Decorator:** A decorator wraps or transforms a function or class,
    commonly to add behavior without changing its body. `@decorator` is
    shorthand for rebinding the decorated name to `decorator(original)`.

## Mock Tests

The ten mock-test algorithms have direct implementations:

| Mock | Solution functions |
| --- | --- |
| 1 | `mock_01_words_sorted_by_length`, `mock_02_kth_largest_distinct` |
| 2 | `mock_03_reverse_remove_value`, `mock_04_most_frequent_character` |
| 3 | `mock_05_longest_zero_sum_subarray`, `mock_06_anagram_differences` |
| 4 | `mock_07_matrix_summaries`, `mock_08_bracket_error_index` |
| 5 | `mock_09_second_salary_and_average`, `mock_10_unique_pairs_with_sum` |

For Mock 1, equal-length words retain their input order. For Mock 4, returned
matrix coordinates are zero-based. For Mock 5, the second-highest salary means
the second-highest **distinct** salary; the first employee with that salary is
returned. If none exists, the employee name is `None`.

## Final Checklist

The first four checklist items are self-assessments, not questions with fixed
answers. Their named algorithms are implemented in the numbered module. The
last item (email, equipment, and interview setup) is personal and must be
checked by the candidate.

## Notes on Assumptions

- Second/third-largest and mock-test k-th-largest results use distinct values;
  the regular k-th-smallest list problem counts repeated values as separate
  positions.
- Palindrome and anagram string checks ignore case and non-alphanumeric
  characters. Character-frequency functions otherwise preserve exact
  characters and case.
- Empty or invalid inputs raise a clear `ValueError`/`IndexError` where a result
  would otherwise be undefined; documented optional-result functions return
  `None` when no match exists.
- SQL uses PostgreSQL syntax, including `FILTER`, `DATE_TRUNC`, `ctid`, and
  bind parameters such as `:city` and `:n`. The duplicate deletion keeps the
  lowest `id` for each matching employee business record.
- Pandas and NumPy are imported only when their corresponding functions run.
