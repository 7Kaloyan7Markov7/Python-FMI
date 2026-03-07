floating_number = input()
parts = floating_number.split('.')
whole_part = int(parts[0])
dec_part = int(parts[1])

answer = {'whole_part': whole_part, 'dec_part' : dec_part}
