import os
import operator

sidebar_content = []


def walk_one_directory(directory, directory_prefix, level):
    readme_path = os.path.join(directory, "README.md")
    if not os.path.exists(readme_path):
        print(directory + ": README.md file not found.")
    if not os.path.isfile(readme_path):
        print(directory + ": README.md is not a file.")

    buf_string = (" " * level) + "* [" + os.path.basename(directory) + "](/" + directory_prefix + "/)\n"
    sidebar_content.append(buf_string)

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            walk_one_directory(item_path, directory_prefix + "/" + item, level + 1)

        if os.path.isfile(item_path):
            if operator.eq(item, "README.md") or not item.endswith(".md"):
                continue

            buf_string = (" " * (level + 1)) + "* [" + os.path.basename(item_path)[:-3] + "](/" + \
                         directory_prefix + "/" + os.path.basename(item_path)[:-3] + ")\n"
            sidebar_content.append(buf_string)


def main():
    docs_dir = input("输入文档根目录: ")
    if not os.path.exists(docs_dir):
        print(docs_dir + ": Not found")

    if not os.path.isdir(docs_dir):
        print(docs_dir + ": Not a directory.")

    root_readme = os.path.join(docs_dir, "README.md")
    if not os.path.exists(root_readme):
        print(docs_dir + ": README.md file not found.")

    if not os.path.isfile(root_readme):
        print(docs_dir + ": README.md is not a file.")

    for item in os.listdir(docs_dir):
        item_path = os.path.join(docs_dir, item)
        if os.path.isdir(item_path):
            walk_one_directory(item_path, os.path.basename(item_path), 0)


if __name__ == "__main__":
    main()
    with open("sidebar.md", mode="w") as f:
        for line in sidebar_content:
            f.write(line)
