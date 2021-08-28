string=input("Enter the string")
split_string = string.split(' ')
print(f"Split string is(List of string) -> {split_string}")

join_string='--'.join(split_string)
print(f"After spliting, new joined string is(List of string) -> {join_string}")

'''
Output
Enter the string-> monk who sold his ferrari
Split string is(List of string) -> ['monk', 'who', 'sold', 'his', 'ferrari']
after spliting, new joined string is(List of string) -> monk--who--sold--his--ferrari
'''
