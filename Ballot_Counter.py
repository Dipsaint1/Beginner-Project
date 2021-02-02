"""
    BALLOT COUNTING PROJECT
            BY
    AYODEJI OLADAPO ADEWALE

    UNIVERSITY OF IBADAN
"""
import time

registered_voters = 1000
profile = {}
count_vote_dict = {"APC": 0, "PDP": 0, "ZLP": 0, "ACCORD": 0, "YDP": 0}     # Initial votes

party_dict = {
                "APC": "ADELABU PENKELEMES",
                "PDP": "SEYI MAKINDE",
                "ZLP": "ADEBAYO ALAO AKALA",
                "ACCORD": "OLUFEMI LANLEHIN",
                "YDP": "ABAYOMI FAGBENRO"
             }
def help():
    for keys, values in party_dict.items():
        print(f"Enter '{keys}' to vote for '{values}'")

def vote(count_vote):
    count = 0
    while count < registered_voters + 1:
        print("-------------------------------------------------------")
        choice = input("PRESS 'ENTER' KEY TO CAST YOUR VOTE or 'Q' TO QUIT\n").upper()
        if choice == "":
            while True:     # Ensure user enters a digit
                age = input("AGE: ")
                if age.isdigit():
                    if int(age) < 18:   # People aged 18 and above are eligible to vote
                        print("\nYOU ARE NOT ELIGIBLE TO VOTE")
                        break
                    else:
                        while True:
                            name = input("\nNAME: ").title()
                            if name.isalpha():
                                break
                            else:
                                print("NAME SHOULD CONTAIN ONLY ALPHABETS")
                        print()  # New line
                        help()  # Display list of parties with their respective aspirants

                        while True:
                            cast_vote = input("\nCHOOSE PARTY: ").upper()
                            if cast_vote.isalpha():
                                if cast_vote in party_dict.keys():
                                    print(". ..", end=" ")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("YOUR VOTE HAS BEEN REGISTERED")
                                    break
                                else:
                                    print(f"{cast_vote} IS AN INVALID INPUT\n")
                                    help()
                            else:
                                print("INVALID INPUT\n")
                                help()

                        if cast_vote == "APC":
                            count_vote[cast_vote] += 1
                        elif cast_vote == "PDP":
                            count_vote[cast_vote] += 1
                        elif cast_vote == "ZLP":
                            count_vote[cast_vote] += 1
                        elif cast_vote == "ACCORD":
                            count_vote[cast_vote] += 1
                        elif cast_vote == "YDP":
                            count_vote[cast_vote] += 1

                        profile[name] = age
                        count += 1
                        break

                else:
                    print("WRONG INPUT! ENTER A DIGIT BETWEEN 0...9")

        elif choice == "Q" or choice == 'q':
            print("VOTING CLOSED!")
            print("--------------------------------------------------------")
            """Deadline can be set to stop people from voting"""
            break

        else:
            print("INVALID INPUT! PRESS 'ENTER' KEY TO CAST YOUR VOTE OR 'Q' TO QUIT")

    return count_vote

def declare_winner():
    counted_votes = vote(count_vote_dict)
    # Sort the votes in descending order i.e from the highest value

    party_with_highest_votes = []
    for party, votes in sorted(counted_votes.items()):
        if votes < 2:
            print(f"{party} has {votes} vote")
        else:
            print(f"{party} has {votes} votes")
        max_votes = max(counted_votes.items(), key=lambda x: x[1])
        if votes == max_votes[1]:
            party_with_highest_votes.append(party)

    if len(party_with_highest_votes) > 1:
        print(f"\nPARTIES WITH HIGHEST VOTES: {party_with_highest_votes}")
        print("POLLS WILL BE OPENED IN 24 HOURS TO GET THE WINNER")

    else:   # If 2 or more parties have the same maximum votes
        for key, value in counted_votes.items():
            if key in party_with_highest_votes:
                highest_vote = key
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("...")
                print(f"\n{party_dict[key]} of {highest_vote} PARTY WINS THE ELECTION")
    # Now declare the winner

declare_winner()






