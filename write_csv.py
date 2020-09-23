import csv

def write_csv(data): #writes contet to csv file
    with open('ducks.csv', 'w', newline = '') as csvfile:

        fnames = ['title','sold','ducks sold together', 'link']
        writer = csv.DictWriter(csvfile, fnames)

        for item in data:
            print(item)
            writer.writerow(item)



