def CheckStr(Str):
	i=0

	for a in Str:
		
		i=i+1

		if a!=Str[len(Str)-i]:
			print'diffrent'
			break;
	
		elif i==len(Str):
			print'same'
		


CheckStr('aha')
CheckStr('bha')