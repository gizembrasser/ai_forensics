import os
import argparse
import pandas as pd
import time
from prompting.prompt_gpt import get_gpt_responses
from prompting.prompt_gemini import get_gemini_responses
from prompting.prompt_llms import test_llms_parallel


def main(input_file, column_name, output_file, num_rows=None):
    start_time = time.time()

    # Define the LLMs to test
    llms = {
        'OpenAI': get_gpt_responses,
        'Google Gemini': get_gemini_responses,
    }

    # Read the Excel file and extract the prompts
    df_prompts = pd.read_excel(input_file)

    if column_name not in df_prompts.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the Excel file.")
    
    # If num_rows is specified, use only that many rows
    if num_rows is not None:
        df_prompts = df_prompts.head(num_rows)

    prompts = df_prompts[column_name].tolist()

    # Test the LLMs
    responses = test_llms_parallel(llms, prompts)

    # Ensure the output directory exists
    os.makedirs('output', exist_ok=True)
    output_path = os.path.join('output', output_file)

    # Write the responses to an Excel file
    df_responses = pd.DataFrame(responses, columns=['prompt', 'answer', 'model'])
    df_responses.to_excel(output_path, index=False)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Responses have been written to {output_path}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process prompts from an Excel file.")
    parser.add_argument("input_file", help="The path to the Excel file containing the prompts.")
    parser.add_argument("column_name", help="The name of the column containing the prompts.")
    parser.add_argument("output_file", help="The name of the output Excel file to store responses.")
    parser.add_argument("--num_rows", type=int, help="The number of rows to process from the input file.")

    args = parser.parse_args()
    main(args.input_file, args.column_name, args.output_file, args.num_rows)