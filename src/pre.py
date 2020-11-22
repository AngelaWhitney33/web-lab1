import os
from operator import itemgetter
from nltk.corpus import stopwords

def freq_analysis(inputfile, dictionary):
    with open(inputfile, "r") as f:
        for line in f:
            key = line.split(' ')[0]
            value = int(line.split(' ')[1])
            if dictionary.__contains__(key):
                dictionary[key] += value
            else:
                dictionary[key] = value


def main():
    # rootdir = "output/dataset"
    # outdir = "output/count"
    # for people in os.listdir(rootdir):
    #     path = os.path.join(rootdir, people)
    #     people_dict = dict()
    #     for directory, subdirectory, filenames in os.walk(path):
    #         for filename in filenames:
    #             freq_analysis(os.path.join(directory, filename), people_dict)
    #     with open('output/count/' + people + '.csv', 'w') as f:
    #         [f.write('{0} {1}\n'.format(key, value)) for key, value in people_dict.items()]
    # dictionary = dict()
    # rootdir = 'output/count'
    # count = 0
    # for filename in os.listdir(rootdir):
    #     with open(os.path.join(rootdir, filename), "r") as f:
    #         for line in f:
    #             sep = line.rfind(',')
    #             key = line[0: sep]
    #             value = int(line[sep + 1: -1])
    #             if dictionary.__contains__(key):
    #                 dictionary[key] += value
    #             else:
    #                 dictionary[key] = value
    #         count += 1
    #         print("\rcount = %d/150" % count, end='')
    # with open('output/count.csv', 'w') as f:
    #     [f.write('{0} {1}\n'.format(key, value)) for key, value in dictionary.items()]
    my_stopwords = []
    with open("src/my_stopwords", "r") as f:
        for line in f.readlines():
            my_stopwords.append(line[:-1])
    my_stopwords.extend(stopwords.words('English'))

    dictionary = dict()
    with open("output/count.csv", "r") as f:
        for line in f:
            sep = line.rfind(' ')
            key = line[0: sep]
            value = int(line[sep + 1: -1])
            dictionary[key] = value

    sorted_dict = sorted(dictionary.items(), key=itemgetter(1), reverse=True)
    with open('output/sorted_count.csv', 'w') as f:
        [f.write('{0} {1}\n'.format(key, value)) for key, value in sorted_dict if key not in my_stopwords]

if __name__ == "__main__":
    main()
