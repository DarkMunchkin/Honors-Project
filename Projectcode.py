import random


Contestants = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def pop_random(list):
    idx = random.randrange(0, len(list))
    return list.pop(idx)
def pairs(list):
    pairs = []
    while list:
        rand1 = pop_random(list)
        rand2 = pop_random(list)
        pair = (rand1, rand2)
        pairs.append(pair)
        return pair
def truth_booth(list): #random pair list
    test_list = []
    for i in range(len(list)):
        try:
            x,y = input("Enter two contestants: ").split()
            break
        except ValueError:
            print("\nThis is not a number. Try again...")
            print()
        test_list.append((x, y))
    return test_list
def bad_list(xlist, ylist): #truth booth list, perfect list
    match = []
    for i in xlist:
        if i not in ylist:
            match.append(i)
    return match
def per_num_pairs(x, y): #random pair list, perfect pair list
    num = 0
    for i in x:
        if i in y:
            num += 1
    return num
# Algorithm 1
for x in range(len(Contestants)//2):
    weeks = 0
    perfect_pairs = pairs(Contestants)
    if weeks == len(Contestants)//2:
        print('Game Over, You Lose!!!')
    elif len(rand_pairs) == 0:
        print('Game Over, You Win!!!')
    else:
        rand_pairs = pairs(Contestants)
        print(per_num_pairs(rand_pairs, perfect_pairs))
        d_list = bad_list(truth_booth(rand_pairs),perfect_pairs)
        rand_pairs = d_list
        weeks +=1
# Algorithm 2

