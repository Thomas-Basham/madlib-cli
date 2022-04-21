import re


def welcome_message():
    print("""
        **********************************************************
        Hello! Welcome to a MadLibs. TODO: Make input instructions
        **********************************************************
    """)


def read_template(some_text):
    try:
        with open(some_text, "r") as file:
            read_text = file.read()
            return read_text
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(some_text):

    keywords = re.findall(r"(?<=\{)(.*?)(?=\})", some_text)

    # stripped = some_text.format('', '', '')

    stripped = "It was a {} and {} {}."

    return stripped, tuple(keywords)


def merge(some_text, tup):
    return some_text.format(*tup)


welcome_message()
read_template("example.txt")
parse_template("example.txt")
merge("example.txt", ("words", "words", "words"))
