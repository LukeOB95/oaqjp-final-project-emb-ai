from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector", methods=['GET', 'POST'])
def give_results():

    # Text to analyze
    text_to_analyse = request.args.get("textToAnalyze")

    # Response
    response = emotion_detector(text_to_analyse)

    # Emotions
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Details - For the return statement
    details = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        'dominant_emotion': dominant_emotion
    }

    if request.method == 'GET':
        return f"For the given statement, the system response is 'anger': {details['anger']}, 'disgust': {details['disgust']}, 'fear': {details['fear']}, 'joy': {details['joy']}, 'sadness': {details['sadness']}. The most dominant emotion is {details['dominant_emotion']}."

    elif request.method == 'GET' and text_to_analyse is None:
        return f"Cannot analyze"
    
    if not dominant_emotion:
        return {"error message": "Blank input"}, 400

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)