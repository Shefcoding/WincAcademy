# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
Goalscorer1 = 'Ruud Gullit'
Goalscorer2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = Goalscorer1 +' '+ str(goal_0) + ', '+ Goalscorer2 + ' '+ str(goal_1)
print(scorers)
report = f'{Goalscorer1} scored in the {goal_0}nd minute\n{Goalscorer2} scored in the {goal_1}th minute'

print(report)
player = 'Ronald Koeman'
first_name_search = player.find(' ')
first_name = player[:first_name_search]
print(first_name)

last_name_len =len(player[first_name_search:])-1
print(last_name_len)

name_short = player[0]+'.'+ player[first_name_search:]
chant = (f'{first_name}! ' *len(first_name))[:-1] 
print(chant)
good_chant= chant[-1] != ' '
print(good_chant) 
