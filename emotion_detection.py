import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests. post(url, json= myobj, headers= header )
    data = json.loads(response.text)

    # Extract emotions and their scores
    emotions = data['emotionPredictions'][0]['emotion']

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # add it to the dictionary
    emotions['dominant_emotion'] = dominant_emotion

    return emotions

