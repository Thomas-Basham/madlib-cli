import re


def welcome_message():
    print("""
        **********************************************************
        Hello! Welcome to a MadLibs. TODO: Make input instructions
        **********************************************************
    """)


word_bank = ()


def read_template(some_text):
    try:
        with open(some_text, "r") as file:
            read_text = file.read()
            return read_text
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(some_text):
    stripped = ""
    keywords = re.findall(r"(?<=\{)(.*?)(?=\})", read_text)
    keywords_tuple = tuple(set(keywords))
    print(keywords_tuple
    return stripped, keywords

def merge():
    text = open(f"{some_text}", 'r')
    read_text = text.read()
    try:
        for i in keywords:
            user_input = input(f"{i}: ")
        print(f"{read_text.format(Adjective = user_input, Noun = user_input)}")

    finally:
        text.close()


welcome_message()
read_template("example.txt")
parse_template("example.txt")
# merge("example.txt")
