# 🌍 AI Multi-Agent Travel Planner

An intelligent travel planning application built using **CrewAI**, **NVIDIA LLMs**, and **Streamlit**. The system employs multiple AI agents that collaborate to recommend destinations, research cities, generate itineraries, and estimate travel budgets based on user preferences.

---

## ✨ Features

### 🏙️ City Selection Agent

Analyzes user preferences such as:

* Travel type
* Interests
* Preferred season

and recommends the most suitable destinations with explanations.

---

### 📍 Local Expert Agent

Provides detailed information about selected destinations:

* Tourist attractions
* Local cuisine
* Cultural experiences
* Accommodation suggestions
* Travel logistics

---

### 🗓️ Travel Planner Agent

Generates a complete travel itinerary including:

* Day-wise schedule
* Activity planning
* Transportation recommendations
* Dining suggestions
* Time allocation for activities

---

### 💰 Budget Manager Agent

Creates a detailed budget breakdown covering:

* Accommodation costs
* Transportation expenses
* Food and dining
* Activities and attractions
* Cost-saving recommendations

---

## 🏗️ System Architecture

```text
User Input
     │
     ▼
City Selection Agent
     │
     ▼
Local Expert Agent
     │
     ▼
Travel Planner Agent
     │
     ▼
Budget Manager Agent
     │
     ▼
Final Travel Report
```

---

## 🤖 Agents Used

### 1. City Selection Expert

**Goal:** Identify the best cities based on user preferences.

### 2. Local Travel Expert

**Goal:** Provide destination-specific insights and recommendations.

### 3. Travel Planning Expert

**Goal:** Generate optimized travel itineraries.

### 4. Budget Management Expert

**Goal:** Estimate costs and suggest budget-friendly alternatives.

---

## 🛠️ Tech Stack

### Backend

* Python
* CrewAI
* NVIDIA AI Endpoints
* LangChain

### Frontend

* Streamlit

### AI Models

* Qwen 3.5 122B (via NVIDIA NIM)

### Environment Management

* python-dotenv

---

## 📂 Project Structure

```text
project/
│
├── main.py
├── trip_plan_agent.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
API_KEY=your_nvidia_api_key
```

---

## 🚀 Running the Application

Start the Streamlit application:

```bash
streamlit run main.py
```

Open:

```text
http://localhost:8501
```

---

## 📝 Example Input

```json
{
  "travel_type": "Adventure",
  "interests": "Nature, Food, Photography",
  "season": "Winter",
  "duration": 7,
  "budget": "Medium"
}
```

---

## 📊 Example Output

### Recommended Cities

* Kyoto, Japan
* Queenstown, New Zealand
* Interlaken, Switzerland

### City Research

* Attractions
* Local cuisine
* Cultural highlights
* Accommodation suggestions

### Travel Itinerary

Detailed day-by-day plan with activities and timings.

### Budget Plan

Comprehensive cost breakdown with saving opportunities.

---

## 🎯 Future Improvements

* Real-time flight search integration
* Hotel booking recommendations
* Interactive maps
* Weather forecasting
* Currency conversion
* Dynamic city research based on selected destinations
* Agent memory and personalization
* Multi-city route optimization

---

## 👨‍💻 Author

**Naman Jain**

* B.Tech Graduate
* Indian Institute of Technology Jodhpur (IIT-Jodhpur)

Interested in:

* Artificial Intelligence
* Agentic AI Systems
* Machine Learning
* Deep Learning

---

## 📜 License

This project is intended for educational and research purposes.
