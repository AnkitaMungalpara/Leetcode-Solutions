"""
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Solution:
Time Complexity: O(N+M)
Space Complexity: O(N+M)

"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazineDict = {}
        for ch in magazine:
            if ch not in magazineDict:
                magazineDict[ch] = magazine.count(ch)

        ransomNoteDict = {}
        for ch in ransomNote:
            if ch not in ransomNoteDict:
                ransomNoteDict[ch] = ransomNote.count(ch)

        for ch in ransomNote:
            if ch not in magazineDict:
                return False
            elif ch in magazineDict:
                if ransomNoteDict[ch] > magazineDict[ch]:
                    return False
        
        return True
      
