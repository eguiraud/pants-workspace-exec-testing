import os

if __name__ == "__main__":
    print("CHECKING IF THE FILE EXISTS")
    print("CWD: ", os.getcwd())
    os.stat("cpp/hello_cpp")
