import pandas as pd

# Load the original and cleaned datasets
original = pd.read_csv("Reviews.csv")
cleaned = pd.read_csv("cleaned_reviews.csv")

# Select the same 10,000 reviews from both datasets
sample_ids = original.sample(n=10000, random_state=42).index

dirty_sample = original.loc[sample_ids]
cleaned_sample = cleaned.loc[sample_ids]

# Save the files for GitHub
dirty_sample.to_csv("dirty_reviews_sample.csv", index=False)
cleaned_sample.to_csv("cleaned_reviews_sample.csv", index=False)

print("Dirty sample:", len(dirty_sample))
print("Cleaned sample:", len(cleaned_sample))
print("Sample datasets saved successfully!")