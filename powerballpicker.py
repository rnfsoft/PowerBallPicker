import random, datetime

def inp(par, rand, r1, r2):
    ans = 0
    while ans not in range(r1, r2):
        if ans != 0: print '%s has to be %d ~ %d' % (par, r1, r2-1)
        ans = int(raw_input("\nEnter date of your %s. %s: " % (rand, par)))
    return ans    
        
def pick_list_validate(l, m, n):
    while True:
        if m in l or m == 0: m = random.randint(1,n) 
        return m        
    
pick_list = []
rand_list =['birthday', 'anniversary', 'vacation', 'employee', 'random']
max_num = 69
max_powerball = 26
print 'Welcome to Power Ball Picker.'
count = 0

while True:
    if count != 0: 
        quit = raw_input('Would you like to quit(Y|N)?').upper()
    
    if quit == 'Y': break
    count += 1
    # Select a speical description from list
    rand = random.choice(rand_list)
    
    # Enter a special month
    month = inp('Month', rand, 1, 13)
    month = pick_list_validate(pick_list, month, max_num)
    pick_list.append(month)
    
    # Enter a special day
    day = inp('Day', rand, 1, 32)
    day = pick_list_validate(pick_list, day, max_num)
    pick_list.append(day)

    # Enter a special year
    year = inp('Year', rand, 1900, 2100)
    year = year % max_num
    year = pick_list_validate(pick_list, year, max_num)
    pick_list.append(year)

    # current mins
    mins = int(datetime.datetime.now().minute * max_num / 60)
    mins = pick_list_validate(pick_list, mins, max_num)
    pick_list.append(mins)
    
    # current seconds    
    secs = int(datetime.datetime.now().second * max_num / 60)
    secs = pick_list_validate(pick_list, secs, max_num)
    pick_list.append(secs)

    print '\n\t************* Results *************'
    print '\tLucky Numbers are:', sorted(pick_list)
    print "\tPowerball is: ", random.randint(1, max_powerball), '\n'
    
    pick_list=[]



	
	
	



