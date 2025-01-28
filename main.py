import os
import PyInstaller.__main__


COMPILE_DIR = "bin"


def main():
    # check compile folder
    if not os.path.isdir(COMPILE_DIR):
        os.makedirs(COMPILE_DIR)

    for file in os.listdir("source"):
        path = os.path.join("source", file)
        print(f"Compiling '{path}'")
        PyInstaller.__main__.run([
            path,
            "--onefile",
            "--noconsole",
            f"--name {os.path.join(COMPILE_DIR, os.path.splitext(file)[0])}"
        ])


if __name__ == '__main__':
    main()
