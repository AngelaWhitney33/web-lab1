import os
import nltk
import sys
import io
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from email.parser import Parser


def email_analyse(inputfile, outputfile, stopwords):
    with open(inputfile, "r", encoding='utf-8', errors='ignore') as f:
        data = f.read()

    email = Parser().parsestr(data)

    words = word_tokenize(email.get_payload())
    stem_words = [PorterStemmer().stem(word) for word in words]
    useful_words = [
        word for word in stem_words if word not in stopwords]

    frequency = nltk.FreqDist(useful_words)
    with open(outputfile, "w") as f:
        f.write('\n'.join('%s %s' % x for x in frequency.most_common()))


def main():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

    my_stopwords = []
    with open("src/my_stopwords", "r") as f:
        for line in f.readlines():
            my_stopwords.append(line[:-1])
    my_stopwords.extend(stopwords.words('English'))

    rootdir = "dataset"
    for directory, subdirectory, filenames in os.walk(rootdir):
        temp = directory.split('/', 1)[-1]
        path = os.path.join("output", temp)
        if not os.path.exists(path):
            os.makedirs(path)
            count = 1
            total = len(filenames)
            for filename in filenames:
                email_analyse(os.path.join(directory, filename), os.path.join(path, filename), my_stopwords)
                print("\r%s completing %d/%d" % (path, count, total), end="")
                count += 1
                if count == total:
                    print("\r%s completed! %d/%d" % (path, count, total))

if __name__ == "__main__":
    main()
