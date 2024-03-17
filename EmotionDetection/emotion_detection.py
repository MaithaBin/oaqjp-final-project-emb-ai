import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    # handles an error
    if response.status_code == 400:
        result =  {'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
        return result

    # Converts response text into dictionary
    formatted_response = json.loads(response.text)

    # Extracts 5 emotions: anger, disgust, fear, joy, and sadness 
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    # Find the highest score in the emotions and add the result to the dictionary
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion
    return emotion_scores



