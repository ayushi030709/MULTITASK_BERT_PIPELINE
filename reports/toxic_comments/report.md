# Dataset Profiling Report

**Dataset:** `toxic_comments`

## Dataset Information

### train

- Rows: **159571**
- Columns: **8**
- Column Names: id, comment_text, toxic, severe_toxic, obscene, threat, insult, identity_hate

### test

- Rows: **306328**
- Columns: **8**
- Column Names: id, comment_text, toxic, severe_toxic, obscene, threat, insult, identity_hate

---

## Text Statistics

### train

- text_column: **comment_text**
- samples: **159571**
- avg_characters: **394.07**
- median_characters: **205.0**
- min_characters: **6**
- max_characters: **5000**
- 95_percentile: **1355.0**
- 99_percentile: **3444.0**
- avg_words: **67.27**
- min_words: **1**
- max_words: **1411**

### test

- text_column: **comment_text**
- samples: **306328**
- avg_characters: **364.88**
- median_characters: **180.0**
- min_characters: **1**
- max_characters: **5000**
- 95_percentile: **1273.8500000000058**
- 99_percentile: **3542.3699999999953**
- avg_words: **61.61**
- min_words: **0**
- max_words: **2321**

---

## Missing Values

### train

- id: 0
- comment_text: 0
- toxic: 0
- severe_toxic: 0
- obscene: 0
- threat: 0
- insult: 0
- identity_hate: 0

### test

- id: 0
- comment_text: 153164
- toxic: 153164
- severe_toxic: 153164
- obscene: 153164
- threat: 153164
- insult: 153164
- identity_hate: 153164

---

## Duplicate Rows

- **train** : 0
- **test** : 0

---

## Label Distribution

### train

- toxic: 15294
- severe_toxic: 1595
- obscene: 8449
- threat: 478
- insult: 7877
- identity_hate: 1405

### test

No label information found.

---

## Random Examples

### train

#### Example 1

- **id** : 7ca72b5b9c688e9e
- **comment_text** : Geez, are you forgetful!  We've already discussed why Marx  was  not an anarchist, i.e. he wanted to use a State to mold his 'socialist man.'  Ergo, he is a statist - the opposite of an  anarchist.  I know a guy who says that, when he gets old and his teeth fall out, he'll quit eating meat.  Would you call him a vegetarian?
- **toxic** : 0
- **severe_toxic** : 0
- **obscene** : 0
- **threat** : 0
- **insult** : 0
- **identity_hate** : 0

#### Example 2

- **id** : c03f72fd8f8bf54f
- **comment_text** : Carioca RFA 

Thanks for your support on my request for adminship.

The final outcome was (31/4/1), so I am now an administrator. If you have any comments or concerns on my actions as an administrator, please let me know. Thank you!
- **toxic** : 0
- **severe_toxic** : 0
- **obscene** : 0
- **threat** : 0
- **insult** : 0
- **identity_hate** : 0

#### Example 3

- **id** : 9e5b8e8fc1ff2e84
- **comment_text** : "

 Birthday 

No worries, It's what I do ;)Enjoy ur day|talk|e "
- **toxic** : 0
- **severe_toxic** : 0
- **obscene** : 0
- **threat** : 0
- **insult** : 0
- **identity_hate** : 0

#### Example 4

- **id** : 5332799e706665a6
- **comment_text** : Pseudoscience category? 

I'm assuming that this article is in the pseudoscience category because of its association with creationism.  However, there are modern, scientifically-accepted variants of catastrophism that have nothing to do with creationism — and they're even mentioned in the article!  I think the connection to pseudoscience needs to be clarified, or the article made more general and less creationism-specific and the category tag removed entirely.
- **toxic** : 0
- **severe_toxic** : 0
- **obscene** : 0
- **threat** : 0
- **insult** : 0
- **identity_hate** : 0

#### Example 5

- **id** : dfa7d8f0b4366680
- **comment_text** : (and if such phrase exists, it would be provided by search engine even if mentioned page is not available as a whole)
- **toxic** : 0
- **severe_toxic** : 0
- **obscene** : 0
- **threat** : 0
- **insult** : 0
- **identity_hate** : 0

### test

#### Example 1

- **id** : 95f65d7eea0209d5
- **comment_text** : None
- **toxic** : -1.0
- **severe_toxic** : -1.0
- **obscene** : -1.0
- **threat** : -1.0
- **insult** : -1.0
- **identity_hate** : -1.0

#### Example 2

- **id** : 04d160111b6bde25
- **comment_text** : None
- **toxic** : -1.0
- **severe_toxic** : -1.0
- **obscene** : -1.0
- **threat** : -1.0
- **insult** : -1.0
- **identity_hate** : -1.0

#### Example 3

- **id** : 54ac59b90cae4f26
- **comment_text** : None
- **toxic** : -1.0
- **severe_toxic** : -1.0
- **obscene** : -1.0
- **threat** : -1.0
- **insult** : -1.0
- **identity_hate** : -1.0

#### Example 4

- **id** : e0d35babf2b9e82d
- **comment_text** : None
- **toxic** : 0.0
- **severe_toxic** : 0.0
- **obscene** : 0.0
- **threat** : 0.0
- **insult** : 0.0
- **identity_hate** : 0.0

#### Example 5

- **id** : fd9ac8fbe658ac91
- **comment_text** : None
- **toxic** : -1.0
- **severe_toxic** : -1.0
- **obscene** : -1.0
- **threat** : -1.0
- **insult** : -1.0
- **identity_hate** : -1.0

