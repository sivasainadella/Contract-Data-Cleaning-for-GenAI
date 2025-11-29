import re
import unicodedata


def normalize_text(text: str) -> str:
    """
    Basic normalization:
    - Unicode normalization
    - Normalize whitespace
    - Remove common header/footer noise patterns (very generic)
    """
    if not text:
        return ""

    # Unicode normalize
    text = unicodedata.normalize("NFKC", text)

    # Remove repeated blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove common page markers like "Page 1 of 10"
    text = re.sub(r"Page\s+\d+\s+of\s+\d+", "", text, flags=re.IGNORECASE)

    # Collapse multiple spaces
    text = re.sub(r"[ \t]{2,}", " ", text)

    # Strip trailing spaces on each line
    text = "\n".join(line.rstrip() for line in text.splitlines())

    return text.strip()
