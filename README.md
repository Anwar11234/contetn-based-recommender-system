# Content-Based Course Recommendation System

The Content-Based Course Recommendation System helps users on online learning platforms discover courses that match their interests and educational needs. This system, based on course content rather than user interactions, is designed to provide relevant recommendations even for new or rarely used courses. Below is an overview of the system's components, from data sources and feature selection to deployment.

## Table of Contents
1. [Introduction](#introduction)
2. [Data Sources](#data-sources)
3. [Feature Selection](#feature-selection)
4. [Text Vectorization with TF-IDF](#text-vectorization-with-tf-idf)
5. [Calculating Similarity with Cosine Similarity](#calculating-similarity-with-cosine-similarity)
6. [Building the Recommendation System](#building-the-recommendation-system)
7. [Deployment](#deployment)
    - [FastAPI Implementation](#fastapi-implementation)
    - [Containerization with Docker](#containerization-with-docker)
    - [Hosting on Hugging Face Spaces](#hosting-on-hugging-face-spaces)

## Introduction

In online learning platforms, recommendation systems enhance user experience by suggesting courses tailored to learners’ interests and educational goals. This project implements a **Content-Based Recommendation System** that uses course information to recommend similar courses, making it suitable for situations where user interaction data may be sparse or unavailable.

## Data Sources

The recommendation system is built using data from three tables:
- **Courses Table**: Contains information such as course ID, title, subject, and learning objectives.
- **Subjects Table**: Holds subject IDs and names.
- **Instructors Table**: Includes instructor names, IDs, and areas of expertise.
  ![image](https://github.com/user-attachments/assets/0ac95d4d-cdc5-4883-8e6c-42e1166b717e)


## Feature Selection

To ensure accurate recommendations, several features are extracted from the data:
- **Course Title**
- **Course Learning Objectives**
- **Course Language**
- **Course Level**
- **Course Subject**
- **Instructor Name**
- **Instructor Expertise**

These features provide a rich representation of each course, facilitating the identification of similar courses.

## Text Vectorization with TF-IDF

The **Term Frequency-Inverse Document Frequency (TF-IDF)** method is used to transform textual data into numerical vectors for similarity calculation. The TF-IDF score for a word `t` in a document `d` is calculated as:

\[
\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)
\]

- **Term Frequency (TF)**: Measures how frequently a word appears in a document.
- **Inverse Document Frequency (IDF)**: Measures the importance of a word across all documents.

## Calculating Similarity with Cosine Similarity

To determine the similarity between courses, **Cosine Similarity** is used, measuring the cosine of the angle between two vectors. The formula for cosine similarity between two vectors `A` and `B` is:

\[
\text{Cosine Similarity}(A, B) = \frac{A \cdot B}{\|A\|\|B\|}
\]

A value of `1` indicates identical courses, while a value of `0` suggests no similarity.

## Building the Recommendation System

The recommendation system consists of the following steps:
1. Load data from the tables.
2. Preprocess and select relevant features.
3. Vectorize text data using TF-IDF.
4. Compute the cosine similarity matrix.
5. Retrieve and return the top 10 similar courses for a given course.

## Deployment

The recommendation system is deployed as an API using **FastAPI** and containerized with **Docker** for platform-independent consistency. It is then hosted on **Hugging Face Spaces** to provide an accessible interface.

### FastAPI Implementation

**FastAPI** was chosen for its simplicity, high performance, and automatic documentation generation. Steps to implement FastAPI include:
1. **Setup**: Install FastAPI and Uvicorn.
2. **Define the API**: Create endpoints for recommendation functionality.
3. **Integrate Recommendation Logic**: Embed the recommendation function within the API endpoint.
4. **Run the API**: Use Uvicorn to launch the FastAPI application.

### Containerization with Docker

To ensure a consistent environment across different platforms, the API is containerized using **Docker**:
1. **Dockerfile**: Define the image.
2. **Build the Image**: Build the Docker image from the Dockerfile.
3. **Run the Container**: Start a container from the built image.

### Hosting on Hugging Face Spaces

The containerized API is hosted on **Hugging Face Spaces** for public accessibility:
1. **Create a Space**: Set up a new Space on Hugging Face.
2. **Configure Space**: Select Docker as the environment.
3. **Upload Docker Image**: Push the Docker image to the Hugging Face Space.
4. **Run the Space**: Start the Space to make the API accessible online.

---

By using TF-IDF vectorization, cosine similarity, and a robust deployment pipeline, this content-based recommendation system efficiently suggests relevant courses to learners, enhancing their online learning experience.
