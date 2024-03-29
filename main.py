import sys

if len(sys.argv) > 1:
    name_parameter = sys.argv[1]
    print(len(sys.argv[1]))
    print(type(sys.argv[1]))
    print(f"Hello {name_parameter}")
else:
    print(len(sys.argv))
    print(type(sys.argv))
    name_parameter = "Default Name"
    print(f"Hello {name_parameter}")
