from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    anger = emotions['anger']
    disgust = emotions['disgust']
    sadness = emotions['sadness']
    joy = emotions['joy']
    fear = emotions['fear']
    dominant_emotion = emotions['dominant_emotion']
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger,disgust,fear,joy,sadness,dominant_emotion)

