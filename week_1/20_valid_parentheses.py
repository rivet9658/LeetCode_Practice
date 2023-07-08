# package import
from typing import List


# my first answer
def is_valid(s: str) -> bool:
    temp_list = []
    for t in s:
        temp_list.append(t)
        if temp_list[-1] in [')', ']', '}'] and len(temp_list) > 1:
            if temp_list[-2] == '(' and temp_list[-1] == ')':
                temp_list = temp_list[:-2]
            elif temp_list[-2] == '[' and temp_list[-1] == ']':
                temp_list = temp_list[:-2]
            elif temp_list[-2] == '{' and temp_list[-1] == '}':
                temp_list = temp_list[:-2]
    if len(temp_list) > 0:
        return False
    return True


# my second answer
def update_1_is_valid(self, s: str) -> bool:
    check_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    t = ''
    for i in range(len(s)):
        t += s[i]
        if s[i] in [')', ']', '}'] and len(t) > 1:
            if check_dict[s[i]] != t[-2]:
                return False
            t = t[:-2]
    if len(t) > 0:
        return False
    return True
