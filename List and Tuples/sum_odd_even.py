# initializing list
test_list = [1,2,3,4,5]


odd_sum = 0
even_sum = 0

for ele in test_list:
	
		
# adding in particular summation according to value 
	if ele % 2 == 0:
		even_sum += int(ele)
	else:
		odd_sum += int(ele)

# printing result 
print("Odd digit sum : ",odd_sum)
print("Even digit sum : ",even_sum)
