import pandas as pd
import numpy as np
from semf import SEMF
from ga import GA
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a Genetic Algorithm to find the Semi-Empirical Mass Formula coefficients.')
    parser.add_argument('--file_name', type=str, help='a name for the file containing the results')
    args = parser.parse_args()

    data = pd.read_csv("nudat_data.csv")
    results_file = open(args.file_name+".txt", "w")
    training_data = data.sample(n=250)
    population_size = 500
    
    my_ga = GA(population_size)

    n=0
    while True:
        print(n)
        results_file.writelines("Generation number {}\n".format(n))
        my_ga.calc_fitness(training_data)
        if n==200:
            break        
        results_file.writelines(my_ga.find_best())
        my_ga.mate()
        my_ga.mutate(0.5, 1)
        my_ga.mutate(0.1, 50)
        n+=1

    results_file.writelines("Final results:\n")
    results_file.writelines(my_ga.find_best())