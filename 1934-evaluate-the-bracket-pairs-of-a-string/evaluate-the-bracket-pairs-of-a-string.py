class Solution(object):
    def evaluate(self, s, knowledge):
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        result = ''
        key = ''
        inside = False

        for ch in s:
            if ch == '(':
                inside = True
                key = ''

            elif ch == ')':
                inside = False
                result += mp.get(key, '?')

            elif inside:
                key += ch

            else:
                result += ch

        return result