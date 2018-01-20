import os

note='./huozai_note.md'
data = open(note,'rt').readlines()
date_index_list = []
for index,line in enumerate(data):
    if line.startswith('201'):
        date_index_list.append(index)
with open(note,'w') as f:
    for date_index in date_index_list:
        f.writelines(data[:date_index])
        f.writelines(data[date_index+1:])
