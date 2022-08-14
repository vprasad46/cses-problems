import heapq
from collections import defaultdict


class FileProcessor:
    def __init__(self):
        self.collection_size = defaultdict(int)
        self.file_collection = defaultdict(list)
        self.total_processed = 0

    def process_file(self, file_name, size, collection=None):
        if not collection:
            collection = ["<def>"]
        self.total_processed += size
        for c in collection:
            if c != "<def>":
                self.collection_size[c] += size
            self.file_collection[c].append((file_name, size))


    def get_top_k(self, k):
        top_k = [(-size, collection) for collection, size in self.collection_size.items()]
        heapq.heapify(top_k)

        while top_k and k:
            size, c = heapq.heappop(top_k)
            print(c, -size)
            k -= 1

