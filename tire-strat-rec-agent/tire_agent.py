import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import os

# Initialize label encoders globally
le_weather = LabelEncoder()
le_current_tire = LabelEncoder()
le_next_tire = LabelEncoder()

# Define all possible values to ensure consistent encoding
weather_categories = ['Dry', 'Light Rain', 'Moderate Rain', 'Heavy Rain']
tire_categories = ['Soft', 'Medium', 'Hard', 'Intermediate', 'Wet', 'Full Wet']


def load_and_train_model():
    """Load data and train the model"""
    global model, le_weather, le_current_tire, le_next_tire
    
    # Check if CSV file exists
    if not os.path.exists('tire_strategy_data.csv'):
        raise FileNotFoundError("tire_strategy_data.csv not found. Please ensure the file is in the same directory.")
    
    # Load data
    df = pd.read_csv('tire_strategy_data.csv')
    
    # Validate required columns
    required_columns = ['lap', 'track_temp', 'weather', 'current_tire', 'stint_laps', 'next_tire']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Fit label encoders with all possible categories to avoid unseen label errors
    le_weather.fit(weather_categories)
    le_current_tire.fit(tire_categories)
    le_next_tire.fit(tire_categories)
    
    # Encode the data
    df['weather_enc'] = le_weather.transform(df['weather'])
    df['current_tire_enc'] = le_current_tire.transform(df['current_tire'])
    df['next_tire_enc'] = le_next_tire.transform(df['next_tire'])
    
    # Prepare features and target
    features = df[['lap', 'track_temp', 'weather_enc', 'current_tire_enc', 'stint_laps']]
    target = df['next_tire_enc']
    
    # Train the model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(features, target)
    
    return model

def recommend_tire(lap, temp, weather, current_tire, stint_laps):
    """Recommend tire based on input parameters"""
    try:
        # Validate inputs
        if weather not in weather_categories:
            return f"Error: Invalid weather condition '{weather}'. Must be one of: {weather_categories}"
        
        if current_tire not in tire_categories:
            return f"Error: Invalid tire compound '{current_tire}'. Must be one of: {tire_categories}"
        
        # Create input dataframe
        input_data = pd.DataFrame([[
            lap,
            temp,
            le_weather.transform([weather])[0],
            le_current_tire.transform([current_tire])[0],
            stint_laps
        ]], columns=['lap', 'track_temp', 'weather_enc', 'current_tire_enc', 'stint_laps'])
        
        # Make prediction
        pred_enc = model.predict(input_data)[0]
        recommended_tire = le_next_tire.inverse_transform([pred_enc])[0]
        
        return recommended_tire
        
    except Exception as e:
        return f"Error making recommendation: {str(e)}"


# Load and train the model when the module is imported
try:
    model = load_and_train_model()
    print("Model trained successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None