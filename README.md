# League Analytics Hub

## Overview
**League Analytics Hub** is a comprehensive analytics platform for competitive League of Legends.  
It improves on Riot’s default global rankings by introducing a balanced algorithm that accounts for **regional depth, player performance, and historical data**, not just international tournament appearances.  

This project provides tools for fans, analysts, and competitors to explore teams, players, metas, and international results across the entire history of League of Legends esports.

---

## Features

### Global Rankings Reimagined
- Custom algorithm that weighs **regional strength and depth** more accurately than Riot’s system.
- Retroactive global and regional rankings from **Season 1 to present**.

### Major Regional League Tracking
- Live standings, playoff brackets, and schedules for:
  - LCK (Korea)  
  - LPL (China)  
  - LEC (Europe)  
  - LCS (North America)  
  - LCP (Pacific)
  - CBLOL (Brazil)

### Player Analytics
- Individual player rankings across multiple seasons.  
- Performance metrics against elite competition.  
- Career trajectory and performance trend analysis.  

### Regional Meta Analysis
- Tier lists for each role in each region.  
- Visualization of meta evolution across patches and seasons.  
- Champion and strategy effectiveness over time.  

### Historical Data
- Tournament results from **Season 1 to present**.  
- Retroactive rankings and match archives.  
- Regional and international comparisons over multiple eras.  

### International Tournament Hub
- Live brackets for MSI, Worlds, and other international events.  
- Match predictions powered by data models.  
- Regional performance breakdowns by meta, patch, and era.  

---

## Technical Stack & Tools Overview

### Programming Languages & Frameworks
- **Python**: Main backend language.  
- **Flask**: Web framework for APIs and server-rendered pages.  
- **JavaScript**: Frontend interactivity and data visualizations.  
- **HTML/CSS**: Website structure and styling.  
- **SQL**: Database queries and data management.  

### Databases & Data Storage
- **SQLite**: Lightweight database for development.  
- **PostgreSQL**: Production-ready, scalable database.  
- **SQLAlchemy**: Python ORM for database operations.  

### Data & Analytics
- **Pandas**: Data cleaning, transformation, and manipulation.  
- **NumPy**: Core mathematical operations.  
- **Scikit-learn**: Machine learning algorithms for predictions.  
- **Matplotlib / Plotly**: Charts and analytics visualizations.  

### APIs & Data Sources
- **Riot Games API**: Official match and player data.  
- **Leaguepedia API**: Tournament structures and historical data.  
- **Web scraping**: Supplemental esports data collection.  

### Deployment & DevOps
- **Docker**: Containerized application packaging.  
- **Railway / Render**: Deployment and hosting.  
- **GitHub Actions**: Automated CI/CD for testing and deployment.  
- **Git / GitHub**: Version control and collaboration.  

### Frontend & Visualization
- **Bootstrap**: Responsive, professional design components.  
- **Chart.js / D3.js**: Interactive visualizations and charts.  
- **React (optional)**: For advanced frontend interactivity.  

---

## Roadmap
- Implement ranking algorithm and historical data processing.  
- Build APIs for regional standings and player analytics.  
- Create visual dashboards for meta and player insights.  
- Add support for predictions and machine learning models.  
- Expand coverage to minor leagues and academy circuits.  

---

## Getting Started
1. Clone the repository:
```bash
git clone https://github.com/yourusername/league-analytics-hub.git
cd league-analytics-hub
```

2. Create virtual environment:
```bash
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Copy example env file
cp backend/config/.env.example backend/config/.env

# Edit .env and add your Riot API key
```

5. Initialize database:
```bash
cd backend
python scripts/init_database.py
```

6. Run the application:
```bash
python run.py
```

Visit: http://localhost:5000
