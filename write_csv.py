import csv

def write_csv(data):

    with open('ducks.csv', 'w', newline = '') as csvfile:

        fnames = ['title','sold','ducks sold together', 'link']
        writer = csv.DictWriter(csvfile, fnames)

        # row = [
        #     data['title'],
        #     data['sold'],
        #     data['ducks sold together']
        #        ]
        for item in data:
            print(item)
            writer.writerow(item)

    pass

