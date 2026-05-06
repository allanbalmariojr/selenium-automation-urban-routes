# 🚕 Urban Routes UI Automation Framework (Sprint 8)

This project is an automated UI testing framework for the Urban Routes web application using **Selenium WebDriver, Python, and PyTest**.

Sprint 8 focuses on converting previous procedural tests into a **Page Object Model (POM) structure**, improving scalability, maintainability, and overall test organization.

---

## 🎯 Project Objective

The goal of this sprint was to:

- Refactor existing Selenium tests into a **Page Object Model (POM) architecture**
- Implement proper **setup and teardown methods using PyTest class fixtures**
- Improve maintainability by separating test logic from page interactions
- Ensure complete end-to-end user flow coverage for the taxi ordering application

---

## 🧠 Key Features Implemented

### 🏗️ Page Object Model (POM)

- Created `pages.py` to store all locators and page methods
- Encapsulated all UI interactions inside the `UrbanRoutesPage` class
- Improved reusability and reduced duplication across test cases

---

### 🧪 End-to-End Test Coverage

Automated full user workflows including:

- Route setup (From / To address input)
- Taxi plan selection
- Phone number authentication with SMS verification
- Payment method setup (credit card entry and confirmation)
- Driver comment input
- Additional service options (blankets, handkerchiefs, ice cream ordering)
- Final taxi order placement and confirmation validation

---

### 🕒 Synchronization Handling

- Used `WebDriverWait` and `expected_conditions`
- Improved test stability and reduced flakiness
- Ensured proper element visibility and clickability before actions

---

## 📁 Project Structure

```text
selenium-automation-urban-routes/
│
├── data/
│   └── data.py
│
├── pages/
│   └── urban_routes_page.py
│
├── utils/
│   └── helpers.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ How to Run Tests

These instructions are universal and work in any environment with Python installed (VS Code, PyCharm, Mac, Windows, Linux, or CI pipelines).

---

### 1. Clone the repository

git clone https://github.com/allanbalmariojr/selenium-automation-urban-routes.git

cd selenium-automation-urban-routes

---

### 2. (Optional) Create a virtual environment

python -m venv venv

---

### 3. Activate it:

Windows (PowerShell):
venv\Scripts\activate

Mac / Linux:
source venv/bin/activate

---

### 4. Install dependencies

pip install selenium pytest

---

### 5. Run all tests

pytest

---

### 6. Run a specific test file (optional)

pytest main.py

---

## 🧪 Test Scenarios Covered
- Route creation and validation
- Taxi plan selection
- Phone number verification (SMS flow)
- Credit card payment setup
- Driver message input
- Extra service selection (blankets, handkerchiefs, ice cream)
- Complete taxi order flow

---

## 📌 Key Takeaways (Sprint 8 Focus)
- Transitioned from procedural test scripts to POM-based framework
- Improved separation of concerns between tests and page logic
- Introduced proper test lifecycle management (setup/teardown)
- Strengthened full end-to-end UI automation coverage

---

## 🧠 Tech Stack
- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)

---

