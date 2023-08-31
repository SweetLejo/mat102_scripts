import cesar


def open_file_and_return_str(file_path : str) -> str:
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)



open_file_and_return_str("romeo_juliet.txt")


if __name__ == "main":
    open_file_and_return_str("romeo_juliet.txt")
    