import heapq

heap = []

heapq.heappush(heap, 40)
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)
heapq.heappush(heap, 20)
heapq.heappush(heap, 50)

while heap:
    numero = heapq.heappop(heap)
    print(numero)