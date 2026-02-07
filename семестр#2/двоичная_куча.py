import heapq

class TopN:
    def __init__(self, N):
        self.N = N
        self.heap = []  # это min-heap (меньший элемент наверху)

    def add(self, value):
        if len(self.heap) < self.N:
            heapq.heappush(self.heap, value)                                                                                                                                                        
        else:
            if value > self.heap[0]:
                heapq.heappushpop(self.heap, value)

    def get_top_n(self):
        return sorted(self.heap, reverse=True)  # от большего к меньшему

    def pop_top(self):
        if self.heap:
            # найти и удалить наибольший (неэффективно, но работает)
            max_val = max(self.heap)
            self.heap.remove(max_val)
            heapq.heapify(self.heap)
            return max_val
        else:
            return None
