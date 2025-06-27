from mrjob.job import MRJob

class MinTemp(MRJob):

    def MakeFahrenheit(self, tenthsOfCelsius):
        celsius = float(tenthsOfCelsius) / 10.0
        fahrenheit = celsius * 1.8 + 32.0
        return fahrenheit

    def mapper(self, _, line):
        (location, date, datatype, data, x, y) = line.split(',')
        if (datatype == 'TMIN'):
            temperature = self.MakeFahrenheit(data)
            yield location, temperature

    def reducer(self, location, temps):
        yield location, min(temps)

if __name__ == '__main__':
    MinTemp.run()

# !python MinTemperature.py 1800weather.csv