import random
import matplotlib.pyplot as plt

def card_value(number):
    ''' returns the value of a card according to their position in a list of 52 standard cards, defined by a table
        param number is any integer from 0 to 51
    '''
    if number not in list(range(52)):
        print("Not a valid card")
    elif number in ([0, 10, 20, 30, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]): # corresponds to a 10, J, Q, or K
        return 10
    elif number % 10 == 1: # corresponds to an ace
        return 1
    elif number % 10 == 2:
        return 2
    elif number % 10 == 3:
        return 3
    elif number % 10 == 4:
        return 4
    elif number % 10 == 5:
        return 5
    elif number % 10 == 6:
        return 6
    elif number % 10 == 7:
        return 7
    elif number % 10 == 8:
        return 8
    else:
        return 9

def player(cards):
    ''' returns the score of the player's hand calculated from the first two cards in the deck
        param cards is a list of integers
    '''
    ace_count = 0 # initializing the number of times the player draws an ace
    score = 0 # initializing total score

    for i in cards[0:2]:
        if card_value(i) == 1 and ace_count == 0:
            score += 11 # adds 11 to score for the first ace
            ace_count += 1
        else:
            score += card_value(i)

    return score
        

def dealer(cards):
    ''' returns the score of the dealer after drawing enough cards to have a hand equal to or greater than 17
        param cards is a list of integers
    '''

    score = 0 

    i = 2 

    while score < 17: 
        score += card_value(cards[i])
        
        i += 1 

    return score


num_games = 100000

# initialize player wins, pushes, win streaks, and score dictionary

num_wins = 0
num_push = 0

win_streak = 0
longest_streak = 0

score_dict = {4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0}


for i in range(num_games):
    cards = list(range(52))
    random.shuffle(cards)
    
    p = player(cards) 

    score_dict[p] += 1 
    
    d = dealer(cards) 

    if p > d or d > 21: 
        num_wins += 1
        win_streak += 1

        if win_streak > longest_streak: 
            longest_streak = win_streak

    elif p == d:
        num_push += 1 

    elif p < d:
        win_streak = 0 



win_prob = num_wins / num_games
push_prob = num_push / num_games

print(f"Probability player wins: {win_prob * 100:.4f}%")
print(f"Probability of push: {push_prob * 100:.4f}%")
print(f"Longest winning streak: {longest_streak} games")
print(score_dict)

# Extract data for plotting
scores = list(score_dict.keys())
frequencies = list(score_dict.values())

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(scores, frequencies, color='skyblue', edgecolor='black')
plt.title(f'Distribution of Player Scores (N={num_games:,})')
plt.xlabel('Final Score')
plt.ylabel('Frequency')
plt.xticks(scores)
plt.grid(axis='y', alpha=0.5)

# Save the plot instead of just showing it
plt.savefig('distribution_plot.png')
plt.show()
print("Plot saved as distribution_plot.png")