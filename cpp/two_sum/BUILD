cc_library(
    name = "two_sum",
    srcs = ["two_sum.cpp"],
    hdrs = ["two_sum.hpp"],
)

cc_binary(
    name = "main",
    srcs = ["main.cpp"],
    deps = [":two_sum"],
)

cc_test(
    name = "two_sum_test",
    srcs = ["two_sum_test.cpp"],
    deps = [
        "@gtest//:gtest",
        "@gtest//:gtest_main",
        ":two_sum"
    ],
)
