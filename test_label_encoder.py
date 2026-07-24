from src.preprocessing.label_encoder import LabelEncoder

encoder = LabelEncoder()

###########################################################
# TweetEval
###########################################################

tweet = {
    "text": "Amazing movie",
    "label": 2
}

print(encoder.encode(tweet))

###########################################################
# GoEmotions
###########################################################

emotion = {
    "text": "I am happy",
    "labels": [2, 5]
}

print(
    encoder.encode(
        emotion,
        num_classes=28
    )
)

###########################################################
# Toxic
###########################################################

toxic = {

    "comment_text": "...",

    "toxic": 1,

    "severe_toxic": 0,

    "obscene": 1,

    "threat": 0,

    "insult": 1,

    "identity_hate": 0,
}

print(
    encoder.encode(toxic)
)