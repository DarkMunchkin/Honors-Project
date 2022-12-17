import random
import time
class GameSimulator:

    def __init__(self):

        Contestant_Names = ['Bob','Jeff','Jason','Jackson','Megan','Lisa','Maddy','Ash','Naruto','Luffy','Goku','Percy','Jacky','Zoro','Madara','Ginny','Price','Graves','Ghost','Sif','Freya']
        
        # pick 16 random contestants
        self.contestants = random.sample(Contestant_Names, 16)
        
        # randomly create 8 perfect pairs store in dictionary
        self.perfect_pairs = self.get_random_pairing(self.contestants)

    def get_random_pairing(self, contestants):
        """ Given a list of contestants, returns a dictionary representing a random pairing of contestants.
            Number of contestants must be even
        """

        # Shuffle your contestants list
        shuffled = random.sample(contestants, len(contestants)) 
        pairs = {}

        # Create dictionary mapping contesants to their pair
        for x in range(0, len(contestants), 2):
            pairs.update({shuffled[x]: shuffled[x+1]})

        return pairs

    def truth_booth(self, contestant1, contestant2):
        """ Takes two contestant names and returns whether or not they are a perfect match.
        """
        return self.perfect_pairs.get(contestant1) == contestant2 or self.perfect_pairs.get(contestant2) == contestant1

    def get_num_correct_pairings(self, pairings):
        """ Takes a dictionary of pairings and returns the number of correct pairings.
        """
        counter = 0
        for contestant1, contestant2 in pairings.items():
            if self.truth_booth(contestant1,contestant2):
                counter +=1
        return counter
    start1 = time.time()
    def simulate_game_random(self):
        """ Simulates the game, given that contestants pick their matches randomly.
            If contestants find their perfect match, they stay the same.
            Returns the number of weeks.
        """

        weeks = 0

        # list of unmatched contestants
        unmatched_contestants = self.contestants.copy()

        # dictionary of matched contestants
        matched = {}

        while True:

            print(f"Week # {weeks}")

            # get random pairing from remaining unmatched contestants
            random_pairing = self.get_random_pairing(unmatched_contestants)

            # merge with dictionary of matched contestants
            all_pairings = {**matched, **random_pairing}

            print(f"This weeks pairings: {all_pairings}")

            # get random pair from dictionary and run through truth booth
            contestant1, contestant2 = random.choice(list(random_pairing.items()))
            print(f"Contestants {contestant1} and {contestant2} selected for truth booth.")

            if self.truth_booth(contestant1, contestant2):
                matched.update({contestant1: contestant2})
                unmatched_contestants.remove(contestant1)
                unmatched_contestants.remove(contestant2)
                print("They are a perfect match!")
            else:
                print(f"{contestant1} and {contestant2} are not a perfect match.")


            n_correct_pairings = self.get_num_correct_pairings(all_pairings) 
            print(f"{n_correct_pairings} correct pairings this round.")
            
            if n_correct_pairings == 8:
                break

            weeks += 1

        return weeks
    end1 = time.time()
    start2 = time.time()
    def simulate_game_try_all_pairs(self):
        """ Simulates the game by making a list of all possible couples.
            Each round one of the couples gets sent to the truth booth. 
            If they are a match, all pairs containing that couple are removed from list of possible combinations.
        """
        weeks = 0

        # Create list of tuples with all possible pairings
        all_possible_couples = []
        for contestant1 in self.contestants:
            for contestant2 in self.contestants:
                if contestant1 != contestant2:
                    all_possible_couples.append((contestant1,contestant2))

        while len(all_possible_couples) > 0:

            print(f"Week # {weeks}")

            pair = all_possible_couples.pop()

            print(f"Contestants {pair[0]} and {pair[1]} selected for truth booth.")

            if self.truth_booth(pair[0], pair[1]):
                print("They are a perfect match!")

                # If we find two contestants are matched, we do not need to check any other pairs with those contestants
                # Remove these pairs from all possible couples
                for couple in all_possible_couples:
                    if couple[0] == pair[0] or couple[1] == pair[0] or couple[0] == pair[1] or couple[1] == pair[1]:
                        all_possible_couples.remove(couple)

            else:
                print(f"{pair[0]} and {pair[1]} are not a perfect match.")

            weeks += 1
        return weeks
    end2 = time.time()
    start3 = time.time()
    def simulate_game_pairs(self):
        """ Simulates the game by making a list of all possible couples.
            Each round one of the couples gets sent to the truth booth. 
            If they are a match, all pairs containing that couple are removed from list of possible combinations.
            However this time the game will get rid of the first perfect pair's contestants on the list every 25 weeks
            This will reduce the weeks
        """
        weeks = 0

        # Create list of tuples with all possible pairings
        all_possible_couples = []
        for contestant1 in self.contestants:
            for contestant2 in self.contestants:
                if contestant1 != contestant2:
                    all_possible_couples.append((contestant1,contestant2))


        while len(all_possible_couples) > 0:

            print(f"Week # {weeks}")

            pair = all_possible_couples.pop()
            pair1 = self.perfect_pairs.copy()
            if weeks % 25:
                for key, value in pair1.items():
                    for couple in all_possible_couples:
                        if couple[0] == key or couple[1] == key or couple[0] == value or couple[1] == value:
                            all_possible_couples.remove(couple)
                    break
                
            print(f"Contestants {pair[0]} and {pair[1]} selected for truth booth.")

            if self.truth_booth(pair[0], pair[1]):
                print("They are a perfect match!")

                # If we find two contestants are matched, we do not need to check any other pairs with those contestants
                # Remove these pairs from all possible couples
                for couple in all_possible_couples:
                    if couple[0] == pair[0] or couple[1] == pair[0] or couple[0] == pair[1] or couple[1] == pair[1]:
                        all_possible_couples.remove(couple)

            else:
                print(f"{pair[0]} and {pair[1]} are not a perfect match.")

            weeks += 1

        return weeks
    end3 = time.time()


