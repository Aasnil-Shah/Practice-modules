'''Write a program to print below:
        *
       * *
      * * *
     * * * *
    * * * * *
    * * * * *
     * * * *
      * * *
       * *
        *                        '''

n = 5
for i in range(n+1):
    print(" "*(n-i), end = "")
    print("* "*i, end = "")
    print()
for j in range(n+1):
    print(" "*j, end = "")
    print("* "*(n-j), end = "")
    print()