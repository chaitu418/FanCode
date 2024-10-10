# FanCode User Todo Completion Check

This project automates the verification of todo task completion for users in the city "FanCode".

## Setup and Running

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd FanCode_Automation
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the tests:**
    ```bash
    pytest test_fancode.py
    ```

## Description

The script does the following:
1. Fetches users and todos from JSONPlaceholder API.
2. Identifies users in the "FanCode" city based on latitude and longitude.
3. Checks if each user has completed more than 50% of their todos.
4. Asserts the completion percentage and reports results.
