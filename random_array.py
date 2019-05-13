# Code source: project.pdf

from random import randint

def random_array(n):
    # create an array variable
    array = []
    # incremented from zero
    for i in range(0, n, 1):
        # adding random integers between 0 and 100
        array.append(randint(0,100))
    return array


# assign the random array to alist variable
alist = random_array(100)
alist1 = random_array(250)
alist2 = random_array(500)
alist3 = random_array(750)
alist4 = random_array(1000)
alist5 = random_array(1250)
alist6 = random_array(2500)
alist7 = random_array(3570)
alist8 = random_array(5000)
alist9 = random_array(6250)
alist10 = random_array(7500)
alist11 = random_array(8750)
alist12 = random_array(10000)
alist13 = random_array(50000)
