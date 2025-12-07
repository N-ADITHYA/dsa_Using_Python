class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        isFCaps = 0
        isFFSmall = 0
        isFFCaps = 0

        for i, ch in enumerate(word):
            if i == 0 and ch.isupper():
                isFCaps = 1
                isFFCaps += 1
            else:
                if ch.islower():
                    isFFSmall += 1
                elif ch.isupper():
                    isFFCaps += 1

        if len(word) == isFFCaps:  # ALL CAPS
            return True
        elif len(word) == (isFCaps + isFFSmall):  # First caps + rest small
            return True
        elif len(word) == isFFSmall:  # all small
            return True
        return False
