# Enki Prefixer

This simple `Python` script that recursively crawls through (Enki's curriculum)[https://github.com/enkidevs/curriculum] renaming `folders` and `.md` documents according to their order.

This order is defined by the contents of the `README.md` in their respective folder.

## Installation/Use

1. Download the `format.py` script.
2. Put the `format.py` in the highest-level folder that you would like to prefix.
3. Run the script.
(If you'd like more detailed instructions, let me know)

## How it works

1. The script uses `os.path` to work out where it is.
2. It tries to open the `README.md` in the current folder; if there isn't one, it will just pretend it was empty.
3. A list of all the lines in this file that could be referring to a file/folder is built.
4. A list of the files/folders in the current folder is made
5. The script then renames any matching entries (for folders and `.md` files) incrementing a counter for each file found.
6. The script then builds a list of all the folders in the current folder and repeats the process for each one.

## Contributions

So far, this has worked astonishingly well, but make an `Issue` if there are any bits that don't work as intended.

Pull requests are welcome, but **not** encouraged without an `Issue`.
