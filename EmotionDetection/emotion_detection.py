import requests
import json

def emotion_detector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json={"raw_document": {"text": text}}, headers=headers)
    
    if response.status_code == 200:
        return json.dumps(response.json(), indent=4)  # تنسيق الإخراج ليكون واضحًا
    return json.dumps({"error": "Failed to fetch emotions"}, indent=4)

def emotion_predictor(detected_text):
    if not detected_text or all(value is None for value in detected_text.values()):
        return json.dumps(detected_text, indent=4)
    
    emotions = detected_text.get('emotionPredictions', [{}])[0].get('emotion', {})
    if not emotions:
        return json.dumps(detected_text, indent=4)
    
    result = {**emotions, 'dominant_emotion': max(emotions, key=emotions.get)}
    return json.dumps(result, indent=4)
