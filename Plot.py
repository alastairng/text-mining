from Sentiment_Analysis import *
import matplotlib.pyplot as plt


def create_list(dic, key):
    """Creates a list of values extracted from the list of dictionaries 'dic', taking the
        value from the same key in each dictionary.
    """
    array = []
    for i in dic:
        array.append(i[key])
    return array


def scat_plot(a,b,s):
    """Takes two lists and creates a scatterplot of both these lists created above
        on the same scatterplot.
    s = String. Either 'pos' for positivity analysis or 'neg' for negativity analysis
    """
    x = range(len(a))
    y = range(len(b))
    fig = plt.figure()
    axi = fig.add_subplot(111)

    axi.scatter(x, sorted(a), s=10, c='g', marker="s", label='Elon')
    axi.scatter(y, sorted(b), s=10, c='r', marker="o", label='Trump')   

    if(s == 'pos'):
        axi.scatter(y, [0.11196 for i in range(len(b))], s=10, c='black', marker="o", label='Mean Elon')
        axi.scatter(x, [0.10312 for i in range(len(a))], s=10, c='y', marker="o", label='Mean Trump')
        axi.set_xlabel("Number of Tweets")
        axi.set_ylabel("Positivity Score")
        axi.set_title("Positivity Analysis")
        plt.legend(loc= 2)
        plt.show()
    if(s =='neg'):
        axi.scatter(y, [0.05716 for i in range(len(b))], s=10, c='black', marker="o", label='Mean Elon')
        axi.scatter(x, [0.05689 for i in range(len(a))], s=10, c='y', marker="o", label='Mean Trump')
        axi.set_xlabel("Number of Tweets")
        axi.set_ylabel("Negativity Score")
        axi.set_title("Negativity Analysis")
        plt.legend(loc= 2)
        plt.show()


def main():
    elon = open_file('sentimentsElon.pickle')
    trump = open_file('sentimentsTrump.pickle')

    elonpos = create_list(elon, 'pos')
    trumppos = create_list(trump, 'pos')

    scat_plot(elonpos, trumppos, 'pos')

    elonneg = create_list(elon, 'neg')
    trumpneg = create_list(trump, 'neg')

    scat_plot(elonneg, trumpneg, 'neg')


if __name__ == '__main__':
    main()