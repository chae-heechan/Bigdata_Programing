
def main():
    year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    population = [10249679, 10193518, 10143645,
                  10103233, 10022181, 9930616, 9857426, 9838892]

    # 뒤에서 3번째부터 끝까지 슬라이싱
    print(year[len(year)-3:])
    print(population[len(population)-3:])


main()
