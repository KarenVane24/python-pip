import charts
import read_csv
import utils


def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  #countries = list(map(lambda x: x['Country'], data))
  countries = [x['Country/Territory'] for x in data]
  #percentages = list(map(lambda x: x['World Population Percentage'], data))
  percentages = [x['World Population Percentage'] for x in data]
  charts.generate_pie_chart(countries, percentages)
  
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country/Territory"], labels, values)
  
if __name__ == '__main__':
  run()

'''import utils

data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]
def run():
  keys, values=utils.get_population()
  print(keys,values)
  
  print(utils.a)
  
  
  country = input('Type Country => ')
  
  result = utils.population_by_country(data, country)
  print(result)
 '''
