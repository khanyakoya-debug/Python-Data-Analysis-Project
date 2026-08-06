import csv

file_name = "fifa_world_cup_2026_player_performance.csv"

print("\nWelcome to the FIFA Player Analysis System!")
print("Analyse FIFA World Cup 2026 player data using Python.\n")

def find_highest_value(column_index, title, value_name, data_type=int):

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        next(reader)

        highest_value = -1
        best_player = ""

        for row in reader:

            value = data_type(row[column_index])

            if value > highest_value:

                highest_value = value
                best_player = row[1]

        print("\n" + title)
        print("-" * 45)
        print("Player:", best_player)
        print(value_name + ":", highest_value)

def display_columns():
    with open(file_name, "r") as file:
        reader = csv.reader(file)

        headers = next(reader)

        print("\nDataset Columns")
        print("-" * 30)

        for number, header in enumerate(headers, start=1):
            print(f"{number}. {header}")
            
def dataset_information():

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        headers = next(reader)

        row_count = 0

        for row in reader:
            row_count += 1

        print("\nDATASET INFORMATION")
        print("-" * 30)
        print("Total Columns:", len(headers))
        print("Total Rows:", row_count)

def search_player():

    player_id = input("\nEnter player's id: ")

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        headers = next(reader)

        found = False

        for row in reader:

            if player_id.lower() in row[0].lower():

                print("\nPLAYER FOUND")
                print("-" * 30)

                for header, value in zip(headers, row):
                    print(f"{header}: {value}")

                found = True
                break

        if not found:
            print("\nPlayer not found.")

def total_players():

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        next(reader)

        player_count = 0

        for row in reader:
            player_count += 1

        print("\nTOTAL PLAYERS")
        print("-" * 25)
        print("Total Players:", player_count)

def average_age():

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        headers = next(reader)

        total_age = 0 #Starts counting the total age of all players.
        player_count = 0 #Counts how many players there are.

        for row in reader:

            total_age += float(row[2]) #Adds each player's age to the total. and row 2 its the age 

            player_count += 1

        average = total_age / player_count# we devide when we want an average of something by what we want with its total , this is the formula

        print("\nAVERAGE PLAYER AGE")
        print("-" * 25)
        print("Average Age:", round(average, 2), "years")


def top_goal_scorer():
    
    
   find_highest_value(
    22,
    "TOP GOAL SCORER",
    "Goals"
           )

   #with open(file_name, "r") as file:

       #reader = csv.reader(file)

        #next(reader)

        #highest_goals = -1 #This keeps track of the highest number of goals found so far.
        #best_player = ""

       # for row in reader:

            #goals = int(row[22]) # for every goal read this 

            #if goals > highest_goals: #If the player has scored more goals than the current highest

                #highest_goals = goals#best_player = row[1]

        #print("\nTOP GOAL SCORER")
        #print("-" * 25)
        #print("Player:", best_player)
        #print("Goals:", highest_goals)

def top_10_goal_scorers():

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        next(reader)

        players = [] # creates a list , This will store every player and their goals.

        for row in reader:

            player = row[1]
            goals = int(row[22])

            players.append([player, goals]) # adds each player 

        players.sort(key=lambda x: x[1], reverse=True) #This sorts by the Goals column from highest to lowest.

        print("\nTOP 10 GOAL SCORERS")
        print("-" * 35)

        for i, player in enumerate(players[:10], start=1): # keeps list a 10
            print(f"{i}. {player[0]} - {player[1]} Goals")

def team_goals():

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        next(reader)

        teams = {} # this is the dictionary

        for row in reader:

            team = row[4]
            goals = int(row[22])

            if team in teams: #If we've already seen this team before, add the new goals to its total.
                teams[team] += goals
            else:
                teams[team] = goals

        print("\nTEAM GOAL TOTALS")
        print("-" * 35)

        sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True) # lambda means "look at this column when sorting."

        for team, goals in sorted_teams:
            print(f"{team}: {goals} goals")

def most_valuable_player():

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        next(reader)

        highest_value = 0
        best_player = ""

        for row in reader:

            value = float(row[11])#Reads the player's market value.

            if value > highest_value: #Checks whether the current player is worth more than the most valuable player found so far.

                highest_value = value
                best_player = row[1] #Stores the player's name.

        print("\nMOST VALUABLE PLAYER")
        print("-" * 30)
        print("Player:", best_player)
        print("Market Value: €{:,.2f}".format(highest_value)) #Formats the number nicely.

def average_goals_by_position():

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        next(reader)

        positions = {}

        for row in reader:

            position = row[6]  
            goals = int(row[22])

            if position not in positions:
                positions[position] = [0, 0]

            positions[position][0] += goals
            positions[position][1] += 1

        print("\nAVERAGE GOALS BY POSITION")
        print("-" * 35)

        for position in positions:

            total_goals = positions[position][0]
            total_players = positions[position][1]

            average = total_goals / total_players

            print(f"{position}: {average:.2f} goals")

