def areAnagram(str1, str2):
	#find lengths of both strings
	n1 = len(str1)
	n2 = len(str2)

	# If length is not same,
	# they cannot be anagram
	if n1 != n2:
		return 0

	# Sort both strings
	str1 = sorted(str1)
	str2 = sorted(str2)

	# Compare sorted strings
	for i in range(0, n1):
		if str1[i] != str2[i]:
			return 0

	return 1


#test code
str1 = "test"
str2 = "ttew"

#fuction call
if areAnagram(str1, str2):
	print("The two strings are anagram of each other")
else:
	print("The two strings are not anagram of each other")


