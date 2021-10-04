revenue = int(input('Input your revenue: '))
expenses = int(input('Input your expenses: '))

if revenue > expenses:
    profit = revenue - expenses
    print('Congratulations, your profit is:', profit)

    margin = 100 * revenue / expenses
    print('Your profit margin is:', '{0:5.2f}%'.format(margin))

    people=int(input('Please input your head count: '))
    print('Your profit per person is:', '{0:5.3f}'.format(profit/people))
else:
    losses = - revenue + expenses
    print('Unfortunately, your losses are:', losses)
