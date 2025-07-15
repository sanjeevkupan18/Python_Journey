# Function to Replace each vowel in
# the string with a specified character


def replaceVowelsWithK(test_str, K):

	# string of vowels
	vowels = 'AEIOUaeiou'

	# iterating to check vowels in string
	for ele in vowels:

		# replacing vowel with the specified character
		test_str = test_str.replace(ele, K)

	return test_str


# Driver Code
# input string
input_str = "COMPUTER"

# specified character
K = "#"

# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)

# printing output
print("After replacing vowels with the specified character:",
	replaceVowelsWithK(input_str, K))
