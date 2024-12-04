import argparse
import random

# Test fil for parallel running at job script

print(" start ")

parser = argparse.ArgumentParser()
parser.add_argument("--seed", type=int, required=True)
parser.add_argument("--n_veh", type=int, required=True)

args = parser.parse_args()
print(" args.seed ", args.seed)
print(" args.n_veh ", args.n_veh)
print(" finish ")