class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
       
        citations.sort(reverse=True)
        
        h = 0
        for i, cite_count in enumerate(citations):
            if cite_count >= i + 1:
                h = i + 1
            else:
                break
                
        return h