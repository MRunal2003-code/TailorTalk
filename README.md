# Titanic Dataset Chatbot

This project is a **Titanic Dataset Chatbot** built using **FastAPI** for the backend and **Streamlit** for the frontend. The chatbot answers user queries about the Titanic dataset and provides visualizations for certain questions. It allows users to interact with the Titanic dataset in a conversational manner.

---

## Features

- Provides statistical information about the Titanic dataset (e.g., average ticket fare, percentage of male passengers).
- Generates visualizations, such as histograms of passenger ages.
- Accepts natural language questions and provides concise responses.
- User-friendly web interface built using Streamlit.

---

## Prerequisites

1. Python 3.8 or above installed on your system.
2. Basic understanding of Python and terminal/command prompt usage.

---

## Installation and Setup

Follow these steps to run the program locally:

### 1. Clone the Repository

```bash
https://github.com/MRunal2003-code/TailorTalk.git
cd TailorTalk
```

### 2. Create a Virtual Environment

```bash
python -m venv env
```

Activate the environment:
- **Windows:**
  ```bash
  .\env\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source env/bin/activate
  ```

### 3. Install Dependencies

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

### 4. Add the Titanic Dataset

Ensure the Titanic dataset CSV file (e.g., `Titanic-Dataset.csv`) is in the project directory.

---

## Running the Program

### 1. Start the Backend (FastAPI)

Run the FastAPI backend server:

```bash
uvicorn main:app --reload --port 8501
```

### 2. Start the Frontend (Streamlit)

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## How to Use

1. Open your browser and go to the Streamlit app (usually at `http://localhost:8502` unless specified otherwise).
2. Enter your question about the Titanic dataset in the input box (e.g., "What was the average ticket fare?").
3. Click the **Submit** button to see the answer.
4. If the question generates a visualization (e.g., histogram), the image will also be displayed below the answer.
   ![image](https://github.com/user-attachments/assets/7b71363c-f57f-45aa-b60e-1be2be3cba65)

---

## Example Questions

- "What percentage of passengers were male?"
- "Show the histogram of passenger ages."
- "What was the average ticket fare?"
- "How many passengers embarked from each port?"
![image](https://github.com/user-attachments/assets/82c3fb20-bfa1-4d3d-af9d-0508c6161d6e)
![image](https://github.com/user-attachments/assets/ecefa3ec-78fc-4844-8b0c-46249e1b96b9)

---

## Future Improvements

- Adding support for more datasets.
- Enhancing natural language understanding capabilities.
- Deploying the app on a cloud platform for public access.

---

## Contributions

Feel free to fork this repository, make improvements, and create pull requests. Your contributions are welcome!

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For any queries or suggestions, please contact:
- **Name:** Mrunal RK
- **Email:** mrunalrk2002@gmail.com
- **GitHub:** [https://github.com/MRunal2003-code](https://github.com/MRunal2003-code)

Happy coding! 🚀

