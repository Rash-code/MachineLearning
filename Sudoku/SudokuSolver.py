

board1= [[7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]]

board= [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def print_board(b):
    for i in range(len(b)):
        if i % 3 ==  0 :
            print('-------|--------|----------')
        for j in range(len(b)):
            if j % 3 == 0 and j != 0:
                print(' | ', end="")
            if j==8:
                print(str(b[i][j]) + " ")
            else:
                print(str(b[i][j])+ " ", end="")
    print('-------|--------|----------')

def find_emplty(b):
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i][j] == 0:
                return (i,j)
    return None


def valid_entry(b,num,pos):
    # check each row
    for i in range(len(b)):
        if b[pos[0]][i] == num and i != pos[1]:
            return False
    # check each column
    for i in range(len(b)):
        if b[i][pos[1]] == num and i != pos[0]:
            return False
    #check each box
    x = pos[1] // 3
    y = pos[0] // 3
    for i in range(y*3 , y*3+3):
        for j in range(x*3,x*3+3):
            if b[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(b):
    find=find_emplty(b)
    if not find:
        return True
    else:
        row, col= find
    for i in range(1,10):
        if valid_entry(b,i,find):
            b[row][col]= i

            if solve(b):
                return True
            b[row][col]=0
    return False

print_board(board)
solve(board)
print_board(board)