class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_num = {}

        for num in nums:
            if num in freq_num:
                freq_num[num] += 1
            else:
                freq_num[num] = 1

        cnt = 0
        ans = []
        while cnt < k:
            data = max(freq_num, key=freq_num.get)
            ans.append(data)
            del freq_num[data]
            cnt += 1
        
        return ans



