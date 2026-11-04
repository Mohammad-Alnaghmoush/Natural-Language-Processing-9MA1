# Natural Language Processing — Labs 1–11

**Student:** Mohammad Abdalrouf Alnaghmoush  
**Student ID:** 2230004028  
**Course repository:** Natural Language Processing (9MA1)

All eleven numbered labs are available as Jupyter notebooks with their **actual saved execution outputs**. Open any `.ipynb` file directly on GitHub to view printed results, tables, and embedded plots without running the notebook.

## Notebook submission index

| Lab | Executed code cells | Cells with visible output | Embedded PNG plots |
|---|---:|---:|---:|
| [Lab 1](lap1_NLP.ipynb) | 6/6 | 6 | 0 |
| [Lab 2](lab2_NLP_folder/Lab2_NLP.ipynb) | 1/1 | 1 | 0 |
| [Lab 3](Lab3_NLP_folder/Lab3_NLP.ipynb) | 6/6 | 6 | 0 |
| [Lab 4](lab4_NLP/lab4_NLP.ipynb) | 6/6 | 6 | 1 |
| [Lab 5](lab5_NLP.ipynb) | 5/5 | 5 | 0 |
| [Lab 6 — completed extended version](lab6__NLP.ipynb) | 13/13 | 11 | 0 |
| [Lab 6 — original version](lab6_NLP.ipynb) | 11/11 | 10 | 0 |
| [Lab 7](Lab7_LLMs_Completed.ipynb) | 10/10 | 9 | 0 |
| [Lab 8](Lab8_POS_Completed_Mohammad_Alnaghmoush.ipynb) | 17/17 | 12 | 0 |
| [Lab 9](Lab9_NER_Completed_Mohammad_Alnaghmoush.ipynb) | 8/8 | 7 | 0 |
| [Lab 10](Lab10_Machine_Translation_Completed_Mohammad_Alnaghmoush.ipynb) | 13/13 | 12 | 1 |
| [Lab 11](Lab11_Attention_with_RNN/Lab11_Attention_RNN_Completed_Mohammad_Alnaghmoush.ipynb) | 9/9 | 8 | 4 |

*Audit checked on November 4, 2026. The repository contains twelve notebooks because Lab 6 has two versions. All nonempty code cells were executed; no recorded cell errors remain.*

## Dataset and reproduction notes

- **Lab 1:** Downloads IMDb movie reviews through KaggleHub when executed.
- **Lab 2:** Its Apple tweets CSV is included in `lab2_NLP_folder/Apple_tweets.csv`.
- **Lab 3:** The recorded outputs are saved, but the original large `Random Tweets from Pakistan- Cleaned- Anonymous.csv` file is **not** included in the repository. Re-running requires that dataset.
- **Lab 4:** The recorded Naive Bayes evaluation and confusion matrix are saved, but `Amazon_Unlocked_Mobile.csv` is **not** included. Re-running requires that dataset.
- **Lab 5:** Word similarity and TF-IDF outputs are saved in its notebook.
- **Lab 6:** Both versions were executed on the actual 1,000 Yelp reviews from the [UCI Sentiment Labelled Sentences dataset](https://archive.ics.uci.edu/dataset/331/sentiment+labelled+sentences). The required data is included as [07-yelp-dataset.txt](07-yelp-dataset.txt); the extended notebook additionally covers Word2Vec.
- **Lab 7:** Actual Hugging Face transformer inference outputs, including the required tasks and optional sampling challenge, are saved.
- **Lab 8:** POS tagging outputs are saved. Its offline NLTK/spaCy fallbacks are explicitly noted in the notebook.
- **Lab 9:** Entity recognition outputs and 20 iterations of training a custom spaCy NER model are saved. Rule-based demonstration inputs are identified in the notebook.
- **Lab 10:** Outputs were executed on 1,200 real English–French sentence pairs downloaded from the public Kaggle corpus; results are for a small educational model, not a production translator.
- **Lab 11:** Uses the included [original Q&A dataset](Lab11_Attention_with_RNN/dataset/Lab_11_QnA_Dataset.csv) (168 examples); training results and attention visualizations are saved.

**Important:** Execution counts and stored outputs mean these notebook runs completed successfully; they do not establish that the models generalize well to unseen datasets.

## How to view outputs

Open any linked `.ipynb` notebook above. GitHub's notebook preview renders printed output and embedded images directly below the relevant cells. Re-running is **not required** to inspect the saved results.

The `.github/workflows/` folder and the `execute_lab6.py` / `execute_lab7.py` scripts document reproducible runs for the notebooks whose outputs were refreshed.
