class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X' : 10,
            'V': 5,
            'I': 1
        }

        i = len(s) - 1
        prev_val = 0
        sum = 0

        while i >= 0:
            current_val = roman[s[i]]
            if current_val < prev_val:
                sum -= current_val
            else:
                sum += current_val
            prev_val = current_val
            i -= 1

        return sum
