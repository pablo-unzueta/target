from argparse import ArgumentParser
from src.utils.logo import print_logo
from src.utils.process import process

def main():
    parser = ArgumentParser()
    parser.add_argument("--config", help="path to config.yaml file")
    args = parser.parse_args()
    config = process(args.config)
    print(config)
    

if __name__ == "__main__":
    # print("TARGET: Torch AIMS Reimplementation for General Electronic sTructure packages")
    # print("By: Pablo A. Unzueta and Todd J. Martinez")
    # print_logo()
    main() 
    # print("End of Run...")
    # print("Buy Pablo Coffee and Beer :)")


