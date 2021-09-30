# CRSAS - Customer Review Sentiment Analysis System
## Inspiration/Problem Statment 🎯
After the purchase or use of a product, a survey form comes up. The survey form often did not include the options that we preferred to highlight our intent. They were often filled with discrete data points which did not convey what we wanted to say. 
## What it does 🔍
Our product takes in the customer's audio review and analyses it producing different outputs as classified by the NLP model. It also stores the transcript and the results produced in a database to be used for further analysis.
## How we built it 🔨
It was built using **SciKit-learn** library for machine learning classification. The API was built using **FastAPI**. The database is hosted on **MongoDB** with **GCP** server. The front end was built using **Streamlit**. **Google Speech to Text API** was used for conversion of audio file to transcript.
## Challenges we ran into 📉
Lack of hardware to use it in a live environment. Lack of time to deploy API on the cloud.
## Accomplishments that we're proud of 💹
Building a consumer analytics product using a combination of machine learning and development tools 
## What we learned 📖
Learnt building front-end using Streamlit and backend server using FastAPI with access to MongoDB database.
## What's next for CRSAS ⏭️
1. Using a transformer model for better classification
2. Deploying it as an easy to use API
3. Use of transcript data for keyword extraction
4. Customer trust analytics
5. Product viability index
