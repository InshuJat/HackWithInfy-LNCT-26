class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        
        char_map = {}  
        max_length = 0
        left = 0

        for right in range(len(s)):
            current_char = s[right]
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1
            
            char_map[current_char] = right
            
            current_window_size = right - left + 1
            if current_window_size > max_length:
                max_length = current_window_size

        return max_length