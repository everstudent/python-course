import json

profits = {}
losses = {}
total_profits = 0
total_losses = 0

with open('data7.txt') as f:
    for l in f:
        title, form, income, costs = l.split()
        income = int(income)
        costs = int(costs)
        profit = income - costs

        if income >= costs:
            profits[title] = profit
            total_profits += profit
        else:
            losses[title] = profit
            total_losses += profit


result = [
    profits,
    losses,
    {
        'avg_profits': total_profits / len(profits),
        'avg_losses': total_losses / len(losses)
    }
]

with open('data7_res.txt', 'w') as r_f:
    json.dump(result, r_f)

print(result)
