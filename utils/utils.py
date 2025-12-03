import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str)
    parser.add_argument("-automation", action="store_true")
    parser.add_argument("-test_case", action="store_true")
    return parser.parse_args()


# Example usage:
# python -m agents.agent https://api.swaggerhub.com/apis/endava-adf/Auth-Demo/1.0.0 -automation -test_case
# python -m agents.agent https://api.swaggerhub.com/apis/endava-adf/Auth-Demo/1.0.0 -test_case
