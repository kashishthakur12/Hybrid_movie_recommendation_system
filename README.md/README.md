# 🎬 Smart Hybrid Netflix Recommender

An AI-powered Hybrid Movie Recommendation System built using Flask, Machine Learning, Content-Based Filtering, Popularity Prediction, and TMDB API integration.

---

## 🚀 Features

### Movie Recommendations
- Content-based movie recommendation system
- Hybrid recommendation approach
- Top similar movie suggestions

### TMDB Integration
- Fetches movie posters dynamically
- Displays searched movie poster
- Displays recommended movie posters

### Popularity Prediction
- Predicts movie popularity using Machine Learning
- Trained using TMDB movie dataset

### Web Interface
- Netflix-inspired UI
- Responsive design
- Easy movie search

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-Learn
- TMDB API
- HTML
- CSS

---

## 📂 Project Structure

```text
smart_hybrid_netflix_recommender/
│
├── App/
│   └── app.py
│
├── Src/
│   ├── hybrid.py
│   ├── predictor.py
│   └── tmdb.py
│
├── Models/
│   ├── similarity.pkl
│   └── popularity_model.pkl
│
├── Templates/
│   ├── index.html
│   └── predict.html
│
├── Static/
│   ├── style.css
│   └── logo.png
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/smart-hybrid-netflix-recommender.git
```

### Navigate to Project

```bash
cd smart-hybrid-netflix-recommender
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 TMDB API Setup

Create TMDB account:

https://www.themoviedb.org/

Generate API Key and update:

```python
API_KEY = "YOUR_API_KEY"
```

inside:

```text
Src/tmdb.py
```

---

## ▶️ Run Application

```bash
python App/app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📸 Screenshots

Add screenshots here after deployment.

---

## 👨‍💻 Author

Kashish Thakur

B.Tech CSE (AI & ML)
