#hashtable: TIME: O(M+N), SPACE: O(1)(atmost 26 characters)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        if countS != countT:
            return False
        return True      
    

#sorting TIME: O(nlogn + mlogm), space:O(1) or O(m+n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False    
        return sorted(s) == sorted(t)  
    

# one hashtable: TIME: O(M+N), SPACE: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord('a') - ord(s[i])] +=1
            count[ord('a') - ord(t[i])] -= 1
        for val in count:
            if val != 0:
                return False
        return True    