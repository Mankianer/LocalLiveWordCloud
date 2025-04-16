from wordcloud import WordCloud
import matplotlib.pyplot as plt



def show_wortwolke(files: [str] = ["input2.txt"]):
    text = ''
    # read text from files arguments
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            text += f.read()

    # Generate a word cloud image
    wordcloud = wordcloud = WordCloud(
        width=1920,
        height=1080,
        background_color="#FFE4D6",
        colormap="inferno",
        max_font_size=200,
        min_font_size=10,
        max_words=100,
        font_path=None  # Optional: Pfad zu einer Schriftart
    ).generate(text)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    # Save the word cloud image to a file
    wordcloud.to_file("wordcloud.png")
    # save with 1080p resolution


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # show_wortwolke(["input1.txt"])
    show_wortwolke(["input1.txt", "input2.txt"])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
