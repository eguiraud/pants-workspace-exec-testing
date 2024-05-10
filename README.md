# Pants Workspace Execution Testing

This is an example project desiged for testing the "in-workspace" execution
support being developed as per the ["In-Workspace Process Execution" design document](https://docs.google.com/document/d/1jUZTQHmUBr-Ij0nXOO0QX2Bq6XNANJg4-GNzhiOL4Xs/edit?usp=sharing).


## Running

1. Checkout Pants to [this branch](https://github.com/tdyas/pants/tree/shell_workspace_support_2)
   in a peer directory to this repository:

   New clone:

   ```
   cd ..
   git clone git@github.com:tdyas/pants.git
   git checkout --track origin/shell_workspace_support_2
   ./pants --version  # forces Rust compile
   cd pants-workspace-exec-testing
   ```

   Or add fork to an existing Pants clone:

   ```
   cd ../pants
   git remote add tdyas git@github.com:tdyas/pants.git
   git fetch tdyas
   git checkout --track tdyas/shell_workspace_support_2
   ./pants --version  # forces Rust compile
   cd pants-workspace-exec-testing
   ```

2. Run `PANTS_SOURCE=../pants pants run //:run-from-bazel`. The output should be the size of the
   jar file captured from the in-workspace execution (as printed by `ls`).
