# Abstract
Short Data Engineering project, to ensure some skills are mastered before moving on to harder tasks

Python is the main language, used with multiple librairies like FastAPI, Spark and Streamlit

The project goal is to generate data, make it available through an API.
Then extract it, transform it  and load it in a webapp that allows to visualize and analyze the data we produced in the first step. 

# Diagram

![schemadubreu.png](schema%2Fschemadubreu.png)

# Guide

First set up a virtual environment :

`python3 -m venv venv/`

Then, install the requirements :

`pip install -r requirements.txt`

If you want to start the API server (assuming you're in sensor_api folder) :

`uvicorn main:app --reload`

If you want to start airflow server (assuming you're in airflow folder) :

`export AIRFLOW_HOME=$(pwd) && airflow standalone`

Connect to localhost:8080, connect with the credentials given by the previous command

![airflow.png](schema%2Fairflow.png)

You should see this DAG, this is the DAG that run extraction and transformation, run it everytime you want, otherwise it will launch itself hourly

If you want to start the streamlit webapp (assuming you're in streamlit_app folder) :

`streamlit run main.py`

# Apache Parquet

Some precisions about Apache Parquet :
- Column-oriented
- Efficiently compressed
- fast OLAP request
- More efficient than CSV, especially to reduce cloud cost

![img.png](schema%2Fimg.png)

# Next steps ?

If I had to enhance this project, I would use a cloud service like AWS for file storage and Spark computations,
add more options and pages in the web app to add more ways to explore the data, improve the API throughput and maximum load

Project idea and tickets by [Benjamin Dubreu](https://www.linkedin.com/in/benjamin-dubreu-data/) - Data Upskilling