# this file interacts with the user/screen/terminal to communicate how exactly to make the ship balanced

# solution_info is a tuple with the first element being the amount of minutes it takes to balance the ship
# and the second element being the number of moves need to balance the ship
def UserInteraction(filename, action_tuples, total_time, num_moves):
    # first we need to output to the screen that a solution was found, how long it'll 
    # take to balance the ship in minutes, and how many moves are needed to complete 
    # this action

    print(f"A solution was found, it will take {int(total_time)} minutes and {int(num_moves)} moves.")

    # now iterate through all the moves with a feature that requires the user to hit enter after they have
    # finished a move and move on to the next one

    return "Done"