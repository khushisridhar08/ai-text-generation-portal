import pandas as pd

# Load the customer reviews dataset
df = pd.read_csv("Reviews.csv")

# Check the size of the dataset
print("Dataset shape:", df.shape)

# Display the column names
print("\nColumn names:")
print(df.columns.tolist())

# Display the first five rows
print("\nFirst five rows:")
print(df.head())

# Display five sample customer reviews
print("\nSample customer reviews:")
for i, review in enumerate(df["Text"].head(5), start=1):
    print(f"\nReview {i}:")
    print(review)

# Check for missing values in each column
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Check for duplicate review text
print("Duplicate reviews:", df["Text"].duplicated().sum())

# Check the length of customer reviews
df["review_length"] = df["Text"].fillna("").str.len()

print("\nReview length statistics:")
print(df["review_length"].describe())

# Identify common text formatting issues
text = df["Text"].fillna("")

# Check for HTML tags
html_mask = text.str.contains(r"<[^>]+>", regex=True)

# Check for URLs
url_mask = text.str.contains(
    r"https?://\S+|www\.\S+",
    regex=True,
    case=False
)

# Check for repeated punctuation
punctuation_mask = text.str.contains(
    r"[!?.,]{2,}",
    regex=True
)

# Check for non-ASCII characters
non_ascii_mask = text.str.contains(
    r"[^\x00-\x7F]",
    regex=True
)

print("\nText formatting issues:")
print("Reviews containing HTML-like tags:", html_mask.sum())
print("Reviews containing URLs:", url_mask.sum())
print("Reviews containing repeated punctuation:", punctuation_mask.sum())
print("Reviews containing non-ASCII characters:", non_ascii_mask.sum())

# Display examples of reviews containing HTML
print("\nSample reviews containing HTML:")
for review in text[html_mask].head(3):
    print("\n", review[:500])

# Display examples of reviews containing URLs
print("\nSample reviews containing URLs:")
for review in text[url_mask].head(3):
    print("\n", review[:500])