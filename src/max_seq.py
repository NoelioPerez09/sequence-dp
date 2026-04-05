import sys, os
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        
    K = int(lines[0].strip())
    val = {}
    for i in range(1, K + 1):
        x, v = lines[i].strip().split()
        val[x] = int(v) 
    A = lines[K + 1]
    B = lines[K + 2]
    
    return K, val, A, B

def sequence_dp(k, val, A, B):
    n = len(A)
    m = len(B)
    M = [[None] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        M[i][0] = 0
    for j in range(m+1):
        M[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                M[i][j] = val[A[i-1]] + M[i-1][j-1]
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])
    solution = []
    i = n 
    j = m
    while(i != 0 and j != 0):
        if A[i-1] == B[j-1]:
            solution.append(A[i-1])
            i -= 1
            j -= 1
        elif M[i-1][j] == M[i][j]:
            i -= 1
        else:
            j -= 1
    return M[n][m], "".join(solution[::-1])

def main():
    if len(sys.argv) != 2:
        print("Invalid Number of Arguments!")
        sys.exit()
    try:
        k, val, A, B = read_file(sys.argv[1])
    except:
        print("Invalid File Structure!")
        sys.exit()
    if not A.isalpha() or not B.isalpha():
        print("Invalid Strings!")
        sys.exit()
    if not all(map(str.isalpha, val.keys())) or not all([len(i) == 1 for i in val.keys()]):
        print("Invalid Alphabet!")
        sys.exit()
    if not all(isinstance(v, int) and v > 0 for v in val.values()):
        print("Invalid Values!")
        sys.exit()
    if not (isinstance(k, int) and k > 0):
        print("K is not a Nonnegative Integer!")
    
    opt, subsequence = sequence_dp(k, val, A, B)
    out_name = f'../output/{sys.argv[1].split("/")[-1].split(".")[0]}.out'
    with open(out_name, "w") as file:
        file.write(f'{opt}\n')
        file.write(subsequence)
    print(opt)
    print(subsequence)

if __name__ == "__main__":
    main()
