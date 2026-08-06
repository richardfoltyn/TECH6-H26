# TECH6: Data Science and Econometrics

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Course material for fall term 2026 (H26) — Author: Richard Foltyn


## Course outline

`L` = Lecture, `W` = Workshop

| Week | Day         | L/W | Topic | Notes & Exercises | Solutions |
|------|-------------|-----|-------|-------------------|-----------|
|  42  | Tue, Oct 13 | `L` | Introduction to scikit-learn | [Notebook](lectures/lecture1/lecture1.ipynb), [PDF](lectures/lecture1/lecture1.pdf) | — |
|      | Thu, Oct 15 | `W` | Introduction to scikit-learn | [Notebook](workshops/workshop1/workshop1.ipynb), [PDF](workshops/workshop1/workshop1.pdf) | TBA |
|  43  | Tue, Oct 20 | `L` | Regression models | [Notebook](lectures/lecture2/lecture2.ipynb), [PDF](lectures/lecture2/lecture2.pdf) | — |
|      | Thu, Oct 22 | `W` | Regression models | [Notebook](workshops/workshop2/workshop2.ipynb), [PDF](workshops/workshop2/workshop2.pdf) | TBA |
|  44  | Tue, Oct 27 | `L` | Classification models | [Notebook](lectures/lecture3/lecture3.ipynb), [PDF](lectures/lecture3/lecture3.pdf) | — |
|      | Thu, Oct 29 | `W` | Classification models | [Notebook](workshops/workshop3/workshop3.ipynb), [PDF](workshops/workshop3/workshop3.pdf) | TBA |


## Cloning & forking the repository

### Cloning

1. Click on the green `Code` icon to clone the repository to your computer
2. Select HTTPS or SSH depending on your authentication method (SSH keys will only work if you have configured them) and copy the URL.
3. You can clone the repository directly in Visual Studio Code, or use the command line:

    _Using HTTPS (no SSH key configured):_
    ```bash
    git clone https://github.com/richardfoltyn/TECH6-H26.git
    ```
    _Using SSH keys:_
    ```bash
    git clone git@github.com:richardfoltyn/TECH6-H26.git
    ```

### Forking

- Click on the `Fork` icon to fork this repository (create your own personal copy)
- In the future, you need to click on `Sync Fork` to get new commits made to this repository into your forked version.


## Creating a Conda environment

Using the Anaconda Prompt (Windows) or Terminal (macOS), you can use
the environment definition file ([environment.yml](environment.yml)) provided in this repository to create
a conda environment called `TECH6`:
```bash
conda env create -f environment.yml
```
Note that you first need to change to the directory where `environment.yml` is located for this to work.

If you don't know how to locate the `environment.yml` file on your system,
you can also download it directly from GitHub and create the environment in one step:
```bash
curl -O https://raw.githubusercontent.com/richardfoltyn/TECH6-H26/main/environment.yml
conda env create -f environment.yml
```


## Additional resources

1. [Think Python](https://allendowney.github.io/ThinkPython/index.html) by Allen B. Downey:
   general intro to Python, chapters are available as Jupyter notebooks.
2. [Python for Everybody](https://www.py4e.com/book) by Charles R. Severance:
   general intro to Python with a focus on data analysis, available as PDF.

## License

This material is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/),
except for the data files contained in the `data/` folder, which
fall under the terms imposed by the original content creators.
