from pulp import *

# function to validate non-negative input
def get_non_negative_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Value must be non-negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

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

# dict with pack info
packs = {
    'P1': {'price': 5, 'vp': 475},
    'P2': {'price': 10, 'vp': 1000},
    'P3': {'price': 20, 'vp': 2050},
    'P4': {'price': 35, 'vp': 3650},
    'P5': {'price': 50, 'vp': 5350},
    'P6': {'price': 100, 'vp': 11000}
}

intro_text = "valorant currently provides the following packs:\n"
intro_text += "pack\teur\tvp\n"
for pack, details in packs.items():
    intro_text += f"{pack}\t{details['price']}\t{details['vp']}\n"

print(intro_text)

# Get current VP and item price with validation
current = get_non_negative_input("How many VP do you currently have? ")
item_price = get_non_negative_input("How many VP does the desired item cost? ")

# Calculate the required VP
required_vp = item_price - current

# current vp values for 
prob += 475 * x1 + 1000 * x2 + 2050 * x3 + 3650 * x4 + 5350 * x5 + 11000 * x6 >= required_vp

prob.solve()

print("ideal packs configuration to meet required vp:")
for v in prob.variables():
    print(f"{v.name}\t=\t{int(v.varValue)} unit(s)")

total_vp_from_packs = (
    475 * x1.varValue + 
    1000 * x2.varValue + 
    2050 * x3.varValue + 
    3650 * x4.varValue + 
    5350 * x5.varValue + 
    11000 * x6.varValue
)

# Calculate surplus
surplus = total_vp_from_packs - required_vp

print(f"\noptimal cost = {int(prob.objective.value())} eur")
print(f"total vp from purchased packs = {int(total_vp_from_packs)}")
print(f"surplus vp after purchase = {int(surplus)}")