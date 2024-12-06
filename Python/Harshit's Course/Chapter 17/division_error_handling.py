# Program to handle errors 
# In division function
 
def div(a,b):
    
    try:
        return a/b
    
    except ZeroDivisionError:              # If divide by zero
        return "Can't divide by zero"
    
    except TypeError:                      # If one of the input is
        return "Invalid input.."           # Other than int or float
    
    except:                                # For unknown errors           
        return "Unexpected error occured"

print(div('2',1))
