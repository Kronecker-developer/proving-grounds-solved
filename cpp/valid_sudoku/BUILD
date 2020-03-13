cc_library(
    name = "valid_sudoku",
    srcs = ["valid_sudoku.cpp"],
    hdrs = ["valid_sudoku.hpp"],
)

cc_binary(
    name = "main",
    srcs = ["main.cpp"],
    deps = [":valid_sudoku"],
)

cc_test(
    name = "valid_sudoku_test",
    srcs = ["valid_sudoku_test.cpp"],
    deps = [
        "@gtest//:gtest",
        "@gtest//:gtest_main",
        ":valid_sudoku"
    ],
)
