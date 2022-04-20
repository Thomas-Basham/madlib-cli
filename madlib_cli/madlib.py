
def welcome_message():
    print("""
        **********************************************************
        Hello! Welcome to a MadLibs. TODO: Make input instructions
        **********************************************************
    """)


def read_template():

    template = open('example.txt')
    try:
        print(template.read())

    finally:

        template.close()
        print('Reader closed')


def parse_template():
    template = open('example.txt')
    try:
        user_input = input('> ')

        print("TODO: Parse template function")
    finally:

        template.close()


def merge():
    print("TODO: Merge Function")


welcome_message()
read_template()
parse_template()
