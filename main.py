import plotly.express as px

ind = px.data.gapminder().query("country == 'india'")

px.bar(ind, x='country', y='pop')
px.show()

