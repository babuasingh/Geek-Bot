GEEK BOT:
## Short DESCRIPTION:
I have Used technologies like 


. NLTK (Natural Language Toolkit) for tasks such as tokenization, stemming and bag of words. 

. PyTorch for machine learning and  deep learning applications. In the context of my AI - chatbot, PyTorch was likely used to develop and train the neural network model responsible for understanding user queries, predicting appropriate responses, and responding accordingly.

. Linear algebra concepts and techniques for understanding the mathematical principles underlying neural networks , backpropagation and deep learning.

. Flask to create a web server that serves as the interface for users to interact with the chatbot. Flask handles routing HTTP requests from clients to the appropriate functions in the Python code, allowing the chatbot to receive user input, process it, and return the corresponding responses.

. HTML, CSS, and JavaScript : for front-end purpouse .


## Initial Setup:

Clone repo and create a virtual environment
```
git clone 'https://github.com/babuasingh/Geek-Bot.git'
cd Geek-Bot
python -m venv venv(for windows)   |   python3 -m venv venv(for macOS)
. venv\Scripts\activate(for windows)  | . venv/bin/activate(for macOS)
```
Install dependencies
```
(venv) pip install Flask torch torchvision nltk flask_cors
```
Install nltk package
```
(venv) python
>>> import nltk
>>> nltk.download('punkt')
>>> quit()
```


This will dump data.pth file. And then run
the following command to test it in the console.
```
(venv) python train.py
```
Run
```
(venv) python app.py
```


