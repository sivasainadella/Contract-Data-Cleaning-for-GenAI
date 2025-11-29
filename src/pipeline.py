from dataclasses import dataclass, asdict
from typing import List, Dict

from .text_normalization import normalize_text
from .metadata_extraction import extract_metadata, ContractMetadata
from .pii_scrubber import scrub_pii
from .tokenizer_prep import chunk_for_tokenizer


@dataclass
class CleanedContract:
    cleaned_text: str
    chunks: List[str]
    metadata: Dict


def clean_contract_text(raw_text: str) -> CleanedContract:
    """
    High-level pipeline:
    1. Normalize text
    2. Extract metadata
    3. Scrub PII
    4. Chunk for tokenizer
    """
    normalized = normalize_text(raw_text)
    metadata: ContractMetadata = extract_metadata(normalized)
    scrubbed = scrub_pii(normalized)
    chunks = chunk_for_tokenizer(scrubbed)

    return CleanedContract(
        cleaned_text=scrubbed,
        chunks=chunks,
        metadata=metadata.to_dict(),
    )


def clean_and_print_summary(raw_text: str):
    result = clean_contract_text(raw_text)
    print("=== METADATA ===")
    print(result.metadata)
    print("\n=== FIRST 500 CHARS (CLEANED) ===")
    print(result.cleaned_text[:500])
    print("\n=== NUMBER OF CHUNKS ===")
    print(len(result.chunks))
