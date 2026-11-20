import sys, os

def sys_demo():
    print("Python version")
    print(sys.version)
    print("Version info.")
    print(sys.version_info)
    print("System path:")
    print(sys.path)


def os_demo():
    cwd = os.getcwd()
    print("Current working directory:", cwd)
    print("Current working directory:", cwd)
    print("List of files in current directory:", os.listdir(cwd))
    print("Environment variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

    new_folder = "test_folder"
    demo_path = os.path.join(cwd, new_folder)


    if not os.path.exists(demo_path):
        os.makedirs(demo_path)
        print(f"Created new folder: {new_folder}")
    else:
        print(f"Folder already exists: {new_folder}")

    new_file = "test_file.txt"
    file_path = os.path.join(demo_path, new_file)
    # if not os.path.exists(file_path):
    with open(file_path, "w") as f1:
        f1.write("This is a test file.\n")
        lst = ["First\n", "Second\n", "Third\n"]
        f1.writelines(lst)
        print(f"{f1.writable() = }")
        print(f"{f1.readable() = }")
        f1.flush()
        f1.write("This is the second line.\n")
    # except Exception as e:
    #     print(f"An error occurred while writing to the file: {e!r}")
    # finally:
    #     f1.close()

    if os.path.exists(file_path):
        with open(file_path, "r") as f2:
            print(f"{f2.readable() = }")
            content = f2.read()
            print("File content:")
            print(content)

            f2.seek(0)  # Move the cursor back to the beginning of the file

        # with open(file_path, "r") as f3:
            data = f2.readlines()
            print("File content as list of lines:")
            print(data)

# sys_demo()
os_demo()