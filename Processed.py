import pickle, string, nltk, os
from nltk.corpus import stopwords 
nltk.download('stopwords')

def open_file(filename):
    input_file = open(filename,'rb')
    tweets = pickle.load(input_file)
    input_file.close()
    return tweets

def process_file(filename):
    """Makes a histogram that contains the words from a file.
    filename: string
    returns: frequency of words in a dictionary
    """
    
    hist = {}
    if filename[-7:] == '.pickle':
        data = open_file(filename)

        for line in data:
            line = line.replace('-', ' ')
            strippables = string.punctuation + string.whitespace

            # remove punctuation and convert to lowercase
            for word in line.split():
                word = word.strip(strippables)
                word = word.lower()
                hist[word] = hist.get(word, 0) + 1        
        return hist
    else:
        fp = open(filename, encoding='utf8')
        for line in fp:
            line = line.replace('-', ' ')
            strippables = string.punctuation + string.whitespace

            for word in line.split():
                word = word.strip(strippables)
                word = word.lower()
                hist[word] = hist.get(word, 0) + 1

        return hist


def similar(d1, d2):
    """Returns a dictionary with all keys that appear in d1 and d2.
    d1: pickle file
    d2: word.txt
    """
    result = {}
    for i in d1:
        if i in d2:
            result[i] = d1[i]
    return result

def final_words(dic):
    """
    Returns a list of words that have the stop words removed.
    dic is a dictionary
    returns a dictionary
    """
    #Check to see if the word is a stopword. If it is not a stopword, then append it to dictionary.
    
    stop = set(stopwords.words('english'))
    result = {}
    for i in dic: 
        if i not in stop:
            result[i]=dic[i]
    return result


def most_common(hist, num):
    """Makes a list of word-freq pairs in descending order of frequency. 
    num: number of results showed
    hist: map from word to frequency
    returns: list of num (frequency, word) pairs
    """
    com = []
    for word, freq in hist.items():
        com.append((freq, word))
    
    com.sort()
    com.reverse()
    return com[:num]

def write_file(hist, filename):
    """Writes a dictionary to a pickle file.
    filename: string without '.pickle'
    hist: dictionary
    """
    filename += '.pickle'


    if not os.path.exists(filename):
        f = open(filename,'wb')
        pickle.dump(hist,f)
        f.close()
        print('File created as {}.' .format(filename))
    else:
        response = input("File {} already exists. Replace existing? (Yes/No): " .format(filename))
        if response.lower() == 'yes':
            f = open(filename,'wb')
            pickle.dump(hist,f)
            f.close()
            print('File replaced as {}.' .format(filename))
        elif response.lower() == 'no':
            print('Action aborted.')

def main():
    input_file1 = open('elontweets.pickle','br')
    pickle.load(input_file1)
    
    hist1 = process_file('elontweets.pickle')
    words = process_file('words.txt')

    real_words1 = similar(hist1, words)
    completed_words1 = final_words(real_words1)

    print("The processed words in the Elon tweets are:")    
    print(completed_words1)


    input_file2 = open('trumptweets.pickle','br')
    pickle.load(input_file2)
    
    hist2 = process_file('trumptweets.pickle')
    words = process_file('words.txt')

    real_words2 = similar(hist2, words)
    completed_words2 = final_words(real_words2)

    print("The processed words in the Trump tweets are:")    
    print(completed_words2)

    print('Most common words in Elon tweets are:')
    print(most_common(completed_words1, 20))
    print('Most common words in Trump tweets are:')
    print(most_common(completed_words2, 20))

    write_file(completed_words1, 'processedElon')
    write_file(completed_words2, 'processedTrump')
    

if __name__ == '__main__':
    main()