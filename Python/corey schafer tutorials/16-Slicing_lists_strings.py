my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# -index -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# ^^^ --->>> index-len(list) = -index
# list[start:end:step]
# end is non inclusive

print('\n', my_list[0:9:2])  # step
print('\n', my_list[3:8])  # interval
print('\n', my_list[-7:-2])  # reverse index
print('\n', my_list[1:-2])  # mix index
print('\n', my_list[5:])  # undefined end
print('\n', my_list[-5:])  # undefined end r-index
print('\n', my_list[:-3])  # undefined start
print('\n', my_list[:7])  # undefined start
print('\n', my_list[:])  # undefined indexing

# Running in reverse requires mixing negative and positive index use
# and negative step value

print('\n', my_list[2:-1:-1])  # this returns none
print('\n', my_list[9:2:-1])   # 9 to 3
print('\n', my_list[-1:2:-1])  # 9 to 3 [unnecesarry]

print('\n', my_list[::-1])  # entire list reverse

sample_str = 'testing string is a cool made up bunch of words'

print('\n', sample_str)

# reverse the str
print('\n', sample_str[::-1])

# get last 6 caharacters
print('\n', sample_str[-6:])

# get first 5 characters
print('\n', sample_str[:5])

# get from 4'th to second last char

print('\n', sample_str[4:-2])
