import random

def shake_human(dict1, dict2):
	
	count1=1
	count2=1

	dict3={'woman':[], 'man':[]}
	dict3['woman']=[]
	dict3['man']=[]
	
	random.shuffle(dict1)
	random.shuffle(dict2)


	while count1<=4:
		for name in dict1:
			dict3['man'].append(name)
			count1=count1+1

	while count2<=4:
		for name in dict2:
			dict3['woman'].append(name)
			count2=count2+1


	print dict3

man_list = ["james", "jisu", "michael","david","messi"] 
woman_list = ["crystal", "ana", "hary", "julia","candy","jesica","petty"] 

shake_human(man_list, woman_list)

