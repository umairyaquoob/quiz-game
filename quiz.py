# Quiz game in Python

print('Hello, welcome to a Quiz!')
answer = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if answer.lower () == 'yes':
    answer = input('1. What is the best programming language? ')
    if answer.lower () == 'python':
        score +=1
        print('Correct')
    else:
        print('Incorrect')

    answer = input('2. What is 2 + 8 + 9 -1? ')
    if answer == '18':
        score +=1
        print('Correct')
    else:
        print('Incorrect')

    answer = input('3. What is better a 1050ti or 1060 (graphics card)? ')
    if answer.lower() == '1060':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    answer = input('4. Who came second in the stanely cup finals? ')
    if answer.lower() == 'knight' or answer.lower() == 'vegas':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    print('Thank you for playing, you got', score, 'questions correct')
    mark = (score/total_q) * 100

    print('Mark: ', str(mark) + '%')
print('Goodbye')