def top_assist_provider():
    find_highest_value(
    23,
    "TOP ASSIST PROVIDER",
    "Assists"
               )

    #with open(file_name, "r") as file:

       # reader = csv.reader(file)

        #next(reader)

        #highest_assists = -1
        #best_player = ""

       # for row in reader:

            #assists = int(row[23])

            #if assists > highest_assists:

                #highest_assists = assists
                #best_player = row[1]

       # print("\nTOP ASSIST PROVIDER")
        #print("-" * 30)
        #print("Player:", best_player)
        #print("Assists:", highest_assists)

def best_shooting_accuracy():

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        next(reader)

        highest_accuracy = 0
        best_player = ""

        for row in reader:

            shots = int(row[24])
            shots_on_target = int(row[25])

            if shots > 0:

                accuracy = (shots_on_target / shots) * 100 #create new metrics from existing data. instead of reading off the column

                if accuracy > highest_accuracy:

                    highest_accuracy = accuracy
                    best_player = row[1]

        print("\nBEST SHOOTING ACCURACY")
        print("-" * 35)
        print("Player:", best_player)
        print("Accuracy: {:.2f}%".format(highest_accuracy))

def highest_xg_player():
    find_highest_value(
    26,
    "PLAYER WITH HIGHEST EXPECTED GOALS (xG)",
    "Expected Goals (xG)",
    float
            )

    #with open(file_name, "r") as file:

        #reader = csv.reader(file)

        #next(reader)

        #highest_xg = -1
        #best_player = ""

        #for row in reader:

            #xg = float(row[26])

            #if xg > highest_xg:

                #highest_xg = xg
                #best_player = row[1]

        #print("\nPLAYER WITH HIGHEST EXPECTED GOALS (xG)")
        #print("-" * 45)
        #print("Player:", best_player)
        #print("Expected Goals (xG):", round(highest_xg, 2))

def display_menu():

    print("=" * 40)
    print("FIFA PLAYER ANALYSIS SYSTEM")
    print("=" * 40)

    print("1. View Dataset Information")
    print("2. Display Column Names")
    print("3. Total players")
    print("4. Average Age")
    print("5. Top Goal Scorer")
    print("6. Top 10 Goal Scorers")
    print("7. Search for a Player")
    print("8. Team Goal Total")
    print("9. Most Valuable Player")
    print("10. Average Goals by Position")
    print("11. Top Assist Provider")
    print("12. Best Shooting Accuracy")
    print("13. Player with Highest Expected Goals")
    print("14. Exit")
        
running = True

while running:
    display_menu()
    #"Keep repeating this code while running is True."

    choice = input("\nChoose an option: ") # what the user type what they chooose
    
    valid_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]

    if choice not in valid_choices:
        

        print("\nInvalid option!")
        print("Please choose a number from the menu.")

        input("\nPress Enter to continue...")
        continue
    print("\nYou selected option:", choice)

    if choice == "1":
       dataset_information()
       input("\nPress Enter to return to the menu...")
    #print("\nDisplaying dataset information...")

    elif choice == "2":
       display_columns()
       input("\nPress Enter to return to the menu...")

    elif choice =="3":
        total_players()
        input("\nPress Enter to return to the menu...")

    elif choice=="4":
        average_age()
        input("\nPress Enter to return to the menu...")

    elif choice=="5":
        top_goal_scorer()
        input("\nPress Enter to return to the menu...")
        
    elif choice=="6":
         top_10_goal_scorers()
         input("\nPress Enter to return to the menu...") 
        
     #with open(file_name, "r") as file:
    #reader = csv.reader(file)

    #headers = next(reader)

    #print("\nDataset Columns")
   # print("-" * 30)

    #for number, header in enumerate(headers, start=1):
        #print(f"{number}. {header}")
    
#elif choice== "3":
   # print("\nCounting Number of Rows... ")

#elif choice=="4":
   # print("\nCounting Number of Columns...")

    elif choice == "7":
        search_player()
        input("\nPress Enter to return to the menu...")
    #print("\nSearching for a player...")

    elif choice=="8":
        team_goals()
        input("\nPress Enter to return to the menu...")

    elif choice =="9":
        most_valuable_player()
        input("\nPress Enter to return to the menu...")

    elif choice=="10":
        average_goals_by_position()
        input("\nPress Enter to return to the menu...")

    elif choice=="11":
        top_assist_provider()
        input("\nPress Enter to return to the menu...")

    elif choice=="12":
        best_shooting_accuracy()
        input("\nPress Enter to return to the menu...")

    elif choice=="13":
        highest_xg_player()
        input("\nPress Enter to return to the menu...")
        
    elif choice == "14":
        print("\nThank you for using the FIFA Player Analysis System.")
        print("Goodbye!")
        running = False #Now the condition is no longer true, so the loop stops and the program ends.

    else:
       print("\nInvalid option. Please choose a number from the menu.") 
