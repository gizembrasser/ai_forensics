import os
import pandas as pd
import re

training_file = os.path.join(os.path.dirname(__file__), '../../input/training/Microsof-Copilot-Answers_in-Swiss-Bavarian-Hess-Elections.xlsx')
output_file = os.path.join(os.path.dirname(__file__), '../../output/US_responses.xlsx')


def clean_gpt_dataset(file, model_filter='gpt', column_to_clean='answer'):
    df = pd.read_excel(file)

    # Filter the DataFrame to keep only rows where 'model' contains the specified string
    df_filtered = df[df['model'].str.contains(model_filter, case=False, na=False)]

    # Clean the specified column
    df_filtered[column_to_clean] = df_filtered[column_to_clean].str.replace('*', '', regex=False)\
                                                                .str.replace('#', '', regex=False)\
                                                                .str.replace('\n', ' ', regex=True)\
                                                                .str.replace('  +', ' ', regex=True)

    # Save the cleaned DataFrame to the output file
    cleaned_file = os.path.join(os.path.dirname(__file__), '../output/cleaned/US_responses_gpt.xlsx')  
    df_filtered.to_excel(cleaned_file, index=False)


def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese characters
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)


def clean_training_dataset(file, language='en', column_to_clean='answer'):
    df = pd.read_excel(file)

    df_filtered = df[df['language'] == language]
    df_filtered = df_filtered[df_filtered['macrocategory'] != 'unlabelled']

    # Clean the specified column
    df_filtered[column_to_clean] = df_filtered[column_to_clean].str.replace("Hello, this is Bing. ", "", regex=False)\
                                                                .str.replace('<br>', ' ', regex=False)\
                                                                .apply(remove_emojis)\
                                                                .str.replace(r'\[.*?\]', '', regex=True)\
                                                                .str.replace('\n', ' ', regex=True)                                                            

    # Save the cleaned DataFrame to the output file
    cleaned_file = os.path.join(os.path.dirname(__file__), '../../output/cleaned/training_data_gpt.xlsx')  
    df_filtered.to_excel(cleaned_file, index=False)


# clean_gpt_dataset(output_file)
# clean_training_dataset(training_file)
