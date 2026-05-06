# Urban Routes Selenium Test Automation

End-to-end UI test automation framework built using **Python, Selenium WebDriver, and PyTest** to validate core user flows in the Urban Routes web application.

---

## 📌 Overview

This project automates key ride-booking workflows, including route setup, phone verification, payment method configuration, and order placement.

The framework is designed using the **Page Object Model (POM)** to ensure scalability, maintainability, and clean separation of concerns.

---

## 🛠️ Tech Stack

- Python
- Selenium WebDriver
- PyTest
- ChromeDriver
- Chrome DevTools (performance logs)

---

## 🧱 Framework Design

The project follows the **Page Object Model (POM)** pattern:

- **tests/** → Test cases
- **pages/** → UI interactions & locators
- **utils/** → Helper utilities
- **data/** → Test data/constants

This structure improves:
- Code reusability
- Maintainability
- Readability

---

## 📂 Project Structure

```bash
urban-routes-selenium-tests/
│
├── tests/
│   └── test_urban_routes.py
├── pages/
│   └── urban_routes_page.py
├── utils/
│   └── helpers.py
├── data/
│   └── test_data.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Test Coverage

Automated scenarios include:

- Setting pickup and destination locations
- Selecting ride plan
- Phone number verification (with SMS code retrieval)
- Adding payment method (card)
- Adding driver comment
- Selecting additional options (blanket & handkerchiefs)
- Adding items (ice cream quantity)
- End-to-end taxi order flow validation

---

## 🔍 Key Implementation

### Dynamic SMS Code Retrieval

The framework retrieves the verification code dynamically using browser performance logs:

- Captures network traffic via Chrome DevTools Protocol
- Extracts SMS code from API response
- Eliminates need for hardcoded test data

---

## ▶️ How to Run Tests

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/urban-routes-selenium-tests.git
cd urban-routes-selenium-tests
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run tests

```bash
pytest
```

---

## ⚠️ Notes

- The test server URL is temporary and may expire
- Update the URL in `data/test_data.py` before running tests

---

## 🔮 Future Improvements

- Add PyTest fixtures
- Implement base page class
- Add test reporting (HTML reports)
- Integrate CI/CD (GitHub Actions)
- Add cross-browser testing

---

## 👤 Author

**Allan Almario**  
LinkedIn: https://linkedin.com/in/your-linkedin  
GitHub: https://github.com/yourusername
