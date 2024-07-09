import os

def test_bazel_output_is_there():
    print("CHECKING IF THE FILE EXISTS")
    print("CWD: ", os.getcwd())
    os.stat("cpp/hello_cpp")
