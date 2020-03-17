def readFile(matrix, file):
    file = open(file, 'r')
    n = int(file.readline())
    for _ in range(n):
        line = file.readline()
        lineValues = line.split(',')
        lineList = []
        for value in lineValues:
            lineList.append(int(value))
        matrix.append(lineList)
    return n

def min_distance(n, dist, visited):
    min = 10000000
    min_index = -1
    for index in range(n):
        if dist[index] < min and index + 1 not in visited and dist[index] != 0:
            min = dist[index]
            min_index = index + 1
    return min, min_index

def solve(matrice, n, src, dest):
    vizitat = [src] if src else [1]
    sum = 0
    for i in range(n - 1):
        if len(vizitat) != n:
            min, min_index = min_distance(n, matrice[vizitat[-1] - 1], vizitat)
            sum += min
            vizitat.append(min_index)
            if (dest and min_index == dest):
                break
    sum += matrice[vizitat[-1] - 1][vizitat[0] - 1]
    print(n)
    print(vizitat)
    print(sum)


def main():
    # file = 'easy_03_tsp.txt'
    # file = 'medium_01_tsp.txt'
    file = 'hard_01_tsp.txt'
    matrice = []
    solve(matrice, readFile(matrice, file), None, None)

main()
