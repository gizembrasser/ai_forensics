import argparse

def create_parser():
    parser = argparse.ArgumentParser(prog="python main.py", 
                                     description="Send prompts from an Excel file to LLM API's and classify the responses.")
    subparsers = parser.add_subparsers(dest='command')

    prompt_parser = subparsers.add_parser('prompt', help="Run the prompts to the API's.")
    prompt_parser.add_argument("input_file", help="The path to the Excel file containing the prompts.")
    prompt_parser.add_argument("column_name", help="The name of the column containing the prompts.")
    prompt_parser.add_argument("output_file", help="The name of the output Excel file to store responses.")
    prompt_parser.add_argument("--num_rows", type=int, help="The number of rows to process from the input file.")

    classify_parser = subparsers.add_parser('str_classify', help='Run the string classification.')
    classify_parser.add_argument("input_file", help="The path to the Excel file containing the responses.")
    classify_parser.add_argument("column_name", help="The name of the column containing the responses.")
    classify_parser.add_argument("output_file", help="The name of the output Excel file to store classified results.")
    classify_parser.add_argument("--num_rows", type=int, help="The number of rows to process from the input file.")

    keywords_parser = subparsers.add_parser('keywords', help='Check whether responses contain one or more keywords.')
    keywords_parser.add_argument("input_file", help="The path to the Excel file containing the responses.")
    keywords_parser.add_argument("column_name", help="The name of the column containing the responses.")
    keywords_parser.add_argument("output_file", help="The name of the output Excel file to store classified results.")
    keywords_parser.add_argument("--num_rows", type=int, help="The number of rows to process from the input file.")

    args = parser.parse_args()

    return args
