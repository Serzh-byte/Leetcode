class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hashmap = {}
        count = 0
        for hour in hours:
            rem = hour % 24
            check = (24 - rem) % 24 
            if check in hashmap:
                count += hashmap[check]
            if rem in hashmap:
                hashmap[rem] += 1
            else:
                hashmap[rem] = 1
        
        return count
