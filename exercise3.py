i = 0                   # -> 1
n = input("n: ")        # -> 1

while i < n:            # -> N/100
    while a < n:        # -> N^2/100
        while b < n:    # -> N^3/100
            b = b + 1   # -> N^3/100
        a = a + 1       # -> N^2/100
    
    while (c < n):      # -> N^2/100
        c = c + 1       # -> N^2/100
    i = i + 100         # -> N/100

# F(N) = 1 + 1 + N/100 + N^2/100 + N^3/100 + N^3/100 + N^2/100 + N^2/100 + N^2/100 + N/100 = 2N^3/100 + 4N^2/100 + 2N/100 + 2
# O(N^3)