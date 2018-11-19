#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		#filereader = csv.reader(csv_in_file)
		filecont_lst = list(filereader)
		filecont_head = filecont_lst[0]
		head_lth = len(filecont_head)
		
		filewriter = csv.writer(csv_out_file, delimiter=',')
		for row_list in filecont_lst:
			if len(row_list) > head_lth:
				l3 = row_list[:3]
				lmid = row_list[3:len(row_list)-1]
				lend = row_list[len(row_list)-1]
				lm = ','.join(lmid)
				l3.append(lm)
				l3.append(lend)
				print(l3)
				filewriter.writerow(l3)
			else:
				print(row_list)
				filewriter.writerow(row_list)
