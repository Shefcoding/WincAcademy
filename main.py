# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
Goalscorer1 = 'Gullit'
Goalscorer2 = 'Van Basten'
Goal_0 = 32
Goal_1 = 54
Scorers = Goalscorer1 + ' '+ str(Goal_0) + ','+ Goalscorer2 + ' '+ str(Goal_1)
print(Scorers)
report = f'{Goalscorer1} scored in the {Goal_0}nd minute \n{Goalscorer2} scored in the {Goal_1}th minute '

print(report)
player = 'Ronald Koeman'
first_name = player[player.find('Ronald'):6]

last_name_len = len(player[player.find('Koeman'):13])


name_short = player[0]+'. '+ player[player.find('Koeman'):13]
chant = f'\t {first_name}!' * len(first_name)
good_chant= chant[len(chant)-1] != ' '
print(good_chant)