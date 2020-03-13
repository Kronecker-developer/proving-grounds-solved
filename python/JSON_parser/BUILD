py_library(
    name = "JSON_parser",
    srcs = ["JSON_parser.py"],
    deps = [
        "@requests_repo//:requests"
    ],
)

py_test(
    name = "JSON_parser_test",
    srcs = ["JSON_parser_test.py"],
    deps = [
        ":JSON_parser"
    ],
)
