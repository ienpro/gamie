Ex) 5.1

>>> def print_n(s, n):
	if n <= 0:
		return
	print(s)
	print_n(s,n-1)

	
>>> s="Hello"
>>> print_n(s,2)
Hello
Hello


Ex) 5.2

>>> def do_n(a,n):
	if n<=0:
		print("실행종료")
	else:
		a
		do_n(a,n-1)

>>>def Hi(type)
print(type)

Ex) 5.3

```
def check_fermat(a,b,c,n):
    if n>2:
        if a**n + b**n == c**n:
            print("페르마가 틀렸다!")
        elif a**n + b**n != c**n:
            print("아냐, 그건 아니지.")
    else:
        print("n은 2보다 커야 합니다")
```

Ex) 5.4

>>> def is_triangle(a, b, c):
	if a >= b >= c or a >= c >= b:
		if a < b + c:
			print("Yes")
		else :
			print("No")

	if b >= a >= c or b >= c >= a:
		if b < a + c:
			print("Yes")
		else :
			print("No")

	if c >= a >= b or c >= b >= a:
		if c < a + b:
			print("Yes")
		else:
			print("No")
