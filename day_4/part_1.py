def is_solved(board, draw, out = []):
    width = len(board) - 1
    height = len(board[0]) - 1
    for row in range(width + 1):
        for col in range(height + 1):
            if board[row][col] == draw:
                board[row][col] = None
                out.append((row, col))
        for pos in out:
            for row in range(width + 1):
                if board[row][pos[1]] != None:
                    break
                if row == width:
                    print(row, pos)
                    return 1
            
            for col in range(height + 1):
                if board[pos[0]][col] != None:
                    break
                if col == height:
                    return 1
            
                
def total(board, draw):
    total = 0
    for line in board:
        for num in line:
            if num == None:
                continue
            else:
                total += int(num)
    return total * int(draw)
        
        
        
def main():
    input_file = open("day_4/input.txt", "r")
    contents = input_file.read()
    input_file.close()
    boards = contents.split("\n\n")
    draws = boards[0].split(",")
    boards = boards[1:]
    for board in range(len(boards)):
        boards[board] = boards[board].split("\n")
        for line in range(len(boards[board])):
            boards[board][line] = boards[board][line].split()
            
    score = 0
    solved = False
    for draw in draws[:35]:
        for board in boards:
            valid = is_solved(board, draw)
            if valid:
                score = max(total(board, draw), score)
                solved = True
                print(board)
        if solved:
            return score, draw
                
                
    return "Need more draws"

print(main())
    
        
    




