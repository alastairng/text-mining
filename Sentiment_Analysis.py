from Processed import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def sentiments(text):
    """
    This compiles a list of sentiment results of each tweet in text.
    text: list of tweets
    """
    result = []
    for tweet in text:
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        result.append(score)

    return result

# Finding the average of the positivity and negativity score of the 100 tweets

def positivity(x):
    pos = float()
    for i in x:
        pos += i['pos']
    pos = pos/len(x)
    return pos

def negativity(x):
    neg = float()
    for i in x:
        neg += i['neg']
    neg = neg/len(x)
    return neg


def main():
    elon = open_file('elontweets.pickle')
    trump = open_file('trumptweets.pickle')

    elons = sentiments(elon)
    trumps = sentiments(trump)

    write_file(elons, 'sentimentsElon')
    write_file(trumps, 'sentimentsTrump')

    print('Mean positivity in Elon\'s tweets:', end=" ")
    print(positivity(elons))
    print('Mean positivity in Trump\'s tweets:', end=" ")
    print(positivity(trumps))

    print('Mean negativity in Elon\'s tweets:', end=" ")
    print(negativity(elons))
    print('Mean negativity in Trump\'s tweets:', end=" ")
    print(negativity(trumps))


if __name__ == '__main__':
    main()