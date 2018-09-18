
''' How to get π:  
        π = 4( 1/1 + 1/3 + 1/5 + 1/7 + 1/9 + 1/11 ... )
'''
#There is a steady progression towards a point in which the value is 
def calculation_to_get_pi(numerator):
    previous_iteration = 0
    i = 1
    while i <= numerator:
        current_iteration = (1/i)
        pi_infinite_unpair_series = current_iteration + previous_iteration
        previous_iteration = current_iteration
        i += 2
    const = 4
    actual_pi = const * pi_infinite_unpair_series
    return  actual_pi
    
def string_items(int_to_convert):
    return str(int_to_convert)

def main():
    numerator = int(input('Please insert an unpair number: ' ))

    if numerator % 2 == 0:
        return "No señor No señor No señor no es asi"

    pi_finite_series = calculation_to_get_pi(numerator)
    print(pi_finite_series)
    # string_items(pi_finite_series)
    # print("Number of iteration on pi only with a finite series: " + pi_finite_series)

if __name__ == '__main__':
# ### ##### ####### ######### ########### ############# ############# ############### 
    main()
    #stop at a certain number of spaces


    #make it be a string

    #make number string and while number is not the lenght 