from pulp import *

# problem initialisation
prob = LpProblem("valorant_vp_cost_minimization", LpMinimize)

# decision variables
x1 = LpVariable('p1: 5 eur/475 vp', lowBound=0, cat='Integer')
x2 = LpVariable('p2: 10 eur/1000 vp', lowBound=0, cat='Integer')
x3 = LpVariable('p3: 20 eur/2050 vp', lowBound=0, cat='Integer')
x4 = LpVariable('p4: 35 eur/3650 vp', lowBound=0, cat='Integer')
x5 = LpVariable('p5: 50 eur/5350 vp', lowBound=0, cat='Integer')
x6 = LpVariable('p6: 100 eur/11000 vp', lowBound=0, cat='Integer')

# objective function
prob += 5 * x1 + 10 * x2 + 20 * x3 + 35 * x4 + 50 * x5 + 100 * x6

current = int(input("how many vp do you currently have? "))
item_price = int(input("how many vp does the desired item cost? "))

# current vp values for 
prob += 475 * x1 + 1000 * x2 + 2050 * x3 + 3650 * x4 + 5350 * x5 + 11000 * x6 >= (item_price - current)

prob.solve()

print("ideal packs configuration to meet required vp:")
for v in prob.variables():
    print(f"{v.name}\t=\t{v.varValue}")

print(f"optimal cost = {prob.objective.value()} eur")