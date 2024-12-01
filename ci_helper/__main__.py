import argparse

def main():
    # Since setuptools_conda is self-hosting, it needs toml and distlib to read its own
    # requirements just to know that it needs to install toml and distlib! So bootstrap
    # that up if necessary.

    parser = argparse.ArgumentParser(
        prog='ci-helper', formatter_class=argparse.RawTextHelpFormatter,
    )

    print('main!')

if __name__ == '__main__':
    main()
