import re
import time
import requests
from bs4 import BeautifulSoup
from collections import Counter
from config import most_common, black_words, url_parse, logging_to_console


def main() -> None:
    text = parser_hh()
    text = clean_text(text)
    word_counter = Counter(text)
    print("{:<15} | {:<5}".format("Навык", "Кол-во"))
    for word, _count in reversed(word_counter.most_common(most_common)):
        print("{:<15} | {:<5}".format(word, _count))


def clean_text(_text: str) -> list[str]:
    words = re.findall(r"\b[a-z]+\b", _text.lower())
    words = [_word for _word in words if _word not in black_words]
    return words


def parser_hh() -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36",
    }

    session = requests.Session()
    if logging_to_console:
        print(f"get {url_parse}")
    res = session.get(url_parse, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    cards = soup.findAll("div", {"class", "serp-item"})
    descriptions: list[str] = list()
    for card in cards:
        link = card.find("a", {"class": "serp-item__title"}).get("href")
        if logging_to_console:
            print(f"get {link}")
        res = session.get(link, headers=headers)
        time.sleep(0.3)
        soup = BeautifulSoup(res.text, "html.parser")
        desc = soup.find("div", {"class", "vacancy-description"})
        if not desc:
            desc = soup.find("div", {"data-qa", "vacancy-description"})
        if not desc:
            continue
        descriptions.append(desc.text)
    return "\n".join(descriptions)


if __name__ == '__main__':
    main()
