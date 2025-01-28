import os


COMPILE_DIR = "bin"


def main():
    # check compile folder
    if not os.path.isdir(COMPILE_DIR):
        os.makedirs(COMPILE_DIR)

    for file in os.listdir("source"):
        pass


if __name__ == '__main__':
    main()
