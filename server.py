"""
Server module for the Emotion Detection web application.

This module initializes a Flask application that serves a web interface
for detecting emotions in user-provided text using the Watson NLP
Emotion Predict function.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotion of the text passed as a query parameter.

    Reads the 'textToAnalyze' query parameter from the request URL,
    invokes the emotion detector, and returns the formatted result.
    If the input is blank or invalid, returns an error message.

    Returns:
        str: A formatted string with the emotion scores and the
             dominant emotion, or an error message for invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector
    response = emotion_detector(text_to_analyze)

    # Error handling for blank / invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract the emotion scores and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format the output as requested by the customer
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    