#python3.6
import shelve, pprint

print('what is on your mind?')
currentThought = str(input())


shelfFile = shelve.open('stuffOnMind')

shelfThoughts  = shelfFile['thoughts']
#shelfFile['thoughts'] = shelfThoughts
#print(shelfThoughts)
shelfThoughts.append(currentThought)

print('would you like to see you past inputs? (yes = Y)')
more = str(input())

if more == 'Y':
    pprint.pprint(shelfThoughts)

shelfFile['thoughts'] = shelfThoughts
shelfFile.close()


'''
shelfFile = shelve.open('stuffOnMind')

shelfFile['thoughts'] = []

shelfFile['thoughts']

shelfFile.close()
'''
