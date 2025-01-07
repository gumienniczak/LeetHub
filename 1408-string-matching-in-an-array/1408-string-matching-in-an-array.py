class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        output = set()
        current_word = None
        for i in range(n):
            current_word = words[i]
            for j in range(0,i):
                if words[i] in words[j]:
                    output.add(words[i])
            
            for j in range(i+1, n):
                if words[i] in words[j]:
                    output.add(words[i])
        return list(output)