'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

def romanToInt(s: str) -> int:
    roman_to_int = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    total = 0
    n = len(s)
    
    for i in range(n):
        if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
            total -= roman_to_int[s[i]]
        else:
            total += roman_to_int[s[i]]
    return total

print(romanToInt("III"))       
print(romanToInt("LVIII"))     
print(romanToInt("MCMXCIV"))  

# ----

def romanToInt(s2):
    I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
    dict_rome = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
                 '-I':1, '-V':5, '-X':10, '-L':50, '-C':100, '-D':500, '-M':1000}
    tmp_dict = dict()
    ch = s2[0]    
    
    for index, s in enumerate(s2):  
        if dict_rome.get(ch, 0) < dict_rome.get(s, 0):
            tmp_dict[f'-{ch}'] = -(abs(tmp_dict.get(f'-{ch}', 0)) + 2)
            tmp_dict[s] = tmp_dict.get(s, 0) + 1
        else:
            tmp_dict[s] = tmp_dict.get(s, 0) + 1
        ch = s
    common_keys = set(tmp_dict.keys()) & set(dict_rome.keys())
    result = {key: tmp_dict[key] * dict_rome[key] for key in common_keys}
    total_sum = sum(result.values())
    return total_sum

print(romanToInt("III")) 
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))

