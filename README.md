# 🏎️ F1 Tire Strategy AI Agent

An intelligent Formula 1 tire strategy recommendation system built with Streamlit that helps optimize tire choices based on race conditions, weather, and track parameters.

## 🏁 Features

- **Real-time Tire Recommendations**: Get optimal tire compound suggestions based on current race conditions
- **Weather-Aware Strategy**: Intelligent handling of dry, wet, and intermediate weather conditions
- **Temperature Optimization**: Considers track temperature for tire performance optimization
- **Stint Analysis**: Factors in current tire age and degradation patterns
- **Interactive Web Interface**: User-friendly Streamlit dashboard with visual feedback
- **Historical Data Integration**: Uses race data patterns for informed decision-making
- **Strategy Reasoning**: Explains the logic behind each recommendation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/f1-tire-strategy-ai.git
cd f1-tire-strategy-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 📁 Project Structure

```
f1-tire-strategy-ai/
├── app.py                      # Main Streamlit application
├── tire_agent.py              # ML-based tire recommendation engine
├── tire_agent_simple.py       # Rule-based alternative (no ML dependencies)
├── app_simple.py              # Streamlit app for rule-based version
├── tire_strategy_data.csv     # Historical tire strategy dataset
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🎯 How It Works

### Input Parameters
- **Current Lap**: Race progress (1-70 laps)
- **Track Temperature**: Track surface temperature (10-60°C)
- **Weather Condition**: Dry, Light Rain, Moderate Rain, Heavy Rain
- **Current Tire Compound**: Soft, Medium, Hard, Intermediate, Wet, Full Wet
- **Stint Length**: Number of laps on current tires

### Tire Compounds Guide
- 🔴 **Soft**: Fastest lap times, shortest lifespan (3-15 laps)
- 🟡 **Medium**: Balanced performance and durability (10-25 laps)
- ⚪ **Hard**: Longest lasting, slower lap times (20-40 laps)
- 🟢 **Intermediate**: Optimal for light wet conditions
- 🔵 **Wet**: Best for moderate rain
- 🟣 **Full Wet**: Heavy rain specialist

### Algorithm Approaches

**ML Version (`tire_agent.py`)**:
- Uses scikit-learn Decision Tree Classifier
- Trained on historical tire strategy data
- Handles categorical encoding for weather and tire types
- Provides data-driven predictions

**Rule-Based Version (`tire_agent_simple.py`)**:
- Logic-based decision making
- Weather-priority recommendations
- Tire degradation considerations
- Race phase strategy optimization
- No external ML dependencies

## 📊 Sample Data

The system includes sample tire strategy data covering various race scenarios:
- Different weather conditions
- Various track temperatures
- Multiple tire compound transitions
- Different race phases and stint lengths

## 🛠️ Configuration

### Adding New Data
To improve recommendations, add more historical data to `tire_strategy_data.csv`:

```csv
lap,track_temp,weather,current_tire,stint_laps,next_tire
25,35,Dry,Soft,12,Medium
```

### Customizing Rules
Modify the rule-based logic in `tire_agent_simple.py` to adjust:
- Temperature thresholds
- Stint length considerations
- Weather-based priorities
- Race phase strategies

## 🔮 Future Improvements

### Short-term Enhancements
- [ ] **Fuel Load Integration**: Factor in car weight and fuel consumption
- [ ] **Driver Preference Profiles**: Customize recommendations based on driver style
- [ ] **Circuit-Specific Optimization**: Track-dependent tire strategies
- [ ] **Real-time Weather API**: Live weather data integration
- [ ] **Pit Window Calculator**: Optimal pit stop timing recommendations
- [ ] **Competitor Analysis**: Consider other drivers' strategies

### Medium-term Features
- [ ] **Advanced ML Models**: 
  - Random Forest or Gradient Boosting
  - Neural networks for complex pattern recognition
  - Ensemble methods combining multiple algorithms
- [ ] **Historical Race Simulation**: 
  - What-if scenario analysis
  - Strategy outcome predictions
  - Alternative strategy comparisons
- [ ] **Performance Metrics Dashboard**:
  - Lap time predictions
  - Tire degradation curves
  - Strategy success rates
- [ ] **Multi-stint Strategy Planning**:
  - Full race strategy optimization
  - Pit stop sequence planning
  - Risk assessment for different strategies

### Long-term Vision
- [ ] **Real-time Race Integration**:
  - Live telemetry data processing
  - Dynamic strategy updates during race
  - Integration with F1 timing systems
- [ ] **Advanced Analytics**:
  - Predictive modeling for tire performance
  - Weather impact quantification
  - Track evolution modeling
- [ ] **Team Strategy Tools**:
  - Multi-driver coordination
  - Team-wide strategy optimization
  - Communication integration
- [ ] **Machine Learning Enhancements**:
  - Reinforcement learning for strategy optimization
  - Deep learning for complex pattern recognition
  - Transfer learning from other racing series

### Technical Improvements
- [ ] **Performance Optimization**:
  - Model caching and optimization
  - Faster inference times
  - Memory usage optimization
- [ ] **API Development**:
  - RESTful API for external integrations
  - WebSocket support for real-time updates
  - Mobile app backend support
- [ ] **Data Management**:
  - Database integration for larger datasets
  - Automated data collection pipelines
  - Data quality validation and cleaning
- [ ] **Testing & Reliability**:
  - Comprehensive unit testing
  - Integration testing
  - Performance benchmarking
  - Continuous integration/deployment

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Add your changes**: Focus on one feature at a time
4. **Write tests**: Ensure your code is well-tested
5. **Commit changes**: `git commit -m 'Add amazing feature'`
6. **Push to branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**: Describe your changes clearly

### Contribution Ideas
- Add more historical tire strategy data
- Implement new ML algorithms
- Improve the user interface
- Add unit tests
- Create data visualization features
- Optimize performance
- Add new weather condition handling

## 📈 Performance Metrics

Current system performance:
- **Response Time**: < 100ms for recommendations
- **Accuracy**: Based on rule-based logic and historical patterns
- **Coverage**: Handles all major F1 tire compounds and weather conditions
- **Reliability**: Graceful error handling and fallback mechanisms

## 🐛 Known Issues

- Limited historical data may affect ML model accuracy
- Temperature ranges could be expanded for extreme conditions
- Wet weather transitions need more sophisticated handling

## 📄 License

This project is licensed under the MIT License 

## 🙏 Acknowledgments

- Formula 1 for providing inspiration and tire compound specifications
- Streamlit team for the excellent web framework
- scikit-learn contributors for machine learning tools
- F1 racing community for strategy insights



**Made with ❤️ for F1 racing enthusiasts and strategy nerds!**

"Winning is like a drug...I can't settle for second or third in no circumstances whatsoever" - Ayrton Senna
