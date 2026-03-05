# AI Interaction Programs in Python

This project contains two Python programs that demonstrate basic **Artificial Intelligence concepts**: a **Turing Test simulation** and a **CAPTCHA verification system**.

---

# Programs Included

## 1. Turing Test Simulation

### Description

This program simulates a **Turing Test**, where a user chats with an anonymous entity and later decides whether the entity is a **human or a machine**.
The entity is implemented as a simple **rule-based chatbot (ELIZA-style)** that responds using pattern matching.

### Features

* Rule-based chatbot responses
* Pattern matching using regular expressions
* Random response selection
* Simulated typing delay

### Libraries Used

* `random`
* `re`
* `time`

### Run the Program

```bash
python turing_test.py
```

---

## 2. CAPTCHA Verification System

### Description

This program generates an **image-based CAPTCHA** to verify whether the user is human.
The user must correctly type the characters shown in the image within **three attempts**.

### Features

* Random CAPTCHA generation
* Image-based verification
* Automatic image display
* Limited attempts for security

### Libraries Used

* `random`
* `string`
* `time`
* `captcha`
* `Pillow (PIL)`

### Installation

Install required libraries:

```bash
pip install captcha pillow
```

### Run the Program

```bash
python captcha_test.py
```

---

# Purpose

These programs demonstrate:

* **Human vs Machine interaction (Turing Test)**
* **Bot prevention techniques (CAPTCHA)**
* Basic **Python programming and AI concepts**.
