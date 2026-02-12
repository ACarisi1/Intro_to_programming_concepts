

def roman_convert(s: str) -> int:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    if not s:
        return -1

    s = s.upper()

    # Rule 1: valid characters
    for ch in s:
        if ch not in roman_map:
            return -1

    total = 0
    repeat_count = 1

    for i in range(len(s) - 1):
        curr = s[i]
        next_ = s[i + 1]

        curr_val = roman_map[curr]
        next_val = roman_map[next_]

        # Rule 2 & 3: repetition rules
        if curr == next_:
            repeat_count += 1
            if curr in "VLD" or repeat_count > 3:
                return -1
        else:
            repeat_count = 1

        # Rule 4 & 5: subtraction rules
        if curr_val < next_val:
            if curr not in "IXC":
                return -1
            if (curr == 'I' and next_ not in "VX") or \
               (curr == 'X' and next_ not in "LC") or \
               (curr == 'C' and next_ not in "DM"):
                return -1
            if repeat_count > 1:
                return -1
            total -= curr_val
        else:
            total += curr_val

    total += roman_map[s[-1]]
    return total


while True:
    s = input()
    roman_convert(s)
    if s == "FIN":
        break
    print(roman_convert(s))
