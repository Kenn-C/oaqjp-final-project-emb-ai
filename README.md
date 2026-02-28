# EmotionDetection App

A Python web application that detects emotions in text using the Watson NLP EmotionPredict library, deployed via Flask.

---

## Project Structure

```
EmotionDetectionApp/
├── EmotionDetection/
│   ├── __init__.py               # Package initializer
│   └── emotion_detection.py      # Core emotion detection logic
├── templates/
│   └── index.html                # Front-end interface
├── test_emotion_detection.py     # Unit tests
├── server.py                     # Flask web server
└── README.md
```

---

## Features

- Detects five emotions from free-form text: **anger**, **disgust**, **fear**, **joy**, and **sadness**
- Returns confidence scores for each emotion along with the **dominant emotion**
- Handles blank input and invalid requests gracefully (HTTP 400)
- RESTful API endpoint deployable via Flask
- Fully unit-tested with `unittest` and `unittest.mock`
- Passes pylint static analysis with a perfect **10.00/10** score

---

## Requirements

- Python 3.8+
- Flask
- Requests
- Watson NLP Runtime (EmotionPredict model running locally on port 5000)

Install dependencies:

```bash
pip install flask requests
```

---

## Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/EmotionDetectionApp.git
cd EmotionDetectionApp
```

### 2. Start the Watson NLP runtime

Ensure the Watson NLP container is running locally and accessible at:

```
http://localhost:5000/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict
```

### 3. Run the Flask server

```bash
python3 server.py
```

The app will be available at `http://127.0.0.1:5001`.

### 4. Analyze text

Open your browser or use `curl` to send a request:

```
http://127.0.0.1:5001/emotionDetector?textToAnalyze=I am so happy today
```

**Example response:**

```
For the given statement, the system response is 'anger': 0.0217, 'disgust': 0.0524,
'fear': 0.0352, 'joy': 0.8847 and 'sadness': 0.036. The dominant emotion is joy.
```

**Blank input response:**

```
Invalid text! Please try again.
```

---

## Running Unit Tests

```bash
python3 -m unittest test_emotion_detection -v
```

The test suite covers all five dominant emotion cases, blank input handling, and HTTP 400 error handling — 7 tests total.

---

## Static Code Analysis

```bash
pylint server.py
```

Expected output:

```
Your code has been rated at 10.00/10
```

---

## API Reference

### `GET /emotionDetector`

| Parameter       | Type   | Description                  |
|----------------|--------|------------------------------|
| `textToAnalyze` | string | The text to analyze for emotion |

**Returns:** A plain-text string describing the emotion scores and dominant emotion, or an error message if the input is blank.

---

## Module Reference

### `emotion_detector(text_to_analyze)`

Analyzes the emotional content of the provided text.

**Parameters:**
- `text_to_analyze` (str) — The input text to analyze.

**Returns:** A dictionary with the following keys:

```python
{
    'anger':            float | None,
    'disgust':          float | None,
    'fear':             float | None,
    'joy':              float | None,
    'sadness':          float | None,
    'dominant_emotion': str | None
}
```

Returns `None` for all values if the input is blank or the API returns a 400 status code.

---

## License

This project was created as part of the IBM Developer Skills Network — AI Application Development with Watson NLP course.
