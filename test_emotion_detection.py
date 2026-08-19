import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Unit test class using local mocks for API calls."""

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector(self, mock_post):
        emotions_map = {
            "I am glad this happened": "joy",
            "I am really angry about this": "anger",
            "I feel disgusted just thinking about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid this will happen": "fear"
        }

        for statement, expected_emotion in emotions_map.items():
            mock_post.return_value.status_code = 200
            mock_post.return_value.text = f'''{{
                "emotionPredictions": [{{
                    "emotion": {{
                        "anger": {0.9 if expected_emotion == "anger" else 0.01},
                        "disgust": {0.9 if expected_emotion == "disgust" else 0.01},
                        "fear": {0.9 if expected_emotion == "fear" else 0.01},
                        "joy": {0.9 if expected_emotion == "joy" else 0.01},
                        "sadness": {0.9 if expected_emotion == "sadness" else 0.01}
                    }}
                }}]
            }}'''

            res = emotion_detector(statement)
            self.assertEqual(res["dominant_emotion"], expected_emotion)

if __name__ == "__main__":
    unittest.main()