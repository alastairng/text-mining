from twython import Twython
import pickle
import os


def create_file(filename, query):
    """This function creates a new pickle file containing a list of tweets
        resulting from the input query.
        filename - This is the name of the file you want to use to save the tweets in
        query - This is the twitter search query to use to search for tweets.
    """
    # Replace the following strings with your own keys and secrets
    TOKEN = '979038392083197952-NgdBxjQVFX1tK1HR8GH5E3Za5XpxFWP'
    TOKEN_SECRET = 'NKJUnbWIlhSmpIHMnxuIFgAI447yfi2ON7SFx7ClG2dXP'
    CONSUMER_KEY = '11OsLJ0nhOvmZPmDkYVRdD8mI'
    CONSUMER_SECRET = 'JXTBOCm7Ub0eBTEFaynXrjhbFAQrLyANfzIL0dVL8M2GvvqOJ2'

    t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

    result = t.search(q=query, count=100)

    tweets = list()

    for status in result['statuses']:
        tweets.append(status['text'])

    filename += '.pickle'


    if not os.path.exists(filename):
        f = open(filename,'wb')
        pickle.dump(tweets,f)
        f.close()
        print('File created as {}.' .format(filename))
    else:
        prompt = input("File {} exists. Replace existing? (Yes/No):" .format(filename))
        if prompt.lower() == 'yes':
            f = open(filename,'wb')
            pickle.dump(tweets,f)
            f.close()
            print('File replaced as {}.' .format(filename))
        elif prompt.lower() == 'no':
            print('No File Created.')


def open_file(filename):
    input_file = open(filename,'rb')
    tweets = pickle.load(input_file)
    input_file.close()
    return tweets


def main():
    create_file('elontweets', '@elonmusk')
    create_file('trumptweets', '@realDonaldTrump')
if __name__ == '__main__':
    main()
   