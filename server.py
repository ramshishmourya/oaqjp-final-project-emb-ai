from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_analysis():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    dominant_emotion = emotions['dominant_emotion']
    if dominant_emotion is None :
        return "Invalid text! Please try again!."
    anger = emotions['anger']
    disgust = emotions['disgust']
    sadness = emotions['sadness']
    joy = emotions['joy']
    fear = emotions['fear']
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger,disgust,fear,joy,sadness,dominant_emotion)



if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5001)
