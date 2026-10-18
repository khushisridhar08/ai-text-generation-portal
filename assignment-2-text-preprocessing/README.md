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