import re
import html
from bs4 import BeautifulSoup


def clean_text(text):
    # Handle missing or non-text values
    if not isinstance(text, str):
        return ""

    # Convert HTML entities into normal characters
    text = html.unescape(text)

    # Remove HTML markup only when tags are present
    if re.search(r"<[a-zA-Z/][^>]*>", text):
        soup = BeautifulSoup(text, "html.parser")
        text = soup.get_text(separator=" ")

    # Remove URLs
    text = re.sub(
    r"https?://\S+|www\.\S+",
    " ",
    text,
    flags=re.IGNORECASE
)

    # Replace repeated punctuation with a single character
    # Normalize repeated punctuation
    text = re.sub(r"\.{2,}", ". ", text)
    text = re.sub(r"([!?])\1+", r"\1", text)
    text = re.sub(r",{2,}", ",", text)

    # Remove extra spaces and line breaks
    text = re.sub(r"\s+", " ", text).strip()

    return text

if __name__ == "__main__":
    sample = "I LOVE this product!!!<br /><br />Visit https://example.com for more."

    print("Original text:")
    print(sample)

    print("\nCleaned text:")
    print(clean_text(sample))

    print("\nPunctuation test:")

    sample_review = "The peanuts were great...I loved them!!! Would buy again!!"

    print("Original:", sample_review)
    print("Cleaned:", clean_text(sample_review))