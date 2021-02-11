from random import choice

sample = [*range(1,7)]
n = int(input("Perform event no. of times :- "))
outcome = []

def probability(sample, outcome, n):
    for s in sample:
        p = outcome.count(s)/n
        print(f"{s} : {p}")


for _ in range(n):
    outcome.append(choice(sample))
    
print("Probability of each")
probability(sample, outcome, n)
print(outcome)

"""
Perform event no. of times :- 5
Probability of each
1 : 0.0
2 : 0.2
3 : 0.2
4 : 0.4
5 : 0.2
6 : 0.0
[3, 4, 2, 4, 5]

"""


