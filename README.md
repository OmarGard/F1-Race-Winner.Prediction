# F1 Race Winner Prediction

🏁 A machine learning project that predicts Formula 1 Grand Prix winners based on historical race data and current season performance.

## 📋 Project Overview

This project aims to develop a predictive model that analyzes Formula 1 race results from the current season to forecast the winner of upcoming Grand Prix races. By leveraging historical performance data, driver statistics, and race conditions, the model provides data-driven predictions for F1 enthusiasts and analysts.

## 🎯 Objectives

- **Primary Goal**: Predict the winner of the next F1 Grand Prix based on season-to-date results
- **Secondary Goals**:
  - Analyze driver performance trends throughout the season
  - Identify key factors that contribute to race victories
  - Provide probability distributions for race outcomes
  - Enable comparative analysis between drivers and teams

## 🚀 Features

- **Data Collection**: Automated gathering of F1 race results and statistics
- **Feature Engineering**: Creation of meaningful predictors from raw race data
- **Model Training**: Implementation of various machine learning algorithms
- **Prediction Engine**: Real-time winner prediction for upcoming races
- **Performance Analysis**: Model accuracy evaluation and continuous improvement
- **Visualization**: Interactive charts and graphs for data insights

## 📊 Data Sources

The model utilizes various data points including:
- Race results and finishing positions
- Qualifying times and grid positions
- Driver championship standings
- Constructor (team) performance
- Circuit characteristics and historical data
- Weather conditions and track conditions
- Driver experience and recent form

## 🛠️ Technology Stack

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms
- **Matplotlib/Seaborn**: Data visualization
- **Jupyter Notebooks**: Interactive development and analysis

## 📁 Project Structure

```
F1-Race-Winner.Prediction/
├── data/                   # Raw and processed datasets
│   ├── raw/               # Original race data
│   └── processed/         # Cleaned and feature-engineered data
├── notebooks/             # Jupyter notebooks for analysis
│   ├── data_exploration.ipynb
│   ├── feature_engineering.ipynb
│   └── model_training.ipynb
├── src/                   # Source code
│   ├── data_collection.py # Data gathering scripts
│   ├── preprocessing.py   # Data cleaning and preparation
│   ├── feature_engineering.py # Feature creation
│   ├── models.py         # ML model implementations
│   └── prediction.py     # Prediction pipeline
├── models/               # Trained model files
├── visualizations/       # Generated charts and graphs
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🚦 Getting Started

### Prerequisites

- Python 3.12.5 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/OmarGard/F1-Race-Winner.Prediction.git
cd F1-Race-Winner.Prediction
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Quick Start

1. **Data Collection**: Run the data collection script to gather the latest F1 results
2. **Data Preprocessing**: Clean and prepare the data for model training
3. **Model Training**: Train the prediction model on historical data
4. **Make Predictions**: Generate predictions for upcoming races

## 📈 Model Performance

The model's performance is evaluated using various metrics:
- **Accuracy**: Percentage of correct winner predictions
- **Top-3 Accuracy**: Percentage of races where the actual winner is in the top 3 predictions
- **Precision/Recall**: For individual driver predictions
- **Log-loss**: Probability-based evaluation metric

## 🔮 Usage Examples

```python
from src.prediction import F1Predictor

# Initialize the predictor
predictor = F1Predictor()

# Load the trained model
predictor.load_model('models/f1_winner_model.pkl')

# Predict next race winner
prediction = predictor.predict_race_winner(
    circuit='Monaco',
    season=2025,
    race_number=6
)

print(f"Predicted winner: {prediction['driver']}")
print(f"Confidence: {prediction['probability']:.2%}")
```

## 📋 Roadmap

- [X] Data collection and preprocessing pipeline
- [X] Exploratory data analysis
- [ ] Feature engineering and selection
- [ ] Baseline model implementation
- [ ] Advanced model development
- [ ] Model evaluation and validation
- [ ] Web interface for predictions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Omar Gard - [@OmarGard](https://github.com/OmarGard)

Project Link: [https://github.com/OmarGard/F1-Race-Winner.Prediction](https://github.com/OmarGard/F1-Race-Winner.Prediction)

## 🙏 Acknowledgments

- Formula 1 for providing race data and statistics
- The F1 community for inspiration and feedback
- Open source libraries that make this project possible

---

*Note: This project is for educational and research purposes. Predictions are based on historical data and should not be used for gambling or betting purposes.*
