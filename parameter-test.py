import argparse
import parser

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("org")
parser.add_argument("projectName")
parser.add_argument("workItemType")
parser.add_argument("ruleType")
parser.add_argument(" stageCategory")
args=parser.parse_args()

print(args.org, ', ',args.projectName,', ',args.workItemType,', ',args.ruleType,', ',args.stageCategory)
