import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("cleaned_reviews.csv", keep_default_na=False)

print("Total reviews:", len(df))

# Check whether cleaning produced empty reviews
empty_reviews = df["cleaned_text"].str.strip().eq("").sum()
print("Empty cleaned reviews:", empty_reviews)

# Check for remaining HTML-like tags
remaining_html = df["cleaned_text"].str.contains(
    r"<[a-zA-Z/][^>]*>", regex=True
).sum()

# Check for remaining URLs
remaining_urls = df["cleaned_text"].str.contains(
    r"https?://\S+|www\.\S+",
    regex=True,
    case=False
).sum()

print("Reviews with remaining HTML-like tags:", remaining_html)
print("Reviews with remaining URLs:", remaining_urls)

# Compare examples where the text actually changed
changed = df[df["Text"] != df["cleaned_text"]]

print("\nSample before-and-after comparisons:")

for _, row in changed.head(3).iterrows():
    print("\nOriginal:")
    print(row["Text"][:500])

    print("\nCleaned:")
    print(row["cleaned_text"][:500])
    print("-" * 60)

# Find reviews that still contain URLs
remaining_url_reviews = df[
    df["cleaned_text"].str.contains(
        r"https?://\S+|www\.\S+",
        regex=True,
        case=False
    )
]

print("\nReviews with remaining URLs:")

for _, row in remaining_url_reviews.iterrows():
    print("\nReview ID:", row["Id"])
    print("Original text:")
    print(row["Text"])

    print("\nCleaned text:")
    print(row["cleaned_text"])
    print("-" * 60)