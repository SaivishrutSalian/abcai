# Initial counts of unreached Missionaries and Cannibals
um = 3  # unreached Missionaries
uc = 3  # unreached Cannibals
rm = 0  # reached Missionaries
rc = 0  # reached Cannibals
flag = 0  # for checking where the boat is present (on start or at end)

# For displaying the current state of the problem
def display():
    print(f"Left: {'M ' * um} {'C ' * uc} | Boat: {'M ' * rm} {'C ' * rc} | Right: {'M ' * (3 - rm)} {'C ' * (3 - rc)}")

# For checking if all Missionaries and Cannibals have reached the other side
def is_reached():
    return rm == 3 and rc == 3

# The main algorithm working
def solve():
    global um, uc, rm, rc, flag
    
    while not is_reached():
        if flag == 0:  # Boat is on the starting side
            if um >= 2:  # Move 2 Missionaries
                rm += 2
                um -= 2
                print("Moving 2 Missionaries.")
            elif uc >= 2:  # Move 2 Cannibals
                rc += 2
                uc -= 2
                print("Moving 2 Cannibals.")
            elif um >= 1 and uc >= 1:  # Move 1 Missionary and 1 Cannibal
                rm += 1
                uc -= 1
                um -= 1
                print("Moving 1 Missionary and 1 Cannibal.")
            elif um >= 1:  # Move 1 Missionary
                rm += 1
                um -= 1
                print("Moving 1 Missionary.")
            elif uc >= 1:  # Move 1 Cannibal
                rc += 1
                uc -= 1
                print("Moving 1 Cannibal.")
            flag = 1  # Boat is now on the other side
        else:  # Boat is on the other side
            if rm >= 2:  # Return with 2 Missionaries
                rm -= 2
                um += 2
                print("Returning with 2 Missionaries.")
            elif rc >= 2:  # Return with 2 Cannibals
                rc -= 2
                uc += 2
                print("Returning with 2 Cannibals.")
            elif rm >= 1 and rc >= 1:  # Return with 1 Missionary and 1 Cannibal
                rm -= 1
                rc -= 1
                um += 1
                uc += 1
                print("Returning with 1 Missionary and 1 Cannibal.")
            elif rm >= 1:  # Return with 1 Missionary
                rm -= 1
                um += 1
                print("Returning with 1 Missionary.")
            elif rc >= 1:  # Return with 1 Cannibal
                rc -= 1
                uc += 1
                print("Returning with 1 Cannibal.")
            flag = 0  # Boat is now on the starting side
        
        display()  # Display the current state

def main():
    print("Missionaries And Cannibals Problem")
    display()
    solve()
    display()  # Final state

main()
