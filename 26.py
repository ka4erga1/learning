def find_minimal_substring(s, c):
    
    shortest_length = len(s) + 1 
    
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            substring_char_set = set(s[i:j])
            
            if substring_char_set == set(c):
                length = j - i
                if length < shortest_length:
                    shortest_length = length
                    
    return shortest_length if shortest_length != len(s) + 1 else 0

s = input().strip()
c = input().strip()

result = find_minimal_substring(s, c)
print(result)