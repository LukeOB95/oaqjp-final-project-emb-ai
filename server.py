''' Importing Flask, two of its features and EmotionDetection content
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

''' 
Naming the Flask App
'''
app = Flask("Emotion Detection")

@app.route("/emotionDetector")

def emotion_detector_function():

    # Text to analyze
    text_to_analyse = request.args.get("textToAnalyze")

    # Response
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again."

    else:
        response_text = f"For the given statement, the system response is 'anger': \
                    {response['anger']}, 'disgust': {response['disgust']}, \
                    'fear': {response['fear']}, 'joy': {response['joy']}, \
                    'sadness': {response['sadness']}. The dominant emotion is \
                    {response['dominant_emotion']}."

    return response_text

'''Deciding what the app's route is
'''
@app.route("/")
def render_index_page():
    return render_template("index.html")

''' Running the app on port 5000
'''
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)