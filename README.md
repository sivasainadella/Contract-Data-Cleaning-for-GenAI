# Contract-Data-Cleaning-for-GenAI
Data-cleaning pipeline for preparing biotech/pharma contracts for GenAI: normalization, metadata extraction, PII scrubbing, and chunking for better NLP/RAG results.

This repository provides a reference pipeline for **cleaning and preparing
contract documents** for GenAI and NLP use cases.

It focuses on real-world challenges found in **biotech, pharma, payer–provider,
and complex B2B contracting**, where data quality directly impacts
clause extraction, RAG accuracy, and downstream analytics.

---

## What This Project Does

- Normalizes noisy contract text  
- Extracts key metadata (account, product, dates, jurisdiction, etc.)  
- Detects and masks **PII/sensitive fields**  
- Prepares cleaned text for **tokenization and embedding**  
- Provides a simple, composable **Python pipeline**

---

##  Why Data Cleaning Matters for GenAI

GenAI models are only as good as the text they see.

Contracts often contain:
- OCR noise, page numbers, headers/footers
- Inconsistent formatting
- Mixed clauses and tables
- PII and sensitive fields

Cleaning this up:
- Improves **retrieval quality** in RAG
- Reduces token waste and cost
- Lowers hallucinations
- Helps compliance and privacy reviews

---

##  Project Layout

```txt
src/
  text_normalization.py   # normalize whitespace, encoding, boilerplate
  metadata_extraction.py  # extract key entities/fields from text
  pii_scrubber.py         # mask/remove sensitive data (names, emails, ids)
  tokenizer_prep.py       # prepare chunks for LLM/tokenizer
  pipeline.py             # glue everything together

notebooks/
  cleaning_pipeline_example.ipynb  # example of the full flow

README.md
requirements.txt
LICENSE

Quickstart
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
Then in Python
from src.pipeline import clean_contract_text

raw_text = open("sample_contract.txt", encoding="utf-8").read()
result = clean_contract_text(raw_text)

print(result.cleaned_text[:1000])
print(result.metadata)