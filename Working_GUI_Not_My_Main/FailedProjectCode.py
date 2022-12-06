import random

def simulate_game():

    # Possible Names of Contestants
    Contestant_Names = ['Bob','Jeff','Jason','Jackson','Megan','Lisa','Maddy','Ash','Naruto','Luffy','Goku','Percy','Jacky','Zoro','Madara','Ginny','Price','Graves','Ghost','Sif','Freya']

    good_pairs = {}
    perfect_pairs = {}
    bad_pairs = {}
    weeks = 0
    total_correct = 0

    set1 = set() #Creating set because sets don't allow duplicates 
    while len(set1) < 16:
        set1.add(Contestant_Names[random.randint(0, 20)])
    list1 = list(set1) #creating list in order to make a dictionary of perfect pairs

    # Create dictionary mapping contest to their pair
    for x in range(0, 16, 2):
        perfect_pairs.update({list1[x]: list1[x+1]})

    # makes sure to reshuffle the list, uses sample making sure not to change the original list
    shuffled = random.sample(list1, 16) 


    while True:

        # Take two contestants randomly
        Contestant1 = shuffled[random.randint(0, 15)] 
        Contestant2 = shuffled[random.randint(0, 15)]

        # If they are the same, or they have already been checked reselect
        while (Contestant1 == Contestant2 or 
                bad_pairs.get(Contestant1) == Contestant2 or 
                bad_pairs.get(Contestant2) == Contestant1 or
                good_pairs.get(Contestant1) == Contestant2 or
                good_pairs.get(Contestant2) == Contestant1):
            Contestant1 = shuffled[random.randint(0, 15)]
            Contestant2 = shuffled[random.randint(0, 15)] 

        # Check if the pair is a perfect pair given by the perfect pair dictionary
        if perfect_pairs.get(Contestant1) == Contestant2 or perfect_pairs.get(Contestant2) == Contestant1:
            good_pairs.update({Contestant1: Contestant2}) 
            total_correct += 1
        else:
            bad_pairs.update({Contestant1: Contestant2}) 

        if total_correct == 8: #when its all right it will stop
            break 
        
        #incrementing the week by 1
        weeks +=1 
    
    output = ""
    output += f"Perfect pair dictionary: {perfect_pairs}\n"
    output += f"Perfect pair dictionary: {perfect_pairs}\n"
    output += f"The Good dictionary: {good_pairs}\n" 

    output += f"weeks {weeks}"

    return output
        
if __name__ == "__main__":
    print(simulate_game())
