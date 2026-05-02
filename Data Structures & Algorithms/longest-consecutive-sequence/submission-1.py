class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        m_dict = defaultdict(int)
        res = 0
        for i in nums:
            if  not  m_dict[i]:
                m_dict[i] = m_dict[i-1] + m_dict[i+1] +1
                m_dict[i-m_dict[i-1]] = m_dict[i]
                m_dict[i+m_dict[i+1]] = m_dict[i]
            res = max(res,m_dict[i])
        
        return res
