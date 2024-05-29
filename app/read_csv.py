import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      #print(list(iterable)) Una lista de valore4s 
      #country_dict = {key: value for key, value in iterable}
      country_dict = dict(iterable)
      #print(country_dict)  dicccionario de valores
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[1])  #lista de diccionarios se puede ver por possiciones 