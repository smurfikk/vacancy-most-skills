word = "python"  # слово по которому искать вакансии
most_common = 5  # сколько навыков выводить
url_parse = f"https://hh.ru/search/vacancy?text={word}&salary=&ored_clusters=true&area=1"
black_words = (
    word,
    "etc",
    "api",
    "to",
    "it",
    "backend",
    "g",
    "a",
    "of",
    "in",
    "open",
    "s",
    "test",
    "web",
    "review",
    "code",
)
logging_to_console = False
