from src.preprocessing.text_cleaner import TextCleaner

cleaner = TextCleaner(remove_emojis=True)

text = """
I LOVE this movie!!!!! 😍😍😍

Visit https://openai.com

<div>Hello</div>
"""

print(cleaner.clean(text))