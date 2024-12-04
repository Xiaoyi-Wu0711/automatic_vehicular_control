import argparse
import random
print(" start ")

parser = argparse.ArgumentParser()
parser.add_argument("--seed", type=int, required=True)
args = parser.parse_args()

a = random.seed(args.seed)
print(" args.seed ", args.seed)
print("a ", a)
print(" finish ")