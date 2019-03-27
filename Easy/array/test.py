import heapq

alist = []
heapq.heappush(alist, 3)
heapq.heappush(alist, 2)
heapq.heappush(alist, 3)

print(heapq.heappop(alist))
