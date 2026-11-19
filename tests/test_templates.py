"""Randomized checks: every template must agree with a brute-force answer.

Run with either:
    python3 tests/test_templates.py
    pytest
"""
import itertools
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from templates import (binary_search, linear_search, longest_unique,  # noqa: E402
                       max_window_sum, pair_with_sum, two_sum)

ROUNDS = 2000
rng = random.Random(0)

NAMES = ["kai", "zoe", "ravi", "ben", "priya", "leo", "sam", "nora",
         "theo", "ivy", "ana", "maya", "jules", "eli", "fern", "quinn"]


def test_lesson_data():
    """The numbers the lesson page displays."""
    assert linear_search(NAMES, "maya") == 11
    assert linear_search(NAMES, "omar") == -1
    assert pair_with_sum([2, 3, 5, 8, 11, 13, 17, 19, 23, 29], 30) == (4, 7)
    assert max_window_sum([4, 2, 7, 1, 8, 3, 6, 5, 9, 2], 4) == 23
    assert longest_unique("abcbdeaf") == 6
    assert longest_unique("pwwkew") == 3


def test_binary_search():
    s = sorted(NAMES)
    for t in s:
        assert s[binary_search(s, t)] == t
    for _ in range(ROUNDS):
        a = sorted(rng.sample(range(100), rng.randint(0, 15)))
        x = rng.randint(-5, 105)
        r = binary_search(a, x)
        assert (r == -1) == (x not in a)
        assert r == -1 or a[r] == x


def test_two_sum():
    for _ in range(ROUNDS):
        n = [rng.randint(-9, 9) for _ in range(rng.randint(0, 10))]
        t = rng.randint(-10, 10)
        r = two_sum(n, t)
        exists = any(n[i] + n[j] == t for i, j in itertools.combinations(range(len(n)), 2))
        assert (r is not None) == exists
        assert r is None or (r[0] < r[1] and n[r[0]] + n[r[1]] == t)


def test_pair_with_sum():
    for _ in range(ROUNDS):
        a = sorted(rng.sample(range(60), rng.randint(0, 12)))
        t = rng.randint(0, 120)
        r = pair_with_sum(a, t)
        exists = any(a[i] + a[j] == t for i, j in itertools.combinations(range(len(a)), 2))
        assert (r is not None) == exists
        assert r is None or a[r[0]] + a[r[1]] == t


def test_max_window_sum():
    for _ in range(ROUNDS):
        a = [rng.randint(-9, 9) for _ in range(rng.randint(1, 12))]
        k = rng.randint(1, len(a))
        assert max_window_sum(a, k) == max(sum(a[i:i + k]) for i in range(len(a) - k + 1))


def test_longest_unique():
    for _ in range(ROUNDS):
        s = "".join(rng.choice("abcd") for _ in range(rng.randint(0, 12)))
        brute = max((j - i for i in range(len(s) + 1) for j in range(i, len(s) + 1)
                     if len(set(s[i:j])) == j - i), default=0)
        assert longest_unique(s) == brute


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"ok  {t.__name__}")
    print(f"All {len(tests)} test groups passed.")
