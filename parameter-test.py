import argparse
import parser

parser = argparse.ArgumentParser()
parser.add_argument("--org",required=True)
parser.add_argument("--projectName",required=True)
parser.add_argument("--workItemType",required=True)
parser.add_argument("--ruleType",required=True)
parser.add_argument("--stageCategory",required=True)
args=parser.parse_args()

print(args.org, ', ',args.projectName,', ',args.workItemType,', ',args.ruleType,', ',args.stageCategory)
