# Pants Workspace Execution Testing

This is an example project desiged for testing the "in-workspace" execution
support being developed.

## Running

1. Checkout Pants to [this branch](https://github.com/tdyas/pants/tree/shell_workspace_support)
   in a peer directory to this repository.

2. Run `PANTS_SOURCE=../pants pants run //:run-from-bazel`. The output should be the size of the
   jar file captured from the in-workspace execution (as printed by `ls`).
