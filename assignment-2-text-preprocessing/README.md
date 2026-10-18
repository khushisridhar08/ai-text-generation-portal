# Assignment 2 - Text Preprocessing

For this assignment, I worked with the Amazon Fine Food Reviews dataset from Kaggle, containing 568,454 customer reviews.

I explored the dataset to identify missing values, duplicate reviews, HTML tags, URLs, and inconsistent punctuation.

I then used Python, pandas, regular expressions, and BeautifulSoup to clean the review text. The original text was preserved alongside the cleaned text for comparison.

After preprocessing, I validated the results to check for remaining HTML tags, URLs, and empty reviews.

## Files

- `explore_data.py` - Examines the dataset and identifies text issues.
- `preprocess.py` - Contains the text-cleaning function.
- `clean_dataset.py` - Applies preprocessing and exports the cleaned data.
- `validate_data.py` - Validates the cleaned output.
- `prepare_submission.py` - Creates sample datasets for GitHub.
- `dirty_reviews_sample.csv` - Original reviews before cleaning.
- `cleaned_reviews_sample.csv` - Corresponding cleaned reviews.

## Running the Project

Download `Reviews.csv` from [Amazon Fine Food Reviews on Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) and place it in this folder.

Install dependencies:

`uv sync`

Run the scripts:

```bash
uv run explore_data.py
uv run clean_dataset.py
uv run validate_data.py
uv run create_samples.py
```

## Issues Found in the Dataset

While exploring the 568,454 Amazon customer reviews, I noticed several issues:

- 147,324 reviews contained HTML-like tags.
- 11,788 reviews contained URLs.
- 106,902 reviews contained repeated punctuation.
- 1,083 reviews contained non-ASCII characters.
- 174,875 reviews had duplicate review text, and 27 reviews had missing summaries.

## Cleaning Techniques Used

I used BeautifulSoup to remove HTML tags while keeping the actual review text, and regular expressions to remove URLs, normalize repeated punctuation, and remove extra whitespace. I also used Python's `html` module to decode HTML entities.

I kept the original reviews alongside the cleaned text so I could compare them. I didn't remove duplicate reviews or non-ASCII characters automatically, since they aren't necessarily errors.

After cleaning, I validated the dataset and confirmed that no HTML-like tags, URLs, or empty reviews remained.