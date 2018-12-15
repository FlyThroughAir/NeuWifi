import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, default='login', help='input "login" or "logout" ')
args = parser.parse_args()
print(args.type)