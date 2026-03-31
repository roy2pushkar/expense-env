---
title: Expense Env
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# Expense Env

FastAPI-based expense tracking app deployed using Hugging Face Spaces.
🧠 OpenEnv Project: Smart Expense Manager
📌 Project Overview
This project simulates a real-world Expense Management System where an AI agent learns how to manage money efficiently.
________________________________________
🎯 Objective
Build an environment where: - Agent receives income - Performs actions (spend/save/invest) - Tries to maximize savings
________________________________________
🧱 Project Structure
expense-env/
│
├── app.py
├── environment.py
├── tasks.py
├── inference.py
├── openenv.yaml
├── requirements.txt
├── Dockerfile
└── README.md
________________________________________
⚙️ Installation Guide
1. Install Python
python --version
Use Python 3.10+
2. Install dependencies
pip install -r requirements.txt
3. Install OpenEnv
pip install openenv-core
________________________________________
📦 requirements.txt
fastapi
uvicorn
openenv-core
requests
🚀 Run Project Locally
Start server
uvicorn app:app --reload
Run inference
python inference.py
________________________________________
🌐 Deploy to Hugging Face
1.	Create new Space
2.	Upload all files
3.	Add HF_TOKEN in secrets
4.	Select Docker runtime
________________________________________
📘 README.md
Description
Smart Expense Manager environment for AI training.
Actions
•	spend
•	save
•	invest
State
•	balance
•	savings
•	step
Tasks
•	Easy: save 300
•	Medium: save 700
•	Hard: save 1200
________________________________________
✅ Checklist
☒	3 tasks
☒	reward system
☒	API endpoints
☒	inference script
☒	Dockerfile
☒	openenv.yaml
________________________________________
🎉 Done!
