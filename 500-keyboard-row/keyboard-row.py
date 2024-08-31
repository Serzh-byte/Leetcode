class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        second_row = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        third_row = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        answer = []
        for word in words:
            check = set(word.lower())
            if check&first_row == check or check&second_row == check or check&third_row == check:
                answer.append(word)
        return answer