if __name__ == "__main__":

    n_times = 100
    weeks_random = 0
    weeks_all = 0
    weeks_pairs = 0
    median_weeks_random = []
    median_weeks_all = []
    median_weeks_pairs = []
    for i in range(n_times):
        # Compare all three algorithms using average number of weeks
        simulator = GameSimulator()
        weeks_random += simulator.simulate_game_random()
        weeks_all +=  simulator.simulate_game_try_all_pairs()
        weeks_pairs += simulator.simulate_game_pairs()
        median_weeks_random.append(simulator.simulate_game_random())
        median_weeks_all.append(simulator.simulate_game_try_all_pairs())
        median_weeks_pairs.append(simulator.simulate_game_pairs())
        
        

    avg_weeks_random = weeks_random/n_times
    avg_weeks_all = weeks_all/n_times
    avg_weeks_pairs = weeks_pairs/n_times 
    median_random = statistics.median(median_weeks_random)
    median_all = statistics.median(median_weeks_all)
    median_pairs = statistics.median(median_weeks_pairs)

    std_dv_random = statistics.stdev(median_weeks_random)
    std_dv_all = statistics.stdev(median_weeks_all)
    std_dv_pairs = statistics.stdev(median_weeks_pairs)
    print(f'Average Weeks for Random Algorithm :', (avg_weeks_random))
    print(f'Average Weeks for Try All Algorithm:', (avg_weeks_all))
    print(f'Average Weeks for Pairs Algorithm:', (avg_weeks_pairs))
    print(f"Time for Random Algorithm: {simulator.end1 - simulator.start1} seconds")
    print(f"Time for Try All Algorithm: {simulator.end2 - simulator.start2} seconds")
    print(f"Time for Pairs Algorithm: {simulator.end3 - simulator.start3} seconds")
    print(f'Median Weeks for Random Algorithm :', (median_random))
    print(f'Median Weeks for Try All Algorithm:', (median_all))
    print(f'Median Weeks for Pairs Algorithm:', (median_pairs))
    print(f'Standard Deviation of Weeks for Random Algorithm :', (std_dv_random))
    print(f'Standard Deviation of Weeks for Try All Algorithm:', (std_dv_all))
    print(f'Standard Deviation of Weeks for Pairs Algorithm:', (std_dv_pairs))
    median_random = statistics.median(median_weeks_random)
    median_all = statistics.median(median_weeks_all)
    median_pairs = statistics.median(median_weeks_pairs)

    std_dv_random = statistics.stdev(median_weeks_random)
    std_dv_all = statistics.stdev(median_weeks_all)
    std_dv_pairs = statistics.stdev(median_weeks_pairs)



