class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ch = ""
        max_ch = ""

        for j in range(len(s)):
            while s[j] in ch:
                ch = ch[1:]
                i += 1

            ch += s[j]
            max_ch = max(max_ch, ch, key=len)

        return len(max_ch)