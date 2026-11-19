# ---- Lesson 1 ----
def linear_search(items, target):
    """O(n): check every slot until a match."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1


def binary_search(a, target):
    """O(log n). `a` must be sorted."""
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1      # target is in the right half
        else:
            hi = mid - 1      # target is in the left half
    return -1                 # lo is now where target would be inserted


def two_sum(nums, target):
    """O(n) with a hash map: value -> index seen so far."""
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    return None

# Built-ins worth knowing:
#   set / dict        -> hash tables, O(1) average `in`
#   bisect.bisect_left(a, x) -> binary search for the insert position
#   collections.Counter(xs)  -> counts with a dict


# ---- Lesson 2 ----
def pair_with_sum(a, target):
    """Two pointers on a sorted list. O(n)."""
    lo, hi = 0, len(a) - 1
    while lo < hi:
        s = a[lo] + a[hi]
        if s == target:
            return lo, hi
        if s < target:
            lo += 1           # need a bigger sum
        else:
            hi -= 1           # need a smaller sum
    return None


def max_window_sum(a, k):
    """Fixed window of size k. O(n), whatever k is."""
    window = sum(a[:k])
    best = window
    for right in range(k, len(a)):
        window += a[right] - a[right - k]   # add new, drop old
        best = max(best, window)
    return best


def longest_unique(s):
    """Variable window: longest substring with no repeats. O(n)."""
    last = {}                 # char -> last index seen
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1   # jump past the duplicate
        last[ch] = right
        best = max(best, right - left + 1)
    return best
