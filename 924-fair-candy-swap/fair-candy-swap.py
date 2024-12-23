class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        difference = (sum(aliceSizes) - sum(bobSizes))/2
        aliceSizes = set(aliceSizes)
        for candy in set(bobSizes):
            calc = candy + difference
            if calc in aliceSizes:
                return [calc, candy]
