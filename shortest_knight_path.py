# my discovered solution
def knight(p1, p2):
    # verify input
    # length 2
    # first element is char
    # second is digit

    # convert to 1-base numerical coordinates
    p1 = (ord(str(p1[0]))-96, int(str(p1[0])))
    p2 = (ord(str(p2[0]))-96, int(str(p2[0])))

    # verify that each coordinate is 0-8

    # find all possible spaces one move away from p1
    # check all possible spaces if it is p2
    moves = [(p1, 0)]
    for move in moves:
        coordinates = move(0)
        turns = move(1)
        if coordinates == p2: return turns
        for possible in findMoves(coordinates):
            moves.append((possible, turns+1))
        

def findMoves(coordinates):
    # return array of possible moves
    pass

knight('a1', 'b1')
knight('h1', 'z10')