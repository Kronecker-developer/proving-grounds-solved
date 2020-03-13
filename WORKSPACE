load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository", "new_git_repository")

git_repository(
    name = "gtest",
    remote = "https://github.com/google/googletest",
    commit = "3306848f697568aacf4bcca330f6bdd5ce671899",
)

new_git_repository(
    name = "requests_repo",
    remote = "https://github.com/psf/requests.git",
    tag = "v2.23.0",
    build_file_content = """
py_library(
    name = "requests",
    srcs = glob(["requests/*.py"]),
    imports = ["requests"],
    visibility = [ "//visibility:public" ],
)""",
)