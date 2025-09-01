"""
Here we import Flask and two of its features.
We also import the emotion_detector method from its respective file.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# This line gives the app its name.
# Emotion Detection in this case.

app = Flask("Emotion Detection")

'''
Determining the app's route
'''
@app.route("/emotionDetector")


def emotion_detector_function():

    '''
    Get text entered by user.

    Response is then shown after emotion is detected in text.

    Return specific response if no dominant emotion is found.

    Return entered text with emotion-based statistics and dominant
    emotion if the text is valid.
    '''

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

# This decides what the app's route is.
@app.route("/")

def render_index_page():
    '''
    This function renders the template of the app
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
