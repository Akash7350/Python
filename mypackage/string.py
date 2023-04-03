def countwords(s):
	cnt=1
	for i in s:
		if i==' ' or i=='\t' or i=='\n':
			cnt=cnt+1
	return cnt
def toggle(s):
	s1=""
	for i in s:
		if i==' ':
			s1=s1+i
		if i.isalpha():
			if ord(i)>=65 and ord(i)<=90:
				s1=s1+chr(ord(i)+32)
			else :
				s1=s1+chr(ord(i)-32)
	return s1											
