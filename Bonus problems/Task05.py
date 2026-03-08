def spam(intervals, number):
    for interval in intervals:
        parts = interval.split("|")
        start = int(parts[0])
        end = int(parts[1])

        if number in range(start, end):
            return True
        
    return False
        
print(spam(('1|3', '2|9', '11|15'), 55))   
        
