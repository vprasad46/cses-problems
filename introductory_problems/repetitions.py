

def longest_repeating_char_len(string):
    max_len = 1
    cur_len = 1
    cur_char = string[0]
    for char in string[1:]:
        if char == cur_char:
            cur_len += 1
        else:
            cur_char = char
            max_len = max(max_len, cur_len)
            cur_len = 1
    max_len = max(max_len, cur_len)
    return max_len




if __name__ == "__main__":
    dna = input()
    print(longest_repeating_char_len(dna))
