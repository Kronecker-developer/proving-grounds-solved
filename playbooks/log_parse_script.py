import sys
import re

log_file_path = sys.argv[1]
f = open(log_file_path, "r")

expression = "(Executed(.+)out\sof(.+)tests:(.+)tests\spass)"
for line in f:
    if bool(re.search(expression, line)):
        x = re.split("\s", line)

executed = x[1]
passed = x[6]
total = x[4]

print("Executed  tests: "+executed)
print("Passed tests: "+passed)
print("Total tests: "+total)

f.close()

