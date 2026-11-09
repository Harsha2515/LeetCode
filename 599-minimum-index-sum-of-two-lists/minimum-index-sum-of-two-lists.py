class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:

        count = [float('inf')] * len(list1)

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    count[i] = i + j

        k = min(count)

        result = []

        for i in range(len(count)):
            if count[i] == k:
                result.append(list1[i])

        return result