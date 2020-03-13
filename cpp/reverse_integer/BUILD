cc_library(
    name = "reverse_integer",
    srcs = ["reverse_integer.cpp"],
    hdrs = ["reverse_integer.hpp"],
)

cc_binary(
    name = "main",
    srcs = ["main.cpp"],
    deps = [":reverse_integer"],
)

cc_test(
    name = "reverse_integer_test",
    srcs = ["reverse_integer_test.cpp"],
    deps = [
        "@gtest//:gtest",
        "@gtest//:gtest_main",
        ":reverse_integer"
    ],
)
