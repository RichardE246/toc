# Script to add an outline table of contexts to the Barbados Economic and Social Report 2024

Note: This project uses Python version 3.12 and [uv](https://docs.astral.sh/uv/) as a Python project manager. If possible, it may be prudent to do the same.

## Description

Within this repo there is:

* Within ```source/``` directory
    * A copy of the Barbados Economic and Social Report 2024 PDF file.
    * A CSV file of the PDF's headers and subheaders and associated page numbers.
* WIthin ```build/``` directory:
    * A generated copy of the Barbados Economic and Social Report 2024 PDF with clickable outline/table of contents - named **Barbados-Economic-and-Social-Report-2024_Outlined.pdf**.
* Code to generate and attach the outline to the PDF, in ```main.py```



## Instructions

1. Install Python dependencies via:

   * **Pip + requirements.txt**
        ```bash
        pip install requirements.txt
        ```

    * **Pip + pyproject.toml**
        ```bash
        pip install .
        ```

    * **Poetry**
        ```bash
        poetry install
        ```

    * **Uv**
        ```bash
        uv sync
        ```

2. Run command:
    ```bash
    python3 main.py
    ```

    or if you have uv installed:

    ```bash
    uv run main.py
    ```

    A  new **Barbados-Economic-and-Social-Report-2024_Outlined.pdf** will be generated in the ```build/``` directory.