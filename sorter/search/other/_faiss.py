import os
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

try:
    embeddings_path = os.path.dirname(os.path.abspath("embeddings_data"))+"\\search\\other\\documents\\embeddings_data"
    text_data_path = os.path.dirname(os.path.abspath("text_data"))+"\\search\\other\\documents\\text_data"
    faiss_path = os.path.dirname(os.path.abspath("text_data"))+"\\search\\other\\models\\model.faiss"
    models_path = os.path.dirname(os.path.abspath("model.faiss"))+"\\search\\other\\models\\msmarco-distilbert-base-tas-b-fine-tunned-az-10"
    embeddings_data = pd.read_csv(embeddings_path)
except:
    embeddings_path = "documents\\embeddings_data"
    text_data_path = "documents\\text_data"
    faiss_path = "models\\model.faiss"
    models_path = "models\\msmarco-distilbert-base-tas-b-fine-tunned-az-10"


embeddings_data = pd.read_csv(embeddings_path)
text_data = pd.read_csv(text_data_path)
faiss_model = faiss.read_index(faiss_path)

transformer = SentenceTransformer(models_path)

threshold = 0.8

def sorted_data(request:str) -> dict:
    request = pd.DataFrame([transformer.encode(request)])
    vec, index = faiss_model.search(request, len(embeddings_data))
    _embeddings_data = embeddings_data.reindex(index[0]).reset_index(drop=True)
    _text_data_ = text_data.reindex(index[0]).reset_index(drop=True)

    similarity_list = []

    for index, value in enumerate(_embeddings_data.values):
        similarity = cosine_similarity(request.values[0].reshape(1, -1), value.reshape(1, -1))[0, 0]
        similarity_list.append(similarity)

    _text_data_["similarity"] = similarity_list
    _text_data_ = _text_data_.sort_values(["similarity"]).reset_index(drop=True).iloc[::-1].reset_index(drop=True)
    _text_data_ = _text_data_[_text_data_["similarity"] > threshold]

    result = _text_data_.groupby('document').apply(lambda x: dict(zip(x['article'], x['text']))).to_dict()

    return result

# print(sorted_data("Uşağa ad verin"))