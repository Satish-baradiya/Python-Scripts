def insertion_sort(input_list):

	for i in range(1,len(input_list)):
		j = i-1
		nxt_element = input_list[i]

		while (input_list[j] > nxt_element) and (j>=0):
			input_list[j+1] = input_list[j]
			j =j-1
		input_list[j+1] = nxt_element


list = [9,8,7,6,5,4,3,2,1]
insertion_sort(list)
print(list)
