# Prompting LLM API's

## ChatGPT and Gemini models

1. Put your Excel file containing prompts in the `input` folder. Remember the name of the column containing your prompts.

2. In the textfiles in the `input` folder you can specify which models for each LLM you want to prompt. Separate the name of each model by a comma. Example for the Gemini models:

```
gemini-pro, gemini-1.5-flash, gemini-1.0-pro
```

3. Navigate to the root folder and use the following command to run the code:

```
python main.py input/<excel_file.xlsx> <column_name> <output_file>
```

4. You can also use the optional argument `--num_rows` to specify the amount of prompts in the dataset you'd like to run. For example, 10:

```
python main.py input/<excel_file.xlsx> <column_name> <output_file> --num_rows 10
```

## Llama models

The Ollama LLM script in `prompt_ollama.ipynb` has to be run from Google Colab. Upload the Excel file containing the prompts to the notebook on Colab and execute all the codecells.