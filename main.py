import sys

if len(sys.argv) > 1:
    name_parameter = sys.argv[1]
else:
    name_parameter = "Default Name"

print(f"Hello {name_parameter}")
