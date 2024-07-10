1. Put your Excel file containing prompts in the `input` folder. Remember the name of the column containing your prompts.

2. In the textfiles in the `input` folder you can specify which models for each LLM you want to prompt. Separate the name of each model by a comma. Example for the Gemini models:

```
gemini-pro, gemini-1.5-flash, gemini-1.0-pro
```

3. Navigate to the root folder and use the following command to run the code:

```
python main.py input/<excel_file.xlsx> <column_name>
```

4. You can also use the optional argument `--num_rows` to specify the amount of prompts in the dataset you'd like to run. For example, 10:

```
python main.py input/<excel_file.xlsx> <column_name> --num_rows 10
```