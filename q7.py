import array

def  display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    numString = input()
    numFloat= numString.split(", ")

    numFloat=(float, numFloat)
    print(numFloat)
    return numFloat


def calc_average(temps):
    sum=0
    for temp in temps:
        sum= sum + temp

    avg=sum/len(temps)
    print (avg)
    return avg

def calc_min_max_temperature(temps):
    max=temps[0]
    min=temps[0]

    for i in temps:
        if (temps[i]>max):
            max=temps[i]
        if (temps[i]<min):
            min= temps[i]

    minMax=[min,max]
    return minMax
#
# def sort_temperature():
#
# def calc_median_temperature():

def main():
    display_main_menu()
    temps=get_user_input()
    calc_average(temps)
    calc_min_max_temperature(temps)

main()