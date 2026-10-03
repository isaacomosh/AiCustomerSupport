The project entails
AI Customer Support Agent integrated into an e-commerce application. The system combines an online store with a RAG-based AI assistant that helps customers 
   1.find products, 
   2.get product information, and make inquiries about orders, payments, delivery,    3. store policies
<img width="1536" height="1024" alt="5b300cdc-fca1-46e4-92a6-7aa8d94cfc29" src="https://github.com/user-attachments/assets/4b211d6e-a888-43e8-bb3f-c25cf8bb589a" />
#How the Retrieval Sytem works 
  first convert the pdf into chunks 

  make vector embeddings stored in vetor database such as chroma db
  Embedding -text that is converted into a list of numbers representing its meaning
    For example :
          "Delivery within Nairobi takes 1 to 2 business days."
          becomes::::====>
          [
    0.21,
    -0.45,
    0.73,
    0.12,
    ...
]

#creatind an embedding function
from google import genai
client=genai.Client(api_key="Place ur API key here")
def embed(texts):
   response=client.models.embed_content(
         model="gemini-embedding-001",
         contents=texts)


   return [item.values for item in response.embeddings]
  then:
       documents = [
    "Customers can return products within 14 days of purchase.",
    "Delivery within Nairobi takes 1 to 2 business days.",
    "Delivery outside Nairobi takes 3 to 5 business days.",
    "Customers can pay using M-Pesa or credit card.",
    "Custom suits take approximately 7 business days to complete."
]

vectors = embed(documents)

print(vectors[0])

#STORING THE EMBEDDING IN DATABASE
database=[]
for document, vector in zip(documents,vectors):
database.append({"text":document,"embedding":vector})
     The database looks like this:
     [
    {
        "text": "Customers can return products...",
        "embedding": [...]
    },

    {
        "text": "Delivery within Nairobi...",
        "embedding": [...]
    },

    {
        "text": "Delivery outside Nairobi...",
        "embedding": [...]
    }
   ]


