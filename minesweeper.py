#Create minesweeper type game
#Iterate through given list, check all sides of character if not #
#Print number of hashes adjacent to character
#Reprint grid

#Preset mine locations
game = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

def count_adjacent_mines(x, y):
    #Main function to count mines around current position
    count = 0
    
    #Review all coordinates around current x,y coordinates
    #Checks if position is valid before adding to count
    if x > 0 and y > 0 and game[x-1][y-1] == "#":
        #Add one to count of mines around current position
        count += 1
    if x > 0 and game[x -1][y] == "#":
        count += 1
    if x > 0 and y < len(game[0]) - 1 and game[x-1][y+1] == "#":
        count += 1
    if y > 0 and game[x][y-1] == "#":
        count += 1
    if y < len(game[0]) - 1 and game[x][y+1] == "#":
        count += 1
    if x < len(game) - 1 and y > 0 and game[x+1][y-1] == "#":
        count += 1
    if x < len(game) - 1 and game[x+1][y] == "#":
        count += 1 
    if x < len(game) - 1 and y < len(game[0]) - 1 and game[x+1][y+1] == "#":
        count += 1        
    return count

#Loop to itterate through 2D list and review each coordinate

for row_index, value in enumerate(game, start = 0):
    for col_index, temp in enumerate(value, start = 0):
        #Checks if current position is not a mine, if not change to count of mines adjacent
        if game[row_index][col_index] == "-":
            game[row_index][col_index] = (count_adjacent_mines(row_index, col_index))

#Print game in grid format for readability            
for row in game:
    print(" ".join(map(str, row)))
        