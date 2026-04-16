from django.shortcuts import render
import pickle
import os

# Load model and vectorizer
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = pickle.load(open(os.path.join(BASE_DIR, 'ml_model', 'model.pkl'), 'rb'))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, 'ml_model', 'vectorizer.pkl'), 'rb'))

def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        # Get news text from form
        news_text = request.POST.get('news_text', '')
        
        # Clean and vectorize
        transformed = vectorizer.transform([news_text])
        
        # Predict
        prediction = model.predict(transformed)[0]
        
        # Result
        if prediction == 0:
            result = "FAKE News"
            color = "red"
        else:
            result = "REAL News"
            color = "green"
            
        return render(request, 'result.html', {
            'result': result,
            'color': color,
            'news_text': news_text
        })
    return render(request, 'index.html')
