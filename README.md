# Testing moderation on LLM's

This repo consists of two main functionalities: 
1. Running a list of prompts to different models of LLM's (currently ChatGPT, Gemini and Ollama) through their APIs.
2. Classifying which of the prompts the model refused to answer, or complied with, based on string matching.

## Setup

Before running the program, you need to ensure that your environment is set up correctly. Follow these steps:

### 1. Requirements
- Install Python (version 3.8 or higher). You can download it [here](https://www.python.org/downloads/).
- Make sure you have the Terminal application (Mac OS) or Command Prompt (Windows) installed. Basic knowledge of how to use these applications is also required.
- Clone or download this repository to your computer.

### 2. Install Required Libraries
- Open your terminal in the root folder of the repository.
- Run the following command to install the required Python libraries:

```
pip install -r requirements.txt
```

### 3. API Keys
The program uses API keys to interact with OpenAI and Gemini's APIs. Follow these steps to create a `.env` file to securely store your API keys:

- Create a file called `.env` in the root folder of this repository. You can use this command from the terminal:

```
touch .env
```

- Open the `.env` file and add the following lines, replacing <YOUR_API_KEY> with the actual API key you obtained from the respective platforms, in quotation marks:

```
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
```

- Save the file when you're done.

## Automated prompting

### OpenAI and Gemini API's

- Put your Excel file containing prompts in the `input` folder. Remember the name of the column containing your prompts.

- In the textfiles in the `input/models` folder you can specify which models for each LLM you want to prompt. Separate the name of each model by a comma. Example for the Gemini models:

```
gemini-pro, gemini-1.5-flash, gemini-1.0-pro
```

- Navigate to the root folder with your Terminal application and use the `prompt` command with the following parameters to run the code:

```
python main.py prompt input/<excel_file.xlsx> <column_name> <output_file.xlsx>
```

- You can also use the optional argument `--num_rows` to specify the amount of prompts in the dataset you'd like to run. 
- For example, the following command will read 10 rows from the 'Prompts' column in `EU_prompts.xlsx` and write the responses to a new file called `EU_responses.xlsx`:

```
python main.py prompt input/EU_prompts.xlsx Prompts EU_responses.xlsx --num_rows 10
```

### Ollama models (beta)

The Ollama LLM script in `prompt_ollama.ipynb` has to be run from Google Colab. Upload the Excel file containing the prompts to the notebook on Colab and execute all the codecells.

## Response classification (beta)

### Compliance

- The command `str_classify` will call a function that classifies a response from an LLM as a 'full refusal' or 'full compliance' in regards to answering the prompt. Use it with the following parameters:

```
python main.py str_classify input/<excel_file.xlsx> <column_name> <output_file.xlsx>
```

### Keyword search

- The command `keywords` will check if responses contain one or more items from a list of one or more keywords. Use it with the following parameters:

```
python main.py keywords input/<excel_file.xlsx> <column_name> <output_file.xlsx>
```

- All of these commands can be used with the optional `--num_rows` argument.

## In progress

### 1. Sentiment Analysis
- Add functionality to analyze the sentiment (positive, negative, neutral) of each response.

### 2. Topic Modeling
- Implement topic modeling (e.g., using Latent Dirichlet Allocation) to group responses by common themes or topics.
- Include a summary of top keywords for each topic.

*Let me know if you have more ideas :)*