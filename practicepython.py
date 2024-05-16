file_name = "file_name = "input_3_cap1.txt" rounds = []
try:
with open(file_name, 'r') as file:
for line in file:
round_data = line.strip().split() rounds.append((round_data[0], round_data[1]))
except FileNotFoundError:
print(f"Error: File '{file_name}' not found.") exit()
# Function to calculate the score for a round
def calculate_score(player_choice, opponent_choice, outcome): choices = {'A': 1, 'B': 2, 'C': 3}
outcomes = {'X': 0, 'Y': 3, 'Z': 6}
player_score = choices[player_choice] opponent_score = choices[opponent_choice] outcome_score = outcomes[outcome]
if player_score == opponent_score:
        return player_score
    elif (player_score == 1
opponent_score):
        return player_score
    else:
        return player_score
# Calculate the total score
total_score = 0
for round_data in rounds:
+ outcome_score # Draw
and opponent_score == 3) or (player_score >
+ outcome_score  # Win
+ outcome_score  # Lose
player_choice, outcome = round_data
opponent_choice = 'C' if player_choice == 'A' else ('A' if player_choice == 'B' else 'B')
total_score += calculate_score(player_choice, opponent_choice, outcome) # Print the total score
print("Total Score:", total_score)" 
rounds = []

try:
    with open(file_name, 'r') as file:
        for line in file:
            round_data = line.strip().split() 
            rounds.append((round_data[0], round_data[1]))
        
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.") 
    exit()
# Function to calculate the score for a round
def calculate_score(player_choice, opponent_choice, outcome): 
    choices = {'A': 1, 'B': 2, 'C': 3}
    outcomes = {'X': 0, 'Y': 3, 'Z': 6}
    
    player_score = choices[player_choice] 
    opponent_score = choices[opponent_choice] 
    outcome_score = outcomes[outcome]

    if player_score == opponent_score:
        return player_score + outcome_score #Draw
    elif (player_score == 1 and opponent_score == 3) or (player_score > opponent_score):
        return player_score + outcome_score #win
    else:
        return player_score

# Calculate the total score
total_score = 0
for round_data in rounds:
    player_choice, outcome = round_data
    opponent_choice = 'C' if player_choice == 'A' else ('A' if player_choice == 'B' else 'B')
    total_score += calculate_score(player_choice, opponent_choice, outcome) # Print the total score
#Print total score
print("Total Score:", total_score)