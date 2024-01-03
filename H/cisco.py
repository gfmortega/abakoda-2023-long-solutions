from heapq import heappop, heappush
from typing import Optional

# Wrapper classes around Python's heapq library, because I like structs
class MinHeap:
    def __init__(self) -> None:
        self.a = []
        self.total = 0

    def push(self, x: int) -> None:
        heappush(self.a, x)
        self.total += x

    def pop_min(self) -> None:
        top = heappop(self.a)
        self.total -= top
        return top

    def min(self) -> int:
        return self.a[0]

    def empty(self) -> bool:
        return len(self.a) == 0

    def __len__(self):
        return len(self.a)

class MaxHeap:
    def __init__(self) -> None:
        self.min_heap = MinHeap()

    def push(self, x: int) -> None:
        self.min_heap.push(-x)

    def pop_max(self) -> None:
        return -self.min_heap.pop_min()

    def max(self) -> int:
        return -self.min_heap.min()

    def empty(self) -> bool:
        return self.min_heap.empty()

    def __len__(self) -> int:
        return len(self.min_heap)

    @property
    def total(self) -> int:
        return -self.min_heap.total

# Maintain the following two invariants at all times:
#  1) Everyone in left_heap is <= the median, everyone in right_heap is > the median
#  2) len(left_heap) - len(right_heap) = 0 or 1 
# That way, the median is always going to be the top element of the left heap
class MedianMaintainer:
    def __init__(self):
        self.left_heap = MaxHeap()
        self.right_heap = MinHeap()

    def median(self) -> Optional[int]:  # assumes the heaps are balanced
        return None if self.left_heap.empty() else self.left_heap.max()

    def total_distance_to_median(self) -> int:
        median = self.median()
        if median is None:
            return 0
        
        return (
            median*len(self.left_heap) - self.left_heap.total      # sum(median - x) = sum(median) - sum(x)
            + self.right_heap.total - median*len(self.right_heap)  # sum(x - median) = sum(x) - sum(median)
        )

    def balance(self):
        if len(self.left_heap) > len(self.right_heap) + 1:
            self.right_heap.push(self.left_heap.pop_max())
        elif len(self.right_heap) > len(self.left_heap):
            self.left_heap.push(self.right_heap.pop_min())

    def push(self, x: int):
        median = self.median()
        if median is None or x <= median:
            self.left_heap.push(x)
        else:
            self.right_heap.push(x)
        self.balance()

def solve(n, a):
    prefix_median_maintainer = MedianMaintainer()
    prefix_totals = [None for _ in range(n)]
    for i, x in enumerate(a):
        prefix_median_maintainer.push(x)
        prefix_totals[i] = prefix_median_maintainer.total_distance_to_median()

    suffix_median_maintainer = MedianMaintainer()
    suffix_totals = [None for _ in range(n)]
    for i, x in reversed(list(enumerate(a))):
        suffix_median_maintainer.push(x)
        suffix_totals[i] = suffix_median_maintainer.total_distance_to_median()
    
    return [prefix_totals[i] + suffix_totals[i+1] for i in range(n-1)]

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(*solve(n, [a[i]-b[i] for i in range(n)]))

