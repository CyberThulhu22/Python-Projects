import sys
import argparse

# Instantiate Parse
parser = argparse.ArgumentParser()

# Instantiate Sub-Parsers
sub_parser = parser.add_subparsers(dest="mode")

# Add Sub_Parser
fm_parser = sub_parser.add_parser('fm', help="First Mode")
sm_parser = sub_parser.add_parser('sm', help="Second Mode")

# Add Sub_Parser Arguments
fm_parser.add_argument("-f", "--first", dest="fm_first")
fm_parser.add_argument("-s", "--second", dest="fm_second")
sm_parser.add_argument("-f", "--first", dest="sm_first")
sm_parser.add_argument("-s", "--second", dest="sm_second")

args = parser.parse_args()

def main():
    print(args)

if __name__ == "__main__":
    main()
