def highest_even(li):
    max_even= 0
    for i in li:
        if i %2 ==0:
            if(i>max_even):
                max_even=i
    return max_even

print(highest_even([10,2,3,4,8,11]))