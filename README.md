Short Data Engineering project, to ensure some skills are mastered before moving on to harder tasks

Python is the main language, used with multiple librairies like FastAPI, Spark and Streamlit

The project goal is to generate data, make it available through an API.
Then extract it, transform it  and load it in a webapp that allows to visualize and analyze the data we produced in the first step. 

![schemadubreu.png](schema%2Fschemadubreu.png)

Project global diagram

Some precisions about Apache Parquet :
- Column-oriented
- Efficiently compressed
- fast OLAP request
- More efficient than CSV, especially to reduce cloud cost

![img.png](schema%2Fimg.png)

If I had to enhance this project, I would use a cloud service like AWS for file storage and Spark computations,
add more options and pages in the web app to add more ways to explore the data, improve the API throughput and maximum load 