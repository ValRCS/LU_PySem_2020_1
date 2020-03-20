import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print a greeting')
    # we will define some arguments here
    parser.add_argument("-n", "--name",
                        help='Name of the greeting')
    parser.add_argument(
        "-c", type=int, help="How many times to print the greeting")
    parser.add_argument('-f', '--foo', default=42)
    # we will parse the arguments now
    args = parser.parse_args()
    print(args.foo, type(args.foo))
    for _ in range(args.c):
        print(f"Hello {args.name}")
