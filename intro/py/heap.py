# Heaps
import heapq

# under the hood of arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap) # 2, 3, 4

while len(minHeap):
    print(heapq.heappop(minHeap))

# Max heap
maxHeap = []
heapq.heappush(maxHeap, -1 * 3)
heapq.heappush(maxHeap, -1 * 2)
heapq.heappush(maxHeap, -1 * 4)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 *heapq.heappop(maxHeap))