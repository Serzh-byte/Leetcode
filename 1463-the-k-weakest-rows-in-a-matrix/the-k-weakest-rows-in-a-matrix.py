class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = {}
        for i, row in enumerate(mat):
            total = sum(row)
            dic[i] = total

        sort = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}

        answer = []
        
        for key in sort.keys():
            answer.append(key)

        return answer[:k]