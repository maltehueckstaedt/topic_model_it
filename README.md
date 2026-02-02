# hex-informatik-analyse

Das sind die Ideen, die ich für Topic Models gehabt hatte: 
Topic Model 1: Was sind die Informatik-Topics im Studienjahr 2024? Im Studienjahr 2019? Wie unterscheiden sie sich?
Alle Informatikkurse SJ 2024 (filter_model_1a == 1)
alle Informatikkurse SJ 2019 (filter_model_1b == 1)
 
Topic Model 2: Was sind die Informatik-Topics an Unis, wo die Analyse-Sample vollständig ist? Unterscheiden sich diese Unis mit dem gesamt Sample?
Subset Informatikkurse im SJ 2024 für Unis, die für den ganzen Beobachtung-Zeitraum komplett sind (filter_model_2a == 1) **Für TU München, RWTH Aachen wird semesters 2023w & 2024s genutzt, weil sie keine Infos zu 2024w haben und ich sie nicht von den Analysen ausschalten wollte.
Subset Informatikkurse im SJ 2019 für Unis, die für den ganzen Beobachtungs-Zeitraum komplett sind (filter_model_2b== 1)
 
 
Topic Model 3: Was sind die Topics in den Informatik-Sub-Bereiche Wirtschaftsinformatik, Bioinformatik, Medizinische Informatik? (Keine zeitliche Begrenzung)
Informatikkurse in Wirtschaftsinformatik (wirt_info == 1)
Bioinformatik (bio_info == 1)  
Medizinische Informatik (medizin_info == 1)

# Pytorch und RTX5080

## 🚀 Anleitung: PyTorch + BERTopic mit RTX 5080 (CUDA 12.9)

### 1. Neues Conda-Environment anlegen

```bash
conda create -n torch5080 python=3.12
conda activate torch5080
```

### 2. Nightly-Build von PyTorch mit Blackwell-Support installieren

```bash
pip install --pre torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu128
```

### 3. BERTopic + Zusatzpakete installieren

```bash
pip install bertopic[torch] umap-learn hdbscan scikit-learn spacy numpy pandas stopwords optuna openpyxl
python -m spacy download en_core_web_sm
```

### 4. GPU-Test

```python
import torch

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
```
→ Es sollte `True` und `NVIDIA GeForce RTX 5080` ausgeben.

### 5. SentenceTransformer mit GPU aktivieren

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2", device="cuda")
```

### 6. BERTopic verwenden

```python
from bertopic import BERTopic

topic_model = BERTopic(embedding_model=model)
topics, _ = topic_model.fit_transform(docs)
```

