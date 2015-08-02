## Example of computation without and with functional abstraction

## Without functional abstraction

##x = raw_input('Enter a number: ')
##p = int(raw_input('Enter an integer power: '))
##
##result = 1
##
##for turn in range(p):
##    print('iteration: ' + str(turn) + ' current result: ' + str(result))
##    result = result * x


## With functional abstraction

def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result


x=23432
p=234234
result=5
print(iterativePower(3,5))
#x=int(raw_input('Ingrese x: '))
#p=int(raw_input('Ingrese p: '))
#        
#y=iterativePower(x,p)
#print y