<!--
NOTES:
- I kind of like this person's README: https://github.com/z3tt/TidyTuesday because I was going to do a grid of images, but this way you can fully see the visualizations even if there is a lot.
  If I were to do something like that, I would want it to have a title that links it to the folder, and clicking the picture would take you to streamlit cloud. I would have to explain that before the images.
  Also, once I do this i would want to remove the "how to run" section because i don't think people care, unless i fr just keep it for the end, which i could.
-->

# My TidyTuesday Visualizations

This repository is to store my work for the [TidyTuesday](https://github.com/rfordatascience/tidytuesday) weekly challenge.

## What is TidyTuesday?

TidyTuesday is a social data project organized by the [Data Science Learning Community](https://dslc.io/), where each week a dataset is given for others to analyze, visualize, and post online.

You can easily find these posts by searching on most social platforms for the hashtag `#TidyTuesday` or `#PydyTuesday` so that you can check out what people are creating! It's nice to see how others interpreted the same data you were looking at.

## Structure

If you want to check out any of the code, I've structured this repo as follows:

```
tidytuesday/
└── year/
    └── week-#/
        ├── eda.ipynb      # exploratory data analysis, rendered as a notebook
        ├── app.py         # streamlit dashboard (if no single visualization)
        ├── vizname.ipynb  # final visualization, rendered a a notebook (if no dashboard)
        ├── vizname.png    # image of dashboard or single visualization
        └── README.md      # week-specific information, process, links, image of viz, ...
```

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