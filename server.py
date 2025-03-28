from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"Hello": "World"}

   @app.post("/ask-ai/")
   def ask_ai(question: str):
       return {"answer": f"AI says: {question}"}
   
