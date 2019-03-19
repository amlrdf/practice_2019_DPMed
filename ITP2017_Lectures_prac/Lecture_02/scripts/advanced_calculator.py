import operator

ops = {
    '+': operator.add,
    '-': operator.sub
}

number_1 = input('Enter the first digit\t: ')
operator = input('Enter the operator\t: ')
number_2 = input('Enter the second digit\t: ')

if number_1.isnumeric():
    number_1 = int(number_1)
else:
    print("Number 1 was not a number")

if number_2.isnumeric():
    number_2 = int(number_2)
else:
    print("Number 2 was not a number")

print(ops['+'](number_1, number_2))