# Pants Workspace Execution Testing (C++@Proxima version)

This branch showcases a problem with `experimental_wrap_as_resources`.
To reproduce:

```
PANTS_SOURCE=/home/devuser/pants pants --keep-sandboxes=always test --output=all --force //cpp:bazel_output_from_python_test -- -s -vv
```
