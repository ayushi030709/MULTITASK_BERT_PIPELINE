from src.preprocessing.tokenizer import TextTokenizer

tokenizer = TextTokenizer()

text = "I love learning Natural Language Processing!"

print("=" * 60)

print("Tokens")
print(tokenizer.tokenize(text))

print("=" * 60)

encoded = tokenizer.encode(text)

print("Input IDs")
print(encoded["input_ids"])

print("=" * 60)

print("Attention Mask")
print(encoded["attention_mask"])

print("=" * 60)

if "token_type_ids" in encoded:
    print("Token Type IDs")
    print(encoded["token_type_ids"])

print("=" * 60)

print("Decoded")
print(tokenizer.decode(encoded["input_ids"][0]))

print("=" * 60)

print("Vocabulary Size")
print(tokenizer.vocab_size)

print("=" * 60)

print("Special Tokens")
print(tokenizer.special_tokens)

print("=" * 60)

tokenizer.info()