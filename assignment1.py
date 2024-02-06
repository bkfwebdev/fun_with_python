# Install necessary dependencies
import random
import matplotlib.pyplot as plot
def menu():
    """Display a menu with four options, return the user’s selection as an integer"""
    user_input = None
    while(user_input != 4):
        
        user_input_string = input('Choose from the following options:\n1.Test the python random.randrange()\n2.Test the dilbert() function\n3.Test the randu() function\n4.Quit this program\n')
        user_input = int(user_input_string)
        if(user_input >= 1 and user_input <=4):
            return user_input
        else:
            print('That is not a valid option. Please try again.')
def test_random_randrange(num_to_test):
    # YOUR CODE HERE
    my_list = [0] * 10
    for nums in range(10):
        my_list[nums] = 0
    for nums in range(num_to_test):
        my_num = random.randrange(0,10)
        my_list[my_num] = my_list[my_num] + 1
    print('Digit Number of times generated')
    for nums in range(10):
        print(" ",nums,"          ",my_list[nums])
    #display the results as a graph
    figure = plot.figure()
    axes = figure.add_axes([0,0,1,1])
    labels = ['0','1','2','3','4','5','6','7','8','9']
    values = my_list
    axes.bar(labels,values)
    axes.set_title('Counts: random.randrange()')
    plot.show()
def dilbert():
    return 9
def test_dilbert(num_to_test):
    my_list = [0] * 10
    for nums in range(10):
        my_list[nums] = 0
    for nums in range(num_to_test):
        my_num = dilbert()
        my_list[my_num] = my_list[my_num] + 1
    print('Digit Number of times generated')
    for nums in range(10):
        print(" ",nums,"          ",my_list[nums])
    #display the results as a graph
    figure = plot.figure()
    axes = figure.add_axes([0,0,1,1])
    labels = ['0','1','2','3','4','5','6','7','8','9']
    values = my_list
    axes.bar(labels,values)
    axes.set_title('Counts: random.randrange()')
    plot.show()
def randu(last_number):
    new_num = 65539 * last_number % pow(2, 31)
    return new_num
def test_randu(num_to_test):
    my_list = [0] * 10
    last_num = 1
    for nums in range(10):
        my_list[nums] = 0
    for nums in range(num_to_test):
        my_num = randu(last_num)
        my_list[last_num % 10] = my_list[last_num % 10] + 1
        last_num = my_num
    print('Digit Number of times generated')
    for nums in range(10):
        print(" ",nums,"          ",my_list[nums])
    #display the results as a graph
    figure = plot.figure()
    axes = figure.add_axes([0,0,1,1])
    labels = ['0','1','2','3','4','5','6','7','8','9']
    values = my_list
    axes.bar(labels,values)
    axes.set_title('Counts: random.randrange()')
    plot.show()
def main():
    # YOUR CODE HERE
    user_choice = 0
    while user_choice != 4:
        user_choice = menu()
        if user_choice != 4:
            repetitions = input("please input number of repetitions")
            repetitions = int(repetitions)
        if user_choice == 1:
            test_random_randrange(repetitions)
        if user_choice == 2:
            test_dilbert(repetitions)
        if user_choice == 3:
            test_randu(repetitions)
        if user_choice == 4:
            print("program exit")
            break
main()