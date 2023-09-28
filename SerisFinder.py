import plotly.express as px

def evenDivison(x):
    if x == 2:
        return x
    elif x % 2 == 0:
        x = x/2
        return int(evenDivison(x))
    else:
        return x
i = 1
data = []
for _ in range(10000):
    number = evenDivison(i)
    data.append(number)
    print(number)
    i += 1

x = [x for x in range(len(data))]
fig = px.scatter(x=x, y=data)
fig.show()
