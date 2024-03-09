def steps(number):
    n = number
    if n <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        counter = 0
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else: 
                n = n * 3 + 1
            counter = counter + 1
        return counter
    
            
            
        

        

    