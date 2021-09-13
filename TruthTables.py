
import ttg

#Prints a table for the truth values of p and q
table = ttg.Truths(['p', 'q'] , ['p and q', 'p or q', 'p xor q', 'p = q'], ints=False)

print(table.as_prettytable())


