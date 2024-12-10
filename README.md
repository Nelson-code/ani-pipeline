# Anirudh-pipeline 
![image](https://github.com/user-attachments/assets/474db393-552e-4e2b-9a12-2f564d4897d2)

# Project Overview  
Built an End-to-End pipeline using Apache Airflow that involves extracting the top ten track data of Anirudh Ravichander from Spotify API, transforming it into a Pandas DataFrame, and storing it in the specified directory.  

# Tech Stack  
1. Apache Airflow  
2. Ubuntu  
3. Python Pandas and other libraries  

# Apache Airflow  
Open-source tool and framework for running data pipelines in production. It allows data practitioners to design pipelines as code.  

# Features of Airflow Framework  
1. **Task** - Operations in the pipeline  
2. **Dependencies** - Relationship between tasks  
3. **DAG** - Directed Acyclic Graph (DAG), a combination of both tasks and dependencies. It has no directed cycles, meaning that following the direction of edges will never result in a loop.  

**Example**:  
In a simple ETL process, each step, such as Extract (E), Transform (T), and Load (L), can be considered a task, and the relationship between them can be termed as dependencies. A DAG is a container that holds both tasks and dependencies.


![image](https://github.com/user-attachments/assets/145db1cd-ca8d-491d-8ef4-3134275ef608)

# Steps  
## Extract  
1. Create a Spotify Developer account by creating an app.  
2. Copy the `client_id` and `client_secret`.  
3. To get the access token, make a POST call to this endpoint: [https://accounts.spotify.com/api/token](https://accounts.spotify.com/api/token) with `client_id` and `client_secret`.  
4. After getting the `client_id` and `client_secret`, make a GET request to this endpoint: [https://api.spotify.com/v1/artists/4zCH9qm4R2DADamUHMCa6O/top-tracks?market=IN](https://api.spotify.com/v1/artists/4zCH9qm4R2DADamUHMCa6O/top-tracks?market=IN) to retrieve the top ten tracks.  
5. Validate the status code of the request and return the JSON data.  

## Transform  
1. Using a for loop, retrieve only the keys such as "name" and "popularity".  
2. Convert the data into a Pandas DataFrame.  
3. Sort the DataFrame in descending order based on the popularity score of each song.  

## Load  
1. Create a directory using the `makedirs()` method of the `os` library.  
2. As the DAG is scheduled to run every 5 minutes, append the current timestamp to the filename to resolve conflicts between files.  
3. Convert the Pandas DataFrame into a CSV file.  
4. Load the CSV file into the specified directory.  

Refer for more details:
🎬 https://www.youtube.com/watch?v=vc-8pWW8KqI&ab_channel=DataEngineering
📖 https://www.datacamp.com/tutorial/getting-started-with-apache-airflow
📂 https://github.com/sbgowtham/airflow_python_etl_project

