def longest_run(lst):
    if not lst:
        return 0
    
    max_len = 1
    current_len = 1
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1
    
    return max_len
