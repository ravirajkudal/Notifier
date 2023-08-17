import time
from english_words import get_english_words_set
import random
from plyer import notification


def drink():
    notification.notify(
        title="Drink water",
        message="For better physic \n YEE BUDDY!!!",
        app_icon="icon.ico",
        timeout=5
    )


def word_msg():
    words = list(get_english_words_set(['web2'], lower=True))
    word = random.choice(words)
    print(word)
    dic = PyDictionary()
    defines = dic.meaning(word)

    notification.notify(
        title=f"'{word}'",
        message=defines,
        app_icon="dict icon.ico",
        timeout=12
    )


if __name__ == '__main__':
    while True:
        drink()
        word_msg()
        time.sleep(60 * 90)  # sec and min
