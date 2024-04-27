num_of_k = 6
def pattern1(num_of_k):
    for i in range(num_of_k, 0, -1):
        print("  "* (num_of_k-i),end = " ")
        for j in range(0, i - 1):
             print("k", end = " ")

        print("\n")
pattern1(num_of_k)