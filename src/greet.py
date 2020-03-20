# import hw
import sys

if __name__ == "__main__":
    print(f"Greetings we got {len(sys.argv)}")
    for arg in sys.argv:
        print(f"Our argument is {arg}")
    for _ in range(int(sys.argv[2])):
        print(sys.argv[1])
