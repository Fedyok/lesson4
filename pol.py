def palindrome(st):
	for elem in st:
		print(elem)

	if st[::-1] == st:
		return True
	else:
		return False

print(palindrome("шалаш"))
