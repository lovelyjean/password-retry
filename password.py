password = 'a123456'
x = 3

while x > 0:
	pw = input('please input password: ')
	x = x - 1
	if pw == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤 還有', x, '次機會')
