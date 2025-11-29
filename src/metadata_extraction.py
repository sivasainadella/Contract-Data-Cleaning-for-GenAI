import re
from dataclasses import dataclass, asdict
from typing import Optional, Dict

from dateutil import parser as dateparser


@dataclass
class ContractMetadata:
    party_1: Optional[str] = None
    party_2: Optional[str] = None
    effective_date: Optional[str] = None
    expiration_date: Optional[str] = None
    governing_law: Optional[str] = None

    def to_dict(self) -> Dict:
        return asdict(self)


def extract_metadata(text: str) -> ContractMetadata:
    """
    Very simple, pattern-based metadata extractor.
    This is intentionally basic and can be replaced with NLP/NER later.
    """
    metadata = ContractMetadata()

    # Try to find "This Agreement is made between X and Y"
    m = re.search(
        r"between\s+(.*?)\s+and\s+(.*?)[\.,\n]", text, flags=re.IGNORECASE | re.DOTALL
    )
    if m:
        metadata.party_1 = m.group(1).strip()
        metadata.party_2 = m.group(2).strip()

    # Effective date
    eff = _find_date_near_phrase(text, ["effective date", "effective as of"])
    if eff:
        metadata.effective_date = eff

    # Expiration/termination date
    exp = _find_date_near_phrase(text, ["expiration date", "term ends on"])
    if exp:
        metadata.expiration_date = exp

    # Governing law
    gov = re.search(
        r"governed by the laws of\s+([A-Za-z ,]+)", text, flags=re.IGNORECASE
    )
    if gov:
        metadata.governing_law = gov.group(1).strip()

    return metadata


def _find_date_near_phrase(text: str, phrases):
    window_chars = 120
    for phrase in phrases:
        for m in re.finditer(phrase, text, flags=re.IGNORECASE):
            start = max(0, m.start() - 10)
            end = min(len(text), m.end() + window_chars)
            snippet = text[start:end]
            # very naive date parse
            try:
                dt = dateparser.parse(snippet, fuzzy=True)
                return dt.date().isoformat()
            except Exception:
                continue
    return None
