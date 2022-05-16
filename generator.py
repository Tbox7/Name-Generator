

print('Welcome to the Name Generator')

def func(): 
#input for names
    n1 = input('Name of City: ')
    n2 = input('Name of pet: ')
    nf = (n1 + " " + n2)
#result
    print('Generated name: ' + nf)
    again = input('Try again? Y or N')
#Repeat program if selected Y
    if again == 'Y':
        func()
    else:
        print('Congrats on your new name!')
#intial call
func()

