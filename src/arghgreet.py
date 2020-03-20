import argh


def main(name="Valdis", count=3):
    """
    Printing a greeting message
    For our friends
    """
    for _ in range(count):
        print(f'Hello {name}')
    return None


if __name__ == "__main__":
    argh.dispatch_command(main)
