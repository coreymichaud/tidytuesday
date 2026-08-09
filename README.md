# My TidyTuesday Visualizations

This repository is to store my work for the [TidyTuesday](https://github.com/rfordatascience/tidytuesday) weekly challenge.

Feel free to search around for my code! The way I've structured this is as follows:

```
tidytuesday/
└── year/
    └── week-#/
        ├── eda.py           # exploratory data analysis, rendered as a notebook
        ├── app.py           # streamlit dashboard
        └── README.md        # data information, process, links, image of dashboard, etc.
```

## What is TidyTuesday?

TidyTuesday is a social data project where each week a dataset is given for others to analyze, visualize, and post online. You can easily find these posts by searching on most social platforms for the hashtag
`#TidyTuesday` or `#PydyTuesday` so that you can check out what people are creating! It's nice to see how others interpreted the same data you were looking at.

## Goals

1. Practice exploratory data analysis on new data
2. Strengthen my data visualization and storytelling skills
3. Build a public portfolio showcasing mainly data visualization

## Run a given week

1. **Clone repository and change directory:**
    ```
    git clone https://github.com/coreymichaud/tidytuesday.git
    cd tidytuesday
    ```

2. **Sync with `uv`:**
    ```
    uv sync
    ```

3. **Change directories into a week and follow that week's `README.md` for specific instructions and information. For example:**
    ```
    cd 2026/week-30
    uv run streamlit run app.py
    ```