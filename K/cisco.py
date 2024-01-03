from heapq import heappush, heappop

def process(queue, k):
    done_times = []
    for service_time in queue[:k]:
        heappush(done_times, service_time)
    for service_time in queue[k:]:
        heappush(done_times, heappop(done_times) + service_time)
    return max(done_times)

def solve(n, finish_by, queue):
    def is_good(k):
        return process(queue, k) <= finish_by

    if not is_good(n):
        return -1
    # Find the smallest good(k)
    L, R = 1, n
    while L != R:
        M = (L + R) // 2
        if is_good(M):
            R = M
        else:
            L = M+1
    return L

if __name__ == '__main__':
    for _ in range(int(input())):
        n, finish_by = map(int, input().split())
        queue = [int(x) for x in input().split()]
        print(solve(n, finish_by, queue))
