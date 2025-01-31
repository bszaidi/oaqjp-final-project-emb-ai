import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        emotions = emotion_detector('I am glad this happened')
        self.assertEqual(emotions['dominant_emotion'], 'joy')

        emotions = emotion_detector('I am really mad about this')
        self.assertEqual(emotions['dominant_emotion'], 'anger')

        emotions = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(emotions['dominant_emotion'], 'disgust')

        emotions = emotion_detector('I am so sad about this')
        self.assertEqual(emotions['dominant_emotion'], 'sadness')

        emotions = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(emotions['dominant_emotion'], 'fear')
