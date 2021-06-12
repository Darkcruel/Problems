# link : https://www.hackerrank.com/challenges/magic-square-forming/problem

def formingMagicSquare(s):
    # Write your code here
    result = 99999
    Magic_Square = [[[8,1,6],[3,5,7],[4,9,2]],
                    [[4,3,8],[9,5,1],[2,7,6]],
                    [[2,9,4],[7,5,3],[6,1,8]],
                    [[6,7,2],[1,5,9],[8,3,4]],
                    [[6,1,8],[7,5,3],[2,9,4]],
                    [[8,3,4],[1,5,9],[6,7,2]],
                    [[4,9,2],[3,5,7],[8,1,6]],
                    [[2,7,6],[9,5,1],[4,3,8]]] # set of 3*3 magic square
    for k in range(8):
        error_sum = 0
        for i in range(3):
            for j in range(3):
                    error_sum += abs(Magic_Square[k][i][j] - s[i][j])
        if(error_sum <= result):
            result = error_sum
            
    return result