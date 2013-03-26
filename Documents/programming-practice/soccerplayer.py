def dict_loop(dict):
	dict2={'30s':[], '20s':[]}
	dict2['30s']=[]
	dict2['20s']=[]
	
	for name in dict:
		if dict[name]>=30:
				dict2['30s'].append(name)

		else:
			dict2['20s'].append(name)
	
	print dict2

soccerplayer={'henry':35, 'villa':30, 'xavi':32, 'iniesta':30, 'ronaldo':27, 'messi':26}

dict_loop(soccerplayer)
