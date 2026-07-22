from src.preprocessing.tokenizer import BertTokenizerWrapper

tokenizer = BertTokenizerWrapper(max_length=20)

sentence = "I love machine learning."

print("=" * 60)
print("Original Sentence")
print(sentence)

print("=" * 60)
print("Tokens")
print(tokenizer.tokenize(sentence))

print("=" * 60)
print("Encoded")
encoding = tokenizer.encode(sentence)

print(encoding)

print("=" * 60)
print("Input IDs")
print(encoding["input_ids"])

print("=" * 60)
print("Attention Mask")
print(encoding["attention_mask"])

print("=" * 60)
print("Token Type IDs")
print(encoding["token_type_ids"])

print("=" * 60)
print("Decoded")
print(
    tokenizer.decode(
        encoding["input_ids"][0]
    )
)

print("=" * 60)
print("Vocabulary Size")
print(tokenizer.vocab_size())

print("=" * 60)
print("Special Tokens")
print(tokenizer.special_tokens())