import csv
import os
from pathlib import Path

def read_csv_movies(ratings, preference_key,sizeOf):
    pk = str(preference_key)
    script_path = Path(__file__, '..').resolve()
    with open(script_path.joinpath("movie_results.csv"), encoding="utf8") as file:
        reader = csv.reader(file)
        # Reverse if flag is marked
        if (int(ratings) == 0) :
            reader = reversed(list(reader))
        # new list to store results
        lista = []
        i = 0
        for row in reader :
            if row[0] == pk :
                print(row[0], row[1], row[3])
                i += 1
                # add desired result to list
                lista.append(row)
            # End at desired capacity
            if i == int(sizeOf):
                break
    return lista

def main():
    print("Reading...")
    read_csv_movies(1,2,2)
    print("Finished")

    return

if __name__ == "__main__":
     main()