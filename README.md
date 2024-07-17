# Testing moderation on LLM's

This repo consists of two main functionalities: 
1. Running a list of prompts to different models of LLM's (currently ChatGPT, Gemini and Ollama) through their API's.
2. Classifying which of the prompts the model refused to answer, or complied with, based on string matching.

## Automated prompting

### OpenAI and Gemini API's

- Put your Excel file containing prompts in the `input` folder. Remember the name of the column containing your prompts.

- In the textfiles in the `input/models` folder you can specify which models for each LLM you want to prompt. Separate the name of each model by a comma. Example for the Gemini models:

```
gemini-pro, gemini-1.5-flash, gemini-1.0-pro
```

- Navigate to the root folder and use the `prompt` command with the following parameters to run the code:

```
python main.py prompt input/<excel_file.xlsx> <column_name> <output_file.xlsx>
```

- You can also use the optional argument `--num_rows` to specify the amount of prompts in the dataset you'd like to run. For example, 10:

```
python main.py prompt input/<excel_file.xlsx> <column_name> <output_file.xlsx> --num_rows 10
```

### Ollama models

The Ollama LLM script in `prompt_ollama.ipynb` has to be run from Google Colab. Upload the Excel file containing the prompts to the notebook on Colab and execute all the codecells.

## Response classification

- The command `str_classify` will call a function that classifies a response from an LLM as a 'full refusal' or 'full compliance' in regards to answering the prompt. Use it with the following parameters:

```
python main.py str_classify input/<excel_file.xlsx> <column_name> <output_file.xlsx>
```

- This command also accepts the optional `--num_rows` argument:

```
python main.py str_classify input/<excel_file.xlsx> <column_name> <output_file.xlsx> --num_rows 10
```