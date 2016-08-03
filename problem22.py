import sys

name_sum = 0

alpha_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
              'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

f = open('p022_names.txt', 'r')

file_contents = f.read()
file_contents = file_contents.split(',')

new_list = [item[1:-1] for item in file_contents]
sorted_list = sorted(new_list)

# use enumerate to give the index for multiplication, and to start at 1 as given in the problem definition
for index, name in enumerate(sorted_list, start=1):
    score = 0
    for char in name:
        score += alpha_dict[char]
    name_sum += score * index

print name_sum
