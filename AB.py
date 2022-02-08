import random
ans = []

numbers = []

for i in range(0, 10):
    numbers.append(i)
for i in range(4):
    j = random.randint(0, len(numbers) - 1)
    ans.append(numbers.pop(j))

flag = 0

# print(ans)

while flag == 0:
    guess = list(input())
    if len(guess) != 4:
        print('invalid number')
    else:
        invalid = 0
        for i in range(4):
            if '0' > guess[i] or '9' < guess[i]:
                print('invalid number')
                invalid = 1
                break
            else:
                if invalid == 0:
                    for j in range(i+1, 4):
                        if guess[i] == guess[j]:
                            print('invalid number')
                            invalid = 1
                            break
        if invalid == 0:
            A = 0
            B = 0
            sort_ans = sorted(ans)
            sort_guess = sorted(guess)        
            for i in range(4):
                for j in range(4):
                    if int(guess[i]) == ans[j]:
                        B += 1
            for i in range(4):
                if int(guess[i]) == ans[i]:
                    A += 1
                    B -= 1
            print('{As}A{Bs}B'.format(As=A, Bs=B))
            if A == 4:
                flag = 1