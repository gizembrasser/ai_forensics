import os
import pandas as pd
import time
from prompting.prompt_gpt import get_gpt_responses
from prompting.prompt_gemini import get_gemini_responses
from prompting.prompt_llms import prompt_llms_parallel
from analysis.classify_completions_strmatch import strmatch_label
from analysis.keywords import contains_keywords
from core.commands import create_parser


def main(INPUT_FILE, COLUMN_NAME, OUTPUT_FILE, NUM_ROWS=None):
    df = pd.read_excel(INPUT_FILE)

    if COLUMN_NAME not in df.columns:
        raise ValueError(f"Column '{COLUMN_NAME}' does not exist in the Excel file.")
    
    # If NUM_ROWS is specified, use only that many rows
    if NUM_ROWS is not None:
        df = df.head(NUM_ROWS)

    prompts = df[COLUMN_NAME].tolist()

    if args.command == "prompt":
        start_time = time.time()

        # Define the LLMs to test
        llms = {
            'OpenAI': get_gpt_responses,
            'Google Gemini': get_gemini_responses,
        }

        # Test the LLMs
        responses = prompt_llms_parallel(llms, prompts)
 
        # Write the responses to an Excel file
        output_path = os.path.join('output', OUTPUT_FILE)
        df_responses = pd.DataFrame(responses, columns=['prompt', 'answer', 'model'])
        df_responses.to_excel(output_path, index=False)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Responses have been written to {output_path}")
        print(f"Time taken: {elapsed_time:.2f} seconds")
    
    if args.command == "str_classify":
        df["strmatch_label"] = df[COLUMN_NAME].apply(lambda x: strmatch_label(x))

        output_path = os.path.join('output', 'classified', OUTPUT_FILE)
        df.to_excel(output_path, index=False)

        print(f"Responses have been written to {output_path}")
     
    if args.command == "keywords":
        df["contains_keywords"] = df[COLUMN_NAME].apply(lambda x: contains_keywords(x))

        output_path = os.path.join('output', 'classified', OUTPUT_FILE)
        df.to_excel(output_path, index=False)

        print(f"Responses have been written to {output_path}")

if __name__ == "__main__":
    args = create_parser()
    main(args.input_file, args.column_name, args.output_file, args.num_rows)
