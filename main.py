from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; for production, specify your Streamlit URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


app = FastAPI()

# Load the Titanic dataset
df = pd.read_csv('C:\\Users\\mruna\\Music\\tailor talk\\Titanic-Dataset.csv')

class Query(BaseModel):
    question: str

@app.post("/query/")
async def answer_query(query: Query):
    question = query.question.lower()
    
    if "percentage of passengers were male" in question:
        percentage_male = df['Sex'].value_counts(normalize=True)['male'] * 100
        return {"answer": f"{percentage_male:.2f}%"}

    elif "histogram of passenger ages" in question:
        plt.figure(figsize=(10, 6))
        sns.histplot(df['Age'].dropna(), bins=30, kde=True)
        plt.title('Histogram of Passenger Ages')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.tight_layout()
        
        # Save the plot to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        img_str = base64.b64encode(buf.read()).decode('utf-8')
        return {"image": f"data:image/png;base64,{img_str}"}

    elif "average ticket fare" in question:
        average_fare = df['Fare'].mean()
        return {"answer": f"The average ticket fare was ${average_fare:.2f}."}

    elif "passengers embarked from each port" in question:
        embarked_counts = df['Embarked'].value_counts()
        return {"answer": embarked_counts.to_dict()}

    else:
        return {"answer": "I'm sorry, I can't answer that question."}
