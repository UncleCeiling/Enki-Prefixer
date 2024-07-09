import os


def get_dir() -> str:
    """Returns a string containing the Path to the directory that this script is in."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"+++Got directory: {current_dir}+++")
    return current_dir


def read_readme(dir: str) -> list:
    """Returns the relevant lines from the `README.md` file in the specified directory.

    Returns an empty list if the `README.md` cannot be found."""
    readme_loc = os.path.join(dir, "README.md")
    try:
        with open(readme_loc, "r") as readme_file:
            readme_lines = [line.strip()[2:] for line in readme_file if "-" in line]
        # print(readme_lines)
        print(f" > Successfully fetched: {dir}/README.md")
        return readme_lines
    except:
        print(f" X Failed to fetch: {dir}/README.md")
        return []


def read_items(dir: str) -> list:
    """Returns a list of the items in this directory."""
    items = [item for item in os.listdir(dir)]
    print(f"+++Found items: {len(items)}+++")
    return items


def get_dirs(dir: str) -> list:
    """Returns a list of the directories in the specified directory."""
    directories = [
        item for item in os.listdir(dir) if os.path.isdir(os.path.join(dir, item))
    ]
    return directories


def format_dir(dir: str) -> None:
    """Recursively checks file/directory names in the specified directory, and prefixes them in the order that it finds them in the `README.md`."""
    print(f"+++Current path: {dir}+++")
    readme_lines = read_readme(dir)
    items = read_items(dir)
    counter = 0
    for item in readme_lines:
        if item in items:
            try:
                counter += 1
                name = str(counter).rjust(2, "0") + " " + item
                os.rename(
                    os.path.join(dir, item),
                    os.path.join(dir, name),
                )
                print(f" > Successfully renamed: {name}")
            except Exception as exception:
                print(f" X Failed to rename: {name}")
        elif item + ".md" in items:
            try:
                counter += 1
                name = str(counter).rjust(2, "0") + " " + item + ".md"
                os.rename(
                    os.path.join(dir, item + ".md"),
                    os.path.join(dir, name),
                )
                print(f" > Successfully renamed: {name}")
            except Exception as exception:
                print(f" X Failed to rename: {name}")
        else:
            print(f" / Skipping item: {item}")
    # print(readme_lines, items)
    print(f"===Successfully renamed {counter} items===")
    for directory in get_dirs(dir):
        if directory != "curriculum":
            format_dir(os.path.join(dir, directory))
        else:
            print(" / Skipping `curriculum`")


def main():
    current_dir = get_dir()
    format_dir(current_dir)


if __name__ == "__main__":
    main()
