class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        output = []
        for word in words:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
        
        sorted_counter = sorted(counter.items(), key = lambda x: (-x[1], x[0]))

        for i, element in enumerate(sorted_counter):
            if i < k:
                output.append(element[0])

        return output