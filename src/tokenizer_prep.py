from typing import List


def chunk_for_tokenizer(
    text: str,
    max_chars: int = 1200,
    overlap: int = 200,
) -> List[str]:
    """
    Simple character-based chunking with overlap, meant to approximate
    tokenizer-friendly segments while preserving some context.
    """
    chunks = []
    start = 0
    length = len(text)

    while start < length:
        end = min(start + max_chars, length)
        chunk = text[start:end]
        chunks.append(chunk)
        if end == length:
            break
        start = end - overlap

    return chunks
