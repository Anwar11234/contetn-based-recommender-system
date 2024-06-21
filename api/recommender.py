from fastapi import FastAPI, Body
import pickle

with open('preprocessed_data.pkl', 'rb') as f:
    tfidf_matrix, cosine_sim_tfidf, df, indices = pickle.load(f)

app = FastAPI()

@app.post("/recommendations")
def recommend(course_data: dict = Body(...)):
  idx = indices.get(course_data["title"])

  # Handle cases where the course title is not found
  if idx is None:
      return {"message": "Course not found."}

  # Get the pairwise similarity scores of all courses with that course
  sim_scores = list(enumerate(cosine_sim_tfidf[idx]))

  # Sort the courses based on the similarity scores
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

  # Get the scores of the 10 most similar courses
  sim_scores = sim_scores[1:11]

  # Get the course indices
  course_indices = [i[0] for i in sim_scores]

  # Return the top 10 most similar courses
  return list(df['Title'].iloc[course_indices].values)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("recommender:app", host="0.0.0.0", port=3000)