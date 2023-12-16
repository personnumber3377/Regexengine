import re


regex_string = r"\\([0-9]+)"
matcher = re.compile(regex_string)

print(matcher.match("\\10").group())
