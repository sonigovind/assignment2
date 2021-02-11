from itertools import product

n = 5
choice = "T"
sample = set(product(['H', 'T'], repeat=n))
print("Samples :", sample)
'''
{('T', 'H', 'H', 'H', 'H'), ('T', 'T', 'H', 'H', 'H'), ('T', 'H', 'T', 'H', 'H'), ('H', 'T', 'T', 'H', 'H'), ('T', 'T', 'T', 'H', 'H'), ('H', 'H', 'H', 'H', 'H'), ('T', 'H', 'H', 'H', 'T'), ('T', 'T', 'H', 'H', 'T'), ('H', 'T', 'H', 'T', 'H'), ('H', 'H', 'T', 'T', 'H'), ('H', 'T', 'T', 'H', 'T'), ('T', 'H', 'T', 'H', 'T'), ('T', 'T', 'T', 'H', 'T'), ('H', 'H', 'H', 'H', 'T'), ('H', 'T', 'H', 'T', 'T'), ('T', 'T', 'H', 'T', 'H'), ('H', 'H', 'T', 'T', 'T'), ('T', 'T', 'T', 'T', 'H'), ('T', 'H', 'T', 'T', 'H'), ('T', 'T', 'H', 'T', 'T'), ('H', 'T', 'T', 'T', 'H'), ('T', 'H', 'H', 'T', 'H'), ('H', 'H', 'H', 'T', 'H'), ('T', 'T', 'T', 'T', 'T'), ('H', 'T', 'H', 'H', 'H'), ('H', 'H', 'T', 'H', 'H'), ('H', 'T', 'T', 'T', 'T'), ('T', 'H', 'T', 'T', 'T'), ('T', 'H', 'H', 'T', 'T'), ('H', 'T', 'H', 'H', 'T'), ('H', 'H', 'H', 'T', 'T'), ('H', 'H', 'T', 'H', 'T')}
'''
count = [0]*(n+1)
for s in sample:
    count[s.count(choice)] += 1 

print(f"Probability having : {choice}")
for i in range(len(count)):
    print(f"{i} time :- {count[i]/len(sample)}")

'''
Probability having T
0 time :- 0.03125
1 time :- 0.15625
2 time :- 0.3125
3 time :- 0.3125
4 time :- 0.15625
5 time :- 0.03125

'''




