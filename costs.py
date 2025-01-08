# Description: This file contains the cost functions for the different scenarios

# Movement cost function for the first scenario
def C_1(t):
    horizontal = 10
    vertical = 10
    return (horizontal, vertical)

# Movement cost function for the second scenario
def C_2(t):
    horizontal = 15
    vertical = 10
    return (horizontal, vertical)

# Movement cost function for the third scenario
def C_3(t):
    horizontal = 10 + (abs(5 - t) % 6)
    vertical = 10
    return (horizontal, vertical)

# Movement cost function for the fourth scenario
def C_4(t):
    horizontal = 5 + (abs(10 - t) % 11)
    vertical = 10
    return (horizontal, vertical)