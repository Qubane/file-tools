import os
import PyInstaller.__main__


COMPILE_DIR = "bin"


def main():
    # check compile folder
    if not os.path.isdir(COMPILE_DIR):
        os.makedirs(COMPILE_DIR)

    for file in os.listdir("source"):
        path = os.path.join("source", file)
        PyInstaller.__main__.run([
            path,
            "--onefile",
            "--noconsole",
            "--distpath",
            COMPILE_DIR
        ])


if __name__ == '__main__':
    main()
