class Solution:
    def intToRoman(self, num: int) -> str:
        intToRoman = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
            50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
            1000: 'M'
        }
        result = ""
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for value in values:
            while num >= value:
                result += intToRoman[value]
                num -= value

        return result
print(Solution().intToRoman(1000))
print(Solution().intToRoman(4))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))