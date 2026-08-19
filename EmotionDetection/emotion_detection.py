import json

def emotion_detector(text_to_analyze):
    """Local mock implementation of Watson NLP Emotion Detector."""
    
    # Handle blank or empty input (Task 7)
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    text = text_to_analyze.lower()

    # Simple mock logic based on keywords
    if "happy" in text or "glad" in text or "love" in text or "hello" in text:
        emotions = {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.95, 'sadness': 0.02}
    elif "angry" in text or "furious" in text:
        emotions = {'anger': 0.92, 'disgust': 0.03, 'fear': 0.02, 'joy': 0.01, 'sadness': 0.02}
    elif "sad" in text or "upset" in text:
        emotions = {'anger': 0.02, 'disgust': 0.01, 'fear': 0.02, 'joy': 0.01, 'sadness': 0.94}
    else:
        emotions = {'anger': 0.05, 'disgust': 0.05, 'fear': 0.05, 'joy': 0.80, 'sadness': 0.05}

    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion

    return emotions