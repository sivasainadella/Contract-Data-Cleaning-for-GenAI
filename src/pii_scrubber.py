import re


def scrub_pii(text: str) -> str:
    """
    Very basic PII scrubbing:
    - Emails
    - Phone numbers
    - Simple ID-like patterns

    This is not exhaustive and only meant as a starting point.
    """

    # Email addresses
    text = re.sub(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "[EMAIL_REDACTED]",
        text,
    )

    # Phone numbers (very loose pattern)
    text = re.sub(
        r"\+?\d[\d\-\s\(\)]{7,}\d",
        "[PHONE_REDACTED]",
        text,
    )

    # Simple ID-like sequences (e.g., 8+ digits)
    text = re.sub(
        r"\b\d{8,}\b",
        "[ID_REDACTED]",
        text,
    )

    return text
