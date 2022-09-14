"""You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given.
 If you reach the end point before all your moves have gone, you should return Finish.
 If you hit any walls or go outside the maze border, you should return Dead.
 If you find yourself still in the maze after using all the moves, you should return Lost."""


maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

directions = ["N", "N", "N", "N", "N", "E", "E", "S", "S", "S", "S", "S", "S"]

def maze_runner(maze, directions):
    boarder = len(maze)-1
    for row in range(len(maze)):
        for cell in range(len(maze[row])):
            if maze[row][cell] == 2:
                start_row = row
                start_column = cell
                for move in directions:
                    if move == "N" and start_row-1 >= 0:
                        if maze[start_row-1][start_column] in (0, 2):
                            start_row -= 1
                        elif maze[start_row-1][start_column] == 3:
                            return "Finish"
                        else:
                            return "Dead"
                    elif move == "S" and start_row+1 <= boarder:
                        if maze[start_row+1][start_column] in (0, 2):
                            start_row += 1
                        elif maze[start_row+1][start_column] == 3:
                            return "Finish"
                        else:
                            return "Dead"
                    elif move == "E" and start_column+1 <= boarder:
                        if maze[start_row][start_column+1] in (0, 2):
                            start_column += 1
                        elif maze[start_row][start_column+1] == 3:
                            return "Finish"
                        else:
                            return "Dead"
                    elif move == "W" and start_column-1 >= 0:
                        if maze[start_row][start_column-1] in (0, 2):
                            start_column -= 1
                        elif maze[start_row][start_column-1] == 3:
                            return "Finish"
                        else:
                            return "Dead"
                    else:
                        return "Dead"
                return "Lost"

print(maze_runner(maze, directions))