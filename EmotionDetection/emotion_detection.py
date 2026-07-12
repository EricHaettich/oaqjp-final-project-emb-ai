import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = myobj, headers=header) 
    
    formatted_response = json.loads(response.text)
    
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    
    max_score = 0
    dominant_emotion = None
    for key, value in emotion_scores.items():
        score = float(value)
        if score > max_score:
            dominant_emotion = key 
            max_score = score
    
    emotion_scores['dominant_emotion'] = dominant_emotion;
    return emotion_scores