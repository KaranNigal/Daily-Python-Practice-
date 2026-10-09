"""Numbered Python solutions for the Rudder Analytics Round 2 question bank.

Functions are deliberately small and reusable.  Most list-returning pattern
functions return rows so they can be printed or tested without side effects.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from math import factorial as _factorial
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple, TypeVar

T = TypeVar("T")


# 1. Strings
def strings_01_reverse(text: str) -> str:
    return text[::-1]


def strings_02_is_palindrome(text: str) -> bool:
    cleaned = "".join(char.casefold() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def strings_03_vowel_consonant_counts(text: str) -> Tuple[int, int]:
    vowels = set("aeiou")
    letters = [char.casefold() for char in text if char.isalpha()]
    vowel_count = sum(char in vowels for char in letters)
    return vowel_count, len(letters) - vowel_count


def strings_04_are_anagrams(first: str, second: str) -> bool:
    normalize = lambda value: Counter(
        char.casefold() for char in value if char.isalnum()
    )
    return normalize(first) == normalize(second)


def strings_05_character_frequencies(text: str) -> Dict[str, int]:
    return dict(Counter(text))


def strings_06_first_non_repeating(text: str) -> Optional[str]:
    counts = Counter(text)
    return next((char for char in text if counts[char] == 1), None)


def strings_07_first_repeating(text: str) -> Optional[str]:
    seen = set()
    for char in text:
        if char in seen:
            return char
        seen.add(char)
    return None


def strings_08_reverse_word_order(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])


def strings_09_reverse_each_word(sentence: str) -> str:
    return " ".join(word[::-1] for word in sentence.split())


def strings_10_compress_runs(text: str) -> str:
    if not text:
        return ""
    parts: List[str] = []
    run_char = text[0]
    run_length = 1
    for char in text[1:]:
        if char == run_char:
            run_length += 1
        else:
            parts.append(f"{run_char}{run_length}")
            run_char, run_length = char, 1
    parts.append(f"{run_char}{run_length}")
    return "".join(parts)


def strings_11_decompress_runs(encoded: str) -> str:
    parts: List[str] = []
    index = 0
    while index < len(encoded):
        char = encoded[index]
        index += 1
        start = index
        while index < len(encoded) and encoded[index].isdigit():
            index += 1
        if start == index:
            raise ValueError(f"Missing run length after {char!r}")
        count = int(encoded[start:index])
        if count < 1:
            raise ValueError("Run lengths must be positive")
        parts.append(char * count)
    return "".join(parts)


def strings_12_remove_duplicate_characters(text: str) -> str:
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)


def strings_13_longest_word(sentence: str) -> str:
    return max(sentence.split(), key=len, default="")


def strings_14_word_count(sentence: str) -> int:
    return len(sentence.split())


def strings_15_is_pangram(text: str) -> bool:
    return set("abcdefghijklmnopqrstuvwxyz").issubset(
        char.casefold() for char in text
    )


def strings_16_swap_case_manually(text: str) -> str:
    result = []
    for char in text:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)


def strings_17_capitalize_words(sentence: str) -> str:
    return " ".join(word[:1].upper() + word[1:].lower() for word in sentence.split())


def strings_18_most_frequent_character(text: str) -> Optional[str]:
    if not text:
        return None
    counts = Counter(text)
    return max(dict.fromkeys(text), key=counts.__getitem__)


def strings_19_longest_common_prefix(words: Sequence[str]) -> str:
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def strings_20_keep_only_letters_and_digits(text: str) -> str:
    return "".join(char for char in text if char.isalnum())


def strings_21_character_categories(text: str) -> Dict[str, int]:
    counts = {"uppercase": 0, "lowercase": 0, "digits": 0, "special": 0}
    for char in text:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        else:
            counts["special"] += 1
    return counts


def strings_22_contains_only_digits(text: str) -> bool:
    return bool(text) and all("0" <= char <= "9" for char in text)


def strings_23_replace_vowels(text: str) -> str:
    return "".join("*" if char.casefold() in "aeiou" else char for char in text)


def strings_24_is_rotation(first: str, second: str) -> bool:
    return len(first) == len(second) and second in first + first


def strings_25_all_substrings(text: str) -> List[str]:
    return [text[start:end] for start in range(len(text)) for end in range(start + 1, len(text) + 1)]


def strings_26_characters_at_even_indexes(text: str) -> str:
    return text[::2]


def strings_27_longest_unique_substring_length(text: str) -> int:
    last_seen: Dict[str, int] = {}
    start = longest = 0
    for index, char in enumerate(text):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = index
        longest = max(longest, index - start + 1)
    return longest


def strings_28_brackets_balanced(text: str) -> bool:
    return mock_08_bracket_error_index(text) is None


def strings_29_ascii_codes(text: str) -> List[int]:
    return [ord(char) for char in text]


def strings_29_from_ascii_codes(codes: Iterable[int]) -> str:
    return "".join(chr(code) for code in codes)


def strings_30_words_with_lengths(sentence: str) -> List[Tuple[str, int]]:
    return [(word, len(word)) for word in sentence.split()]


# 2. Arrays / Lists
def lists_01_min_max(values: Sequence[T]) -> Tuple[T, T]:
    if not values:
        raise ValueError("Expected at least one value")
    return min(values), max(values)


def lists_02_second_largest(values: Sequence[T]) -> Optional[T]:
    distinct = sorted(set(values), reverse=True)
    return distinct[1] if len(distinct) > 1 else None


def lists_03_third_largest(values: Sequence[T]) -> Optional[T]:
    distinct = sorted(set(values), reverse=True)
    return distinct[2] if len(distinct) > 2 else None


def lists_04_sort_ascending(values: Sequence[T]) -> List[T]:
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
    return result


def lists_05_sort_descending(values: Sequence[T]) -> List[T]:
    return sorted(values, reverse=True)


def lists_06_remove_duplicates(values: Iterable[T]) -> List[T]:
    return list(dict.fromkeys(values))


def lists_07_rotate_right(values: Sequence[T], k: int) -> List[T]:
    items = list(values)
    if not items:
        return []
    shift = k % len(items)
    return items[-shift:] + items[:-shift] if shift else items


def lists_08_rotate_left(values: Sequence[T], k: int) -> List[T]:
    items = list(values)
    if not items:
        return []
    shift = k % len(items)
    return items[shift:] + items[:shift]


def lists_09_two_sum_indexes(values: Sequence[float], target: float) -> Optional[Tuple[int, int]]:
    seen: Dict[float, int] = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None


def lists_10_missing_number(values: Sequence[int], n: int) -> int:
    return n * (n + 1) // 2 - sum(values)


def lists_11_move_zeros_to_end(values: Sequence[T]) -> List[T]:
    return [value for value in values if value != 0] + [value for value in values if value == 0]


def lists_12_maximum_subarray_sum(values: Sequence[float]) -> Optional[float]:
    if not values:
        return None
    best_ending = best = values[0]
    for value in values[1:]:
        best_ending = max(value, best_ending + value)
        best = max(best, best_ending)
    return best


def lists_13_merge_sorted(first: Sequence[T], second: Sequence[T]) -> List[T]:
    merged: List[T] = []
    left = right = 0
    while left < len(first) and right < len(second):
        if first[left] <= second[right]:
            merged.append(first[left])
            left += 1
        else:
            merged.append(second[right])
            right += 1
    return merged + list(first[left:]) + list(second[right:])


def lists_14_binary_search(values: Sequence[T], target: T) -> int:
    low, high = 0, len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def lists_15_duplicates(values: Iterable[T]) -> List[T]:
    seen, duplicates = set(), set()
    result = []
    for value in values:
        if value in seen and value not in duplicates:
            duplicates.add(value)
            result.append(value)
        seen.add(value)
    return result


def lists_16_most_frequent(values: Sequence[T]) -> Optional[T]:
    if not values:
        return None
    counts = Counter(values)
    return max(dict.fromkeys(values), key=counts.__getitem__)


def lists_17_count_pairs_with_sum(values: Sequence[float], target: float) -> int:
    seen: Counter = Counter()
    pairs = 0
    for value in values:
        pairs += seen[target - value]
        seen[value] += 1
    return pairs


def lists_18_even_and_odd_indexes(values: Sequence[T]) -> Tuple[List[T], List[T]]:
    return list(values[::2]), list(values[1::2])


def lists_19_reverse_in_place(values: List[T]) -> None:
    left, right = 0, len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1


def lists_20_is_sorted_ascending(values: Sequence[T]) -> bool:
    return all(values[index] <= values[index + 1] for index in range(len(values) - 1))


def lists_21_sum_and_average(values: Sequence[float]) -> Tuple[float, float]:
    if not values:
        raise ValueError("Expected at least one value")
    total = sum(values)
    return total, total / len(values)


def lists_22_separate_even_odd(values: Iterable[int]) -> Tuple[List[int], List[int]]:
    evens, odds = [], []
    for value in values:
        (evens if value % 2 == 0 else odds).append(value)
    return evens, odds


def lists_23_common_elements(first: Iterable[T], second: Iterable[T]) -> List[T]:
    second_values = set(second)
    return list(dict.fromkeys(value for value in first if value in second_values))


def lists_24_first_not_in_second(first: Iterable[T], second: Iterable[T]) -> List[T]:
    second_values = set(second)
    return [value for value in first if value not in second_values]


def lists_25_union_and_intersection(
    first: Iterable[T], second: Iterable[T]
) -> Tuple[List[T], List[T]]:
    first_values, second_values = list(first), list(second)
    union = list(dict.fromkeys(first_values + second_values))
    intersection = lists_23_common_elements(first_values, second_values)
    return union, intersection


def lists_26_running_sum(values: Iterable[float]) -> List[float]:
    total = 0
    result = []
    for value in values:
        total += value
        result.append(total)
    return result


def lists_27_longest_increasing_run(values: Sequence[float]) -> List[float]:
    if not values:
        return []
    best_start = current_start = 0
    best_length = current_length = 1
    for index in range(1, len(values)):
        if values[index] > values[index - 1]:
            current_length += 1
        else:
            current_start, current_length = index, 1
        if current_length > best_length:
            best_start, best_length = current_start, current_length
    return list(values[best_start:best_start + best_length])


def lists_28_leaders(values: Sequence[float]) -> List[float]:
    leaders = []
    maximum_to_right = None
    for value in reversed(values):
        if maximum_to_right is None or value > maximum_to_right:
            leaders.append(value)
            maximum_to_right = value
    return leaders[::-1]


def lists_29_equilibrium_index(values: Sequence[float]) -> Optional[int]:
    right_sum = sum(values)
    left_sum = 0
    for index, value in enumerate(values):
        right_sum -= value
        if left_sum == right_sum:
            return index
        left_sum += value
    return None


def lists_30_segregate_zeros_ones(values: Sequence[int]) -> List[int]:
    if any(value not in (0, 1) for value in values):
        raise ValueError("All values must be 0 or 1")
    zeros = values.count(0)
    return [0] * zeros + [1] * (len(values) - zeros)


def lists_31_sort_zero_one_two(values: Sequence[int]) -> List[int]:
    if any(value not in (0, 1, 2) for value in values):
        raise ValueError("All values must be 0, 1, or 2")
    counts = Counter(values)
    return [0] * counts[0] + [1] * counts[1] + [2] * counts[2]


def lists_32_product_except_self(values: Sequence[float]) -> List[float]:
    result = [1] * len(values)
    prefix = 1
    for index, value in enumerate(values):
        result[index] = prefix
        prefix *= value
    suffix = 1
    for index in range(len(values) - 1, -1, -1):
        result[index] *= suffix
        suffix *= values[index]
    return result


def lists_33_majority_element(values: Sequence[T]) -> Optional[T]:
    candidate: Optional[T] = None
    balance = 0
    for value in values:
        if balance == 0:
            candidate = value
        balance += 1 if value == candidate else -1
    if candidate is not None and values.count(candidate) > len(values) // 2:
        return candidate
    return None


def lists_34_is_palindrome(values: Sequence[T]) -> bool:
    return list(values) == list(values)[::-1]


def lists_35_sum_squares_of_evens(values: Iterable[int]) -> int:
    return sum(value * value for value in values if value % 2 == 0)


def lists_36_kth_smallest(values: Sequence[T], k: int) -> T:
    if not 1 <= k <= len(values):
        raise ValueError("k must be between 1 and the number of values")
    return sorted(values)[k - 1]


def lists_37_insert_and_delete(
    values: Sequence[T], position: int, item: T, delete_value: T
) -> List[T]:
    result = list(values)
    result.insert(position, item)
    result.remove(delete_value)
    return result


def lists_38_longest_consecutive_sequence(values: Iterable[int]) -> int:
    numbers = set(values)
    longest = 0
    for number in numbers:
        if number - 1 not in numbers:
            end = number
            while end in numbers:
                end += 1
            longest = max(longest, end - number)
    return longest


def lists_39_range(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("Expected at least one value")
    return max(values) - min(values)


def lists_40_marks_above_average(marks: Sequence[float]) -> List[Tuple[int, float]]:
    if not marks:
        return []
    average = sum(marks) / len(marks)
    return [(index, mark) for index, mark in enumerate(marks) if mark > average]


# 3. Numbers and Maths
def maths_01_is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def maths_02_primes_up_to(n: int) -> List[int]:
    return [number for number in range(2, n + 1) if maths_01_is_prime(number)]


def maths_03_fibonacci_terms(n: int) -> List[int]:
    if n < 0:
        raise ValueError("n must be non-negative")
    result, first, second = [], 0, 1
    for _ in range(n):
        result.append(first)
        first, second = second, first + second
    return result


def maths_04_factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers")
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


def maths_04_factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers")
    return 1 if n < 2 else n * maths_04_factorial_recursive(n - 1)


def maths_05_gcd_lcm(first: int, second: int) -> Tuple[int, int]:
    a, b = abs(first), abs(second)
    while b:
        a, b = b, a % b
    gcd = a
    lcm = 0 if gcd == 0 else abs(first * second) // gcd
    return gcd, lcm


def maths_06_sum_digits(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))


def maths_07_reverse_number(number: int) -> int:
    sign = -1 if number < 0 else 1
    return sign * int(str(abs(number))[::-1])


def maths_08_is_number_palindrome(number: int) -> bool:
    return number >= 0 and str(number) == str(number)[::-1]


def maths_09_is_armstrong(number: int) -> bool:
    if number < 0:
        return False
    digits = str(number)
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == number


def maths_10_fizzbuzz(n: int) -> List[str]:
    return [
        "FizzBuzz" if number % 15 == 0 else
        "Fizz" if number % 3 == 0 else
        "Buzz" if number % 5 == 0 else str(number)
        for number in range(1, n + 1)
    ]


def maths_11_digit_count(number: int) -> int:
    return len(str(abs(number)))


def maths_12_is_perfect(number: int) -> bool:
    if number <= 1:
        return False
    divisor_sum = 1
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            divisor_sum += divisor
            partner = number // divisor
            if partner != divisor:
                divisor_sum += partner
        divisor += 1
    return divisor_sum == number


def maths_13_is_perfect_square(number: int) -> bool:
    if number < 0:
        return False
    low, high = 0, number
    while low <= high:
        middle = (low + high) // 2
        square = middle * middle
        if square == number:
            return True
        if square < number:
            low = middle + 1
        else:
            high = middle - 1
    return False


def maths_14_decimal_to_binary(number: int) -> str:
    if number < 0:
        raise ValueError("number must be non-negative")
    if number == 0:
        return "0"
    bits = []
    while number:
        bits.append(str(number % 2))
        number //= 2
    return "".join(reversed(bits))


def maths_15_binary_to_decimal(binary: str) -> int:
    if not binary or any(bit not in "01" for bit in binary):
        raise ValueError("Expected a non-empty binary string")
    value = 0
    for bit in binary:
        value = value * 2 + int(bit)
    return value


def maths_16_power(base: float, exponent: int) -> float:
    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("Zero cannot be raised to a negative power")
        return 1 / maths_16_power(base, -exponent)
    result = 1
    while exponent:
        if exponent % 2:
            result *= base
        base *= base
        exponent //= 2
    return result


def maths_17_even_without_modulo(number: int) -> bool:
    return number // 2 * 2 == number


def maths_18_multiplication_table(number: int, limit: int = 10) -> List[str]:
    return [f"{number} x {multiple} = {number * multiple}" for multiple in range(1, limit + 1)]


def maths_19_sum_natural_numbers(n: int) -> Tuple[int, int]:
    if n < 0:
        raise ValueError("n must be non-negative")
    loop_sum = sum(range(1, n + 1))
    formula_sum = n * (n + 1) // 2
    return loop_sum, formula_sum


def maths_20_factors(number: int) -> List[int]:
    if number <= 0:
        raise ValueError("number must be positive")
    low, high = [], []
    divisor = 1
    while divisor * divisor <= number:
        if number % divisor == 0:
            low.append(divisor)
            if divisor != number // divisor:
                high.append(number // divisor)
        divisor += 1
    return low + high[::-1]


def maths_21_prime_factorization(number: int) -> List[int]:
    if number < 1:
        raise ValueError("number must be positive")
    factors, divisor = [], 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.append(number)
    return factors


def maths_22_is_strong_number(number: int) -> bool:
    return number >= 0 and sum(_factorial(int(digit)) for digit in str(number)) == number


def maths_23_armstrong_numbers(start: int, end: int) -> List[int]:
    return [number for number in range(start, end + 1) if maths_09_is_armstrong(number)]


def maths_24_swap_without_temporary(first: T, second: T) -> Tuple[T, T]:
    return second, first


def maths_25_largest_of_three(first: T, second: T, third: T) -> T:
    return max(first, second, third)


def maths_26_is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def maths_27_interest(
    principal: float, annual_rate_percent: float, years: float
) -> Tuple[float, float]:
    simple = principal * annual_rate_percent * years / 100
    compound = principal * (1 + annual_rate_percent / 100) ** years - principal
    return simple, compound


def maths_28_average(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("Expected at least one value")
    return sum(values) / len(values)


def maths_29_trailing_zeros_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    zeros = 0
    divisor = 5
    while divisor <= n:
        zeros += n // divisor
        divisor *= 5
    return zeros


def maths_30_collatz_sequence(number: int) -> List[int]:
    if number < 1:
        raise ValueError("number must be positive")
    result = [number]
    while number != 1:
        number = number // 2 if number % 2 == 0 else 3 * number + 1
        result.append(number)
    return result


# 4. Linked List
@dataclass
class Node:
    data: Any
    next: Optional["Node"] = None


def linked_01_from_list(values: Iterable[T]) -> Optional[Node]:
    head = tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def linked_01_to_list(head: Optional[Node]) -> List[Any]:
    result, current = [], head
    while current is not None:
        result.append(current.data)
        current = current.next
    return result


def linked_02_insert_beginning(head: Optional[Node], value: Any) -> Node:
    return Node(value, head)


def linked_02_insert_end(head: Optional[Node], value: Any) -> Node:
    node = Node(value)
    if head is None:
        return node
    current = head
    while current.next is not None:
        current = current.next
    current.next = node
    return head


def linked_02_insert_at(head: Optional[Node], position: int, value: Any) -> Node:
    if position < 0:
        raise IndexError("position must be non-negative")
    if position == 0:
        return linked_02_insert_beginning(head, value)
    current = head
    for _ in range(position - 1):
        if current is None:
            raise IndexError("position is outside the list")
        current = current.next
    if current is None:
        raise IndexError("position is outside the list")
    current.next = Node(value, current.next)
    return head


def linked_03_delete_first(head: Optional[Node]) -> Optional[Node]:
    return None if head is None else head.next


def linked_03_delete_last(head: Optional[Node]) -> Optional[Node]:
    if head is None or head.next is None:
        return None
    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None
    return head


def linked_03_delete_value(head: Optional[Node], value: Any) -> Optional[Node]:
    sentinel = Node(None, head)
    previous, current = sentinel, head
    while current is not None:
        if current.data == value:
            previous.next = current.next
            break
        previous, current = current, current.next
    return sentinel.next


def linked_04_length(head: Optional[Node]) -> int:
    length, current = 0, head
    while current is not None:
        length += 1
        current = current.next
    return length


def linked_05_search(head: Optional[Node], value: Any) -> bool:
    current = head
    while current is not None:
        if current.data == value:
            return True
        current = current.next
    return False


def linked_06_reverse(head: Optional[Node]) -> Optional[Node]:
    previous, current = None, head
    while current is not None:
        following = current.next
        current.next = previous
        previous, current = current, following
    return previous


def linked_07_middle(head: Optional[Node]) -> Optional[Node]:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
    return slow


def linked_08_has_cycle(head: Optional[Node]) -> bool:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


def linked_09_merge_sorted(first: Optional[Node], second: Optional[Node]) -> Optional[Node]:
    sentinel = Node(None)
    tail = sentinel
    while first is not None and second is not None:
        if first.data <= second.data:
            tail.next, first = first, first.next
        else:
            tail.next, second = second, second.next
        tail = tail.next
    tail.next = first if first is not None else second
    return sentinel.next


def linked_10_remove_nth_from_end(head: Optional[Node], n: int) -> Optional[Node]:
    if n <= 0:
        raise ValueError("n must be positive")
    sentinel = Node(None, head)
    fast = slow = sentinel
    for _ in range(n):
        fast = fast.next
        if fast is None:
            raise IndexError("n exceeds the list length")
    while fast.next is not None:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return sentinel.next


def linked_11_remove_sorted_duplicates(head: Optional[Node]) -> Optional[Node]:
    current = head
    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def linked_12_is_palindrome(head: Optional[Node]) -> bool:
    values = linked_01_to_list(head)
    return values == values[::-1]


def linked_13_nth_from_end(head: Optional[Node], n: int) -> Any:
    if n <= 0:
        raise ValueError("n must be positive")
    fast = slow = head
    for _ in range(n):
        if fast is None:
            raise IndexError("n exceeds the list length")
        fast = fast.next
    while fast is not None:
        fast, slow = fast.next, slow.next
    return slow.data


def linked_14_values_in_reverse(head: Optional[Node]) -> List[Any]:
    return linked_01_to_list(head)[::-1]


def linked_15_add_reverse_order_numbers(
    first: Optional[Node], second: Optional[Node]
) -> Optional[Node]:
    sentinel = tail = Node(0)
    carry = 0
    while first is not None or second is not None or carry:
        total = carry
        if first is not None:
            total += first.data
            first = first.next
        if second is not None:
            total += second.data
            second = second.next
        carry, digit = divmod(total, 10)
        tail.next = Node(digit)
        tail = tail.next
    return sentinel.next


def linked_16_intersection(first: Optional[Node], second: Optional[Node]) -> Optional[Node]:
    left, right = first, second
    while left is not right:
        left = second if left is None else left.next
        right = first if right is None else right.next
    return left


def linked_17_swap_adjacent_pairs(head: Optional[Node]) -> Optional[Node]:
    sentinel = Node(None, head)
    previous = sentinel
    while previous.next is not None and previous.next.next is not None:
        first, second = previous.next, previous.next.next
        previous.next, first.next, second.next = second, second.next, first
        previous = first
    return sentinel.next


def linked_18_count_value(head: Optional[Node], value: Any) -> int:
    count, current = 0, head
    while current is not None:
        count += current.data == value
        current = current.next
    return count


# 5. Pattern Printing (each function returns lines from top to bottom)
def patterns_01_right_triangle(rows: int) -> List[str]:
    return ["*" * width for width in range(1, rows + 1)]


def patterns_02_inverted_right_triangle(rows: int) -> List[str]:
    return ["*" * width for width in range(rows, 0, -1)]


def patterns_03_pyramid(rows: int) -> List[str]:
    return [" " * (rows - row) + "*" * (2 * row - 1) for row in range(1, rows + 1)]


def patterns_04_inverted_pyramid(rows: int) -> List[str]:
    return [" " * (rows - row) + "*" * (2 * row - 1) for row in range(rows, 0, -1)]


def patterns_05_diamond(rows: int) -> List[str]:
    if rows <= 0:
        return []
    return patterns_03_pyramid(rows) + patterns_04_inverted_pyramid(rows)[1:]


def patterns_06_number_triangle(rows: int) -> List[str]:
    return [" ".join(str(number) for number in range(1, row + 1)) for row in range(1, rows + 1)]


def patterns_07_floyd_triangle(rows: int) -> List[str]:
    value, result = 1, []
    for row in range(1, rows + 1):
        result.append(" ".join(str(number) for number in range(value, value + row)))
        value += row
    return result


def patterns_08_pascals_triangle(rows: int) -> List[str]:
    result = []
    row_values = [1]
    for _ in range(rows):
        result.append(" ".join(map(str, row_values)))
        row_values = [1] + [row_values[i] + row_values[i + 1] for i in range(len(row_values) - 1)] + [1]
    return result


def patterns_09_hollow_square(size: int) -> List[str]:
    return [
        "*" * size if row in (0, size - 1) else "*" + " " * max(0, size - 2) + "*"
        for row in range(size)
    ]


def patterns_10_alphabet_triangle(rows: int) -> List[str]:
    return [" ".join(chr(ord("A") + index) for index in range(row)) for row in range(1, rows + 1)]


# 6. Matrix (2D lists)
def _matrix_shape(matrix: Sequence[Sequence[Any]]) -> Tuple[int, int]:
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError("Matrix rows must have equal lengths")
    return rows, columns


def matrices_01_rows(matrix: Sequence[Sequence[T]]) -> List[List[T]]:
    _matrix_shape(matrix)
    return [list(row) for row in matrix]


def matrices_02_transpose(matrix: Sequence[Sequence[T]]) -> List[List[T]]:
    _matrix_shape(matrix)
    return [list(row) for row in zip(*matrix)] if matrix else []


def matrices_03_add(first: Sequence[Sequence[float]], second: Sequence[Sequence[float]]) -> List[List[float]]:
    if _matrix_shape(first) != _matrix_shape(second):
        raise ValueError("Matrices must have the same dimensions")
    return [[a + b for a, b in zip(left, right)] for left, right in zip(first, second)]


def matrices_04_multiply(first: Sequence[Sequence[float]], second: Sequence[Sequence[float]]) -> List[List[float]]:
    rows_a, columns_a = _matrix_shape(first)
    rows_b, columns_b = _matrix_shape(second)
    if columns_a != rows_b:
        raise ValueError("The number of columns in the first matrix must equal the number of rows in the second")
    return [
        [sum(first[row][k] * second[k][column] for k in range(columns_a)) for column in range(columns_b)]
        for row in range(rows_a)
    ]


def matrices_05_diagonal_sums(matrix: Sequence[Sequence[float]]) -> Tuple[float, float]:
    rows, columns = _matrix_shape(matrix)
    if rows != columns:
        raise ValueError("A square matrix is required")
    size = rows
    return (
        sum(matrix[index][index] for index in range(size)),
        sum(matrix[index][size - index - 1] for index in range(size)),
    )


def matrices_06_row_and_column_sums(matrix: Sequence[Sequence[float]]) -> Tuple[List[float], List[float]]:
    rows, columns = _matrix_shape(matrix)
    row_sums = [sum(row) for row in matrix]
    column_sums = [sum(matrix[row][column] for row in range(rows)) for column in range(columns)]
    return row_sums, column_sums


def matrices_07_spiral_order(matrix: Sequence[Sequence[T]]) -> List[T]:
    rows, columns = _matrix_shape(matrix)
    result = []
    top, bottom, left, right = 0, rows - 1, 0, columns - 1
    while top <= bottom and left <= right:
        result.extend(matrix[top][left:right + 1])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            result.extend(reversed(matrix[bottom][left:right + 1]))
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result


def matrices_08_rotate_clockwise(matrix: Sequence[Sequence[T]]) -> List[List[T]]:
    rows, columns = _matrix_shape(matrix)
    if rows != columns:
        raise ValueError("A square matrix is required")
    return [list(row) for row in zip(*matrix[::-1])]


def matrices_09_is_symmetric(matrix: Sequence[Sequence[Any]]) -> bool:
    rows, columns = _matrix_shape(matrix)
    return rows == columns and all(matrix[row][column] == matrix[column][row] for row in range(rows) for column in range(columns))


def matrices_10_largest_in_each_row(matrix: Sequence[Sequence[T]]) -> List[T]:
    _matrix_shape(matrix)
    if any(not row for row in matrix):
        raise ValueError("Each row must contain at least one value")
    return [max(row) for row in matrix]


# 7. Dictionary, Set and Counter
def dictionaries_01_word_frequencies(sentence: str) -> Dict[str, int]:
    return dict(Counter(sentence.casefold().split()))


def dictionaries_02_most_frequent_word(paragraph: str) -> Optional[str]:
    words = paragraph.casefold().split()
    if not words:
        return None
    counts = Counter(words)
    return max(dict.fromkeys(words), key=counts.__getitem__)


def dictionaries_03_group_anagrams(words: Iterable[str]) -> List[List[str]]:
    groups: Dict[Tuple[str, ...], List[str]] = {}
    for word in words:
        groups.setdefault(tuple(sorted(word.casefold())), []).append(word)
    return list(groups.values())


def dictionaries_04_first_non_repeating(values: Iterable[T]) -> Optional[T]:
    items = list(values)
    counts = Counter(items)
    return next((value for value in items if counts[value] == 1), None)


def dictionaries_05_merge_sum_values(first: Dict[T, float], second: Dict[T, float]) -> Dict[T, float]:
    result = dict(first)
    for key, value in second.items():
        result[key] = result.get(key, 0) + value
    return result


def dictionaries_06_sort_by_value_descending(mapping: Dict[T, float]) -> List[Tuple[T, float]]:
    return sorted(mapping.items(), key=lambda item: item[1], reverse=True)


def dictionaries_07_invert(mapping: Dict[T, Any]) -> Dict[Any, T]:
    return {value: key for key, value in mapping.items()}


def dictionaries_08_first_not_second(first: Iterable[T], second: Iterable[T]) -> set:
    return set(first) - set(second)


def dictionaries_09_topper_and_average(marks: Dict[str, float]) -> Tuple[Optional[str], float]:
    if not marks:
        return None, 0.0
    topper = max(marks, key=marks.__getitem__)
    return topper, sum(marks.values()) / len(marks)


def dictionaries_10_all_unique(values: Iterable[T]) -> bool:
    items = list(values)
    return len(items) == len(set(items))


def dictionaries_11_pairs_with_difference(values: Iterable[float], k: float) -> List[Tuple[float, float]]:
    items = list(values)
    numbers = set(items)
    difference = abs(k)
    if difference == 0:
        counts = Counter(items)
        return [(value, value) for value in sorted(numbers) if counts[value] > 1]
    return sorted(
        (value, value + difference)
        for value in numbers
        if value + difference in numbers
    )


def dictionaries_12_vowel_frequencies(text: str) -> Dict[str, int]:
    return {vowel: sum(char.casefold() == vowel for char in text) for vowel in "aeiou"}


# 8. Recursion, Sorting and Searching
def recursion_01_sum_digits(number: int) -> int:
    number = abs(number)
    return number if number < 10 else number % 10 + recursion_01_sum_digits(number // 10)


def recursion_02_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers")
    return 1 if n < 2 else n * recursion_02_factorial(n - 1)


def recursion_03_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return recursion_03_fibonacci(n - 1) + recursion_03_fibonacci(n - 2)


def recursion_04_power(base: float, exponent: int) -> float:
    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("Zero cannot be raised to a negative power")
        return 1 / recursion_04_power(base, -exponent)
    if exponent == 0:
        return 1
    half = recursion_04_power(base, exponent // 2)
    square = half * half
    return square if exponent % 2 == 0 else base * square


def recursion_05_reverse_string(text: str) -> str:
    return text if len(text) <= 1 else recursion_05_reverse_string(text[1:]) + text[0]


def recursion_06_is_palindrome(text: str) -> bool:
    if len(text) < 2:
        return True
    return text[0] == text[-1] and recursion_06_is_palindrome(text[1:-1])


def recursion_07_bubble_sort(values: Sequence[T]) -> List[T]:
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


def recursion_07_selection_sort(values: Sequence[T]) -> List[T]:
    result = list(values)
    for start in range(len(result)):
        smallest = min(range(start, len(result)), key=result.__getitem__)
        result[start], result[smallest] = result[smallest], result[start]
    return result


def recursion_07_insertion_sort(values: Sequence[T]) -> List[T]:
    result = list(values)
    for index in range(1, len(result)):
        item, position = result[index], index
        while position > 0 and result[position - 1] > item:
            result[position] = result[position - 1]
            position -= 1
        result[position] = item
    return result


def recursion_08_merge_sort(values: Sequence[T]) -> List[T]:
    if len(values) < 2:
        return list(values)
    middle = len(values) // 2
    return lists_13_merge_sorted(recursion_08_merge_sort(values[:middle]), recursion_08_merge_sort(values[middle:]))


def recursion_09_linear_search(values: Sequence[T], target: T) -> int:
    return next((index for index, value in enumerate(values) if value == target), -1)


def recursion_09_binary_search(values: Sequence[T], target: T) -> int:
    return lists_14_binary_search(values, target)


def recursion_10_tower_of_hanoi(n: int, source: str = "A", auxiliary: str = "B", target: str = "C") -> List[Tuple[str, str]]:
    if n < 0:
        raise ValueError("n must be non-negative")
    moves: List[Tuple[str, str]] = []

    def move(disks: int, start: str, spare: str, end: str) -> None:
        if disks:
            move(disks - 1, start, end, spare)
            moves.append((start, end))
            move(disks - 1, spare, start, end)

    move(n, source, auxiliary, target)
    return moves


def recursion_11_permutations(text: str) -> List[str]:
    if len(text) <= 1:
        return [text]
    return [
        char + suffix
        for index, char in enumerate(text)
        for suffix in recursion_11_permutations(text[:index] + text[index + 1:])
    ]


def recursion_12_subsets(values: Sequence[T]) -> List[List[T]]:
    result: List[List[T]] = [[]]
    for value in values:
        result += [subset + [value] for subset in result]
    return result


# 9. File Handling and Basic I/O
def files_01_count_text(path: str | Path) -> Dict[str, int]:
    text = Path(path).read_text(encoding="utf-8")
    return {"lines": len(text.splitlines()), "words": len(text.split()), "characters": len(text)}


def files_02_write_items(path: str | Path, items: Iterable[Any]) -> None:
    Path(path).write_text("".join(f"{item}\n" for item in items), encoding="utf-8")


def files_03_sum_numbers(path: str | Path) -> float:
    tokens = Path(path).read_text(encoding="utf-8").split()
    numbers = [float(token) for token in tokens]
    total = sum(numbers)
    return int(total) if total.is_integer() else total


def files_04_copy(source: str | Path, destination: str | Path) -> None:
    Path(destination).write_bytes(Path(source).read_bytes())


def files_05_sum_input_line(line: str) -> int:
    return sum(map(int, line.split()))


def files_06_reverse_lines(lines: Sequence[str]) -> List[str]:
    return list(lines)[::-1]


def files_07_format_name_age(name: str, age: int) -> str:
    return f"My name is {name} and I am {age} years old."


def files_08_parse_csv_integers(line: str) -> List[int]:
    return [int(value.strip()) for value in line.split(",") if value.strip()]


# 11. Pandas and Data Handling (imports remain local so base solutions need no extras)
def pandas_01_load_csv_summary(path: str | Path) -> Tuple[Any, Tuple[int, int], Any]:
    import pandas as pd

    frame = pd.read_csv(path)
    return frame.head(), frame.shape, frame.dtypes


def pandas_02_filter_above(frame: Any, column: str, threshold: float) -> Any:
    return frame.loc[frame[column] > threshold]


def pandas_03_missing_counts(frame: Any) -> Any:
    return frame.isna().sum()


def pandas_04_fill_numeric_means(frame: Any) -> Any:
    result = frame.copy()
    numeric_columns = result.select_dtypes(include="number").columns
    result[numeric_columns] = result[numeric_columns].fillna(result[numeric_columns].mean())
    return result


def pandas_05_drop_duplicates(frame: Any) -> Any:
    return frame.drop_duplicates()


def pandas_06_group_aggregates(frame: Any, group_column: str, value_column: str) -> Any:
    return frame.groupby(group_column)[value_column].agg(["mean", "sum", "count"])


def pandas_07_sort_descending(frame: Any, column: str) -> Any:
    return frame.sort_values(by=column, ascending=False)


def pandas_08_add_columns(frame: Any, new_column: str, first: str, second: str) -> Any:
    result = frame.copy()
    result[new_column] = result[first] + result[second]
    return result


def pandas_09_merge(first: Any, second: Any, key: str, how: str = "inner") -> Any:
    return first.merge(second, on=key, how=how)


def pandas_10_top_frequencies(frame: Any, column: str, limit: int = 5) -> Any:
    return frame[column].value_counts().head(limit)


def pandas_11_month_from_datetime(frame: Any, source_column: str, new_column: str = "month") -> Any:
    import pandas as pd

    result = frame.copy()
    result[source_column] = pd.to_datetime(result[source_column], errors="raise")
    result[new_column] = result[source_column].dt.month
    return result


def pandas_12_correlation(frame: Any, first: str, second: str) -> float:
    return frame[first].corr(frame[second])


def numpy_13_summary(values: Iterable[float]) -> Tuple[float, float, float]:
    import numpy as np

    array = np.asarray(list(values), dtype=float)
    if array.size == 0:
        raise ValueError("Expected at least one value")
    return float(np.mean(array)), float(np.median(array)), float(np.std(array))


def numpy_14_matrix_summary(values: Optional[Sequence[Sequence[float]]] = None) -> Tuple[Any, Any, Any]:
    import numpy as np

    matrix = np.array(values if values is not None else [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    if matrix.shape != (3, 3):
        raise ValueError("Expected a 3x3 matrix")
    return matrix, matrix.T, matrix.sum(axis=1)


# 14. Timed Mock Tests
def mock_01_words_sorted_by_length(sentence: str) -> List[Tuple[str, int]]:
    words = sentence.split()
    ordered = sorted(enumerate(words), key=lambda item: (-len(item[1]), item[0]))
    return [(word, len(word)) for _, word in ordered]


def mock_02_kth_largest_distinct(values: Iterable[int], k: int) -> int:
    distinct = sorted(set(values), reverse=True)
    return distinct[k - 1] if 1 <= k <= len(distinct) else -1


def mock_03_reverse_remove_value(values: Iterable[T], value: T) -> List[T]:
    return [item for item in reversed(list(values)) if item != value]


def mock_04_most_frequent_character(text: str) -> Tuple[Optional[str], int]:
    if not text:
        return None, 0
    counts = Counter(text)
    char = max(dict.fromkeys(text), key=counts.__getitem__)
    return char, counts[char]


def mock_05_longest_zero_sum_subarray(values: Sequence[int]) -> int:
    first_index = {0: -1}
    running_sum = longest = 0
    for index, value in enumerate(values):
        running_sum += value
        if running_sum in first_index:
            longest = max(longest, index - first_index[running_sum])
        else:
            first_index[running_sum] = index
    return longest


def mock_06_anagram_differences(first: str, second: str) -> Tuple[bool, Dict[str, int]]:
    difference = Counter(first) - Counter(second)
    difference.subtract(Counter(second) - Counter(first))
    return not difference, {char: count for char, count in difference.items() if count}


def mock_07_matrix_summaries(
    matrix: Sequence[Sequence[float]],
) -> Tuple[List[float], List[float], Tuple[int, int]]:
    rows, columns = _matrix_shape(matrix)
    if not rows or not columns:
        raise ValueError("Matrix must not be empty")
    row_sums, column_sums = matrices_06_row_and_column_sums(matrix)
    largest_position = max(
        ((row, column) for row in range(rows) for column in range(columns)),
        key=lambda position: matrix[position[0]][position[1]],
    )
    return row_sums, column_sums, largest_position


def mock_08_bracket_error_index(text: str) -> Optional[int]:
    openings = {"(": ")", "[": "]", "{": "}"}
    closings = {closing: opening for opening, closing in openings.items()}
    stack: List[Tuple[str, int]] = []
    for index, char in enumerate(text):
        if char in openings:
            stack.append((char, index))
        elif char in closings:
            if not stack or stack[-1][0] != closings[char]:
                return index
            stack.pop()
    return stack[0][1] if stack else None


def mock_09_second_salary_and_average(employees: Sequence[Tuple[str, float]]) -> Tuple[Optional[str], float]:
    if not employees:
        return None, 0.0
    salaries = sorted({salary for _, salary in employees}, reverse=True)
    second_salary = salaries[1] if len(salaries) > 1 else None
    second_name = next((name for name, salary in employees if salary == second_salary), None)
    average = sum(salary for _, salary in employees) / len(employees)
    return second_name, round(average, 2)


def mock_10_unique_pairs_with_sum(values: Iterable[int], target: int) -> List[Tuple[int, int]]:
    numbers = set(values)
    return sorted((value, target - value) for value in numbers if value <= target - value and target - value in numbers)
