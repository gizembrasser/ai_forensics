import os
import pandas as pd
import re


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


def clean_ai_dataset(file, filter_column, filter, column_to_clean='answer'):
    df = pd.read_excel(file)

    df_filtered = df[df[filter_column].str.contains(filter, case=False, na=False)]
    df_filtered = df_filtered[df_filtered['macrocategory'] != 'unlabelled']

    # Clean the specified column
    df_filtered[column_to_clean] = df_filtered[column_to_clean].str.replace("Hello, this is Bing.", "", regex=False)\
                                                                .str.replace('<br>', ' ', regex=False)\
                                                                .apply(remove_emojis)\
                                                                .str.replace(r'\s*\[.*?\]', '', regex=True)\
                                                                .str.replace('\n', ' ', regex=True)\
                                                                .str.replace('*', '', regex=False)\
                                                                .str.replace('#', '', regex=False)\
                                                                .str.replace('  +', ' ', regex=True)\
                                                                .str.replace('"', "'", regex=False)\
                                                                .str.strip()                                                            

    # Save the cleaned DataFrame to the output file
    filename = input("Enter the name for the cleaned Excel file (without extension): ") + ".xlsx"

    cleaned_file = os.path.join(os.path.dirname(__file__), f'../../output/cleaned/{filename}') 
    df_filtered.to_excel(cleaned_file, index=False)


training_file = os.path.join(os.path.dirname(__file__), '../../input/training/Microsof-Copilot-Answers_in-Swiss-Bavarian-Hess-Elections.xlsx')
output_file = os.path.join(os.path.dirname(__file__), '../../output/US_responses.xlsx')

# clean_ai_dataset(training_file, "language", "en")
