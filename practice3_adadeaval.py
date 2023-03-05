for n in range(2, 1000):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')






    # for char in AlphabetString:
    #     if char in 'cqmnr':
    #         break
    #     if char in 'CFGJK':
    #         continue
    #     print(char)
    # else:
    #     print('اگر حلقه شکسته نشه من چاپ میشم')
