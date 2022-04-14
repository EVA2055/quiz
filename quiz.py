print('Welcome to my quiz contest!!!')
play = input('Do you want to play? yes/no: ').lower()


if play != 'yes':
    quit()
else:
    print('Ok lets start!')
    score = 0


ans = input('What is cpu? ').lower()
if ans == 'cpu':
    print('correct')
    score += 1
else:
    print('incorrect')
ans = input('What is ram? ').lower()
if ans == 'ram':
    print('correct')
    score += 1
else:
    print('incorrect')
ans = input('What is rom? ').lower()
if ans == 'rom':
    print('correct')
    score += 1
else:
    print('incorrect')
ans = input('What is www? ').lower()
if ans == 'www':
    print('correct')
    score += 1
else:
    print('incorrect')


print('your right answers are  '  +str(score))
print('your percentage  ' +str(score/4*100))