def bubble_sort(input_list):

#Swap the element to arrange in order

	for iter_num in range(len(list)-1,0,-1):
		for idx in range(iter_num):
			if input_list[idx]>input_list[idx+1]:
				temp = input_list[idx]
				input_list[idx] = input_list[idx+1]
				input_list[idx+1] = temp

list = [9,8,7,6,5,4,3,2,1]
bubble_sort(list)
print(list)