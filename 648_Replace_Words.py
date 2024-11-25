"""
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. 
For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. 
If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Solution:
Time Complexity: O(N*M)
Space Complexity: O(N*M)

"""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        lst = []
        hashmap = {}

        for i in sentence.split():
            hashmap[i] = i
            sub = i
            for j in range(len(sub)-1, -1, -1):
                if sub[:j+1] in dictionary:
                    hashmap[i] = sub[:j+1]

            lst.append(hashmap[i])

        return ' '.join(lst)
