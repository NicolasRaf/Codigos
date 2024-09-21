from math import comb

n = 10  
p = 0.2  
q = 1 - p  

k_values = [1,2,3,4,5,6,7,8,9,10]  
prob_sum = 0

for k in k_values:
    prob = comb(n, k) * (p ** k) * (q ** (n - k))
    print(k,"->",prob)
    prob_sum += prob

print(prob_sum)