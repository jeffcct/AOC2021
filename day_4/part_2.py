class Board:
    def __init__(self, values):
        self.values = values
        self.unused = ([], [])
        self.complete = False
        self.width = len(values)
        self.height = len(values[0]) 
        for row in range(self.height):
            self.unused[0].append([i for i in range(self.width)])
        for col in range(self.width):
            self.unused[1].append([i for i in range(self.height)])
            
            
    def update(self, draw):
        for x in range(self.width):
            for y in self.unused[0][x]:
                if self.values[x][y] == draw:
                    if not (y in self.unused[0][x] and x in self.unused[1][y] and draw == self.values[x][y]):
                        print(y, self.unused[0][x], x, self.unused[1][y], draw, self.values[x][y])
                    self.unused[0][x].remove(y)
                    self.unused[1][y].remove(x)
    
    def is_complete(self):
        if [] in self.unused[0] or [] in self.unused[1]:
            return True
        
        
    def total(self):
        total = 0
        for x in range(self.width):
            for y in self.unused[0][x]:
                total += int(self.values[x][y])
        return total
    
    
    
                
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
        boards[board] = Board(boards[board])
    
    output = None
    boards = boards
    for draw in draws:
        for board in boards[::-1]:
            board.update(draw)
            complete = board.is_complete()
            if complete:
                if len(boards) == 1:
                    return draw, board.total() * int(draw)
                output = board
                boards.remove(board)
    return output
print(main())
        
        