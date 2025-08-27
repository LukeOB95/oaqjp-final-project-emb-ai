import requests
import json

# Emotion Detector Method
def emotion_detector(text_to_analyse):

    # Attributes
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }

    # Response
    response = requests.post(url, json = input, headers = headers)

    # Formatted Response
    formatted_response = json.loads(response.text)

    # Extraction process
    emotions = {
        'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
        'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
        'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
        'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness'],
    }

    # Score retrieval
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # What is the most dominant emotion?
    dominant_emotion = max(emotions, key = emotions.get)

    # In the case of a successful response (status code of 200)
    if response.status_code == 200:
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }