import pandas as pd
from preprocess import clean_text

# Load the original dataset
df = pd.read_csv("Reviews.csv")

print("Total reviews loaded:", len(df))

# Apply preprocessing to every customer review
df["cleaned_text"] = df["Text"].apply(clean_text)

# Compare the original and cleaned reviews
print("\nOriginal review:")
print(df["Text"].iloc[0])

print("\nCleaned review:")
print(df["cleaned_text"].iloc[0])

# Count reviews that changed after preprocessing
changed_reviews = (df["Text"] != df["cleaned_text"]).sum()

print("\nReviews modified:", changed_reviews)

# Save the cleaned dataset
df.to_csv("cleaned_reviews.csv", index=False)

print("\nCleaned dataset saved to cleaned_reviews.csv")