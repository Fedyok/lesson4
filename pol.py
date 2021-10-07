def palindrome(st):
	if st[::-1] == st:
		return True
	else:
		return False
	for elem in st:
		print(elem)
print(palindrome("шалаш"))
