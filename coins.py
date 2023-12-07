# Generate Coin Change
# Implement generateCoinChange(cents)​ that accepts a parameter for the number of cents, and
# computes how to represent that amount with the smallest number of coins. 

def generate_coin_change(cents):
    output = {}
    output['quarters'] = cents // 25
    cents -= output['quarters'] *25
    output['dimes'] = cents // 10
    cents -= output['dimes'] *10
    output['nickels'] = cents // 5
    cents -= output['nickels'] *5
    output['pennies'] = cents
    return f"""
    Quarters: {output['quarters']}
    Dimes: {output['dimes']}
    Nickels: {output['nickels']}
    Pennies: {output['pennies']}"""

print(generate_coin_change(122))
#Returns:
#     Quarters: 4
#     Dimes: 2
#     Nickels: 0
#     Pennies: 2