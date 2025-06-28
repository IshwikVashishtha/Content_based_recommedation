# 🎬 Movie Recommendation System

A sophisticated content-based movie recommendation system built with Python, featuring a modern Streamlit web interface and powered by machine learning algorithms.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This Movie Recommendation System uses content-based filtering to suggest movies based on user preferences. The system analyzes movie features including genres, cast, crew, keywords, and plot descriptions to find similar movies. It provides an intuitive web interface where users can select a movie and receive personalized recommendations with movie posters.

## ✨ Features

- **Content-Based Filtering**: Recommends movies based on content similarity
- **Interactive Web Interface**: Modern Streamlit-based UI with movie posters
- **Real-time Movie Data**: Integrates with TMDB API for up-to-date movie information
- **Smart Text Processing**: Uses NLTK for text preprocessing and stemming
- **Cosine Similarity**: Implements advanced similarity algorithms
- **Responsive Design**: Displays recommendations in a clean, grid layout
- **Movie Posters**: Fetches and displays movie posters for better user experience

## 🛠️ Technologies Used

- **Python 3.13.5**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning algorithms
- **NLTK** - Natural language processing
- **Pickle** - Model serialization
- **Requests** - HTTP library for API calls
- **TMDB API** - Movie database integration

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd movie_recommendation_system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   ```bash
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

4. **Install required packages**
   ```bash
   pip install streamlit pandas scikit-learn nltk requests
   ```

5. **Download NLTK data**
   ```python
   python -c "import nltk; nltk.download('punkt')"
   ```

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:8501`
   - The application will open automatically

3. **Get recommendations**
   - Select a movie from the dropdown menu
   - Click the "Recommend" button
   - View personalized movie recommendations with posters

## 🔬 How It Works

### Data Processing Pipeline

1. **Data Collection**: Uses TMDB 5000 movies and credits datasets
2. **Feature Extraction**: Extracts genres, cast, crew, keywords, and overview
3. **Text Preprocessing**: 
   - Converts text to lowercase
   - Applies Porter Stemming
   - Removes stop words
4. **Vectorization**: Uses CountVectorizer to create feature vectors
5. **Similarity Calculation**: Implements cosine similarity algorithm
6. **Recommendation Generation**: Returns top 30 similar movies

### Algorithm Details

The system uses **Content-Based Filtering** with the following steps:

1. **Feature Engineering**: Combines movie overview, genres, cast, crew, and keywords
2. **Text Processing**: Applies stemming and normalization
3. **Vectorization**: Converts text to numerical vectors using TF-IDF
4. **Similarity Computation**: Calculates cosine similarity between movies
5. **Ranking**: Sorts movies by similarity scores

## 📁 Project Structure

```
movie_recommendation_system/
├── app.py                 # Streamlit web application
├── model.ipynb           # Jupyter notebook for model development
├── movies.csv            # Processed movie dataset
├── similarity.pkl        # Pre-computed similarity matrix
├── tmdb_5000_movies.csv  # Raw movie data
├── tmdb_5000_credits.csv # Raw credits data
└── README.md            # Project documentation
```

## 🔌 API Integration

The system integrates with **The Movie Database (TMDB) API** to:
- Fetch movie posters
- Get real-time movie information
- Ensure data accuracy and completeness

### API Configuration

The application uses a public TMDB API key for demonstration purposes. For production use, consider:
- Using your own API key
- Implementing rate limiting
- Adding error handling for API failures

## 🎨 Features in Detail

### Content-Based Filtering
- Analyzes movie content rather than user behavior
- Considers multiple features: plot, genre, cast, crew, keywords
- Provides personalized recommendations based on movie characteristics

### Text Processing
- **Stemming**: Reduces words to their root form (e.g., "running" → "run")
- **Stop Word Removal**: Eliminates common words that don't add meaning
- **Case Normalization**: Converts all text to lowercase for consistency

### Similarity Algorithm
- **Cosine Similarity**: Measures the cosine of the angle between two vectors
- **High Performance**: Pre-computed similarity matrix for fast recommendations
- **Scalable**: Can handle large datasets efficiently

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add comments to complex code sections
- Update documentation for new features
- Test your changes thoroughly

## 📊 Performance

- **Dataset Size**: 5000+ movies
- **Feature Vector Size**: 5000 dimensions
- **Recommendation Speed**: < 1 second
- **Accuracy**: High similarity scores for related movies

## 🔮 Future Enhancements

- [ ] Collaborative filtering implementation
- [ ] User rating system
- [ ] Advanced filtering options (year, rating, language)
- [ ] Movie trailer integration
- [ ] User authentication and profiles
- [ ] Recommendation explanations
- [ ] Mobile-responsive design improvements

## 🙏 Acknowledgments

- **TMDB** for providing the movie dataset and API
- **Streamlit** for the excellent web framework
- **Scikit-learn** for machine learning tools
- **NLTK** for natural language processing capabilities

## 📞 Contact

For questions, suggestions, or collaboration opportunities, please open an issue on GitHub or contact the project maintainers.

---

**Made with ❤️ for movie enthusiasts everywhere!** 