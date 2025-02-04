"""
Flask server for Emotion Detection API
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Render the index.html page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_api():
    """API endpoint to analyze emotions from text."""
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    # Format response as per requirements
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )
    return response_text

# Run the app on localhost:5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
