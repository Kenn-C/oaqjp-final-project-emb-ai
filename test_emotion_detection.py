"""Unit tests for the emotion_detection module."""
import unittest
from unittest.mock import patch, MagicMock
import json
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit tests for emotion_detector function."""

    def _mock_response(self, emotion_scores):
        """Helper to build a mock Watson NLP response."""
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.text = json.dumps({
            "emotionPredictions": [
                {"emotion": emotion_scores}
            ]
        })
        return mock_resp

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy_for_happy_text(self, mock_post):
        """I am glad this happened → dominant emotion should be joy."""
        mock_post.return_value = self._mock_response({
            "anger": 0.0217, "disgust": 0.0524,
            "fear": 0.0352, "joy": 0.8847, "sadness": 0.0360
        })
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger_for_angry_text(self, mock_post):
        """I am really mad about this → dominant emotion should be anger."""
        mock_post.return_value = self._mock_response({
            "anger": 0.8011, "disgust": 0.0531,
            "fear": 0.0414, "joy": 0.0145, "sadness": 0.0261
        })
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust_for_disgusting_text(self, mock_post):
        """I feel disgusted just thinking about it → dominant = disgust."""
        mock_post.return_value = self._mock_response({
            "anger": 0.0764, "disgust": 0.7606,
            "fear": 0.0452, "joy": 0.0176, "sadness": 0.0812
        })
        result = emotion_detector("I feel disgusted just thinking about it")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness_for_sad_text(self, mock_post):
        """I am so sad about this → dominant emotion should be sadness."""
        mock_post.return_value = self._mock_response({
            "anger": 0.0361, "disgust": 0.0329,
            "fear": 0.0611, "joy": 0.0132, "sadness": 0.8325
        })
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear_for_fearful_text(self, mock_post):
        """I am really afraid that this will happen → dominant = fear."""
        mock_post.return_value = self._mock_response({
            "anger": 0.0603, "disgust": 0.0174,
            "fear": 0.7795, "joy": 0.0148, "sadness": 0.1056
        })
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input_returns_none(self):
        """Blank input should return None for all fields."""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_status_400_returns_none(self, mock_post):
        """HTTP 400 response should return None for all fields."""
        mock_resp = MagicMock()
        mock_resp.status_code = 400
        mock_post.return_value = mock_resp
        result = emotion_detector("some text")
        self.assertIsNone(result['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()
