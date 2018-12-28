import random

def eldritchify():
        namelist = []
        name  = str.lower(input('whats yr name \n'))
        for n in name:
                namelist.append(n)
        eldritchlist = []
        i = 0
        while i < len(namelist):
                eldritchlist.append(random.choice(namelist))
                i+=1
        print('your eldritch name is....')
        i = 0
        while i < len(eldritchlist):
                print(str(eldritchlist[i]),sep=' ', end='', flush=True)
                i +=1
        print('\n')
        q = str.lower(input('run again? y/n \n'))
        if q == 'y' or q == 'yes':
                eldritchify()
        else:
                print('ok bye')
	
eldritchify()
