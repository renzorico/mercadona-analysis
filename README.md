# Mercadona Products Scraper and Analysis

## Overview

This project is designed to scrape product information from the Mercadona supermarket website, process the data, and perform analysis. The web scraping is done using Selenium, and the data is stored in a Pandas DataFrame for further analysis.

## Folder Structure

.
├── app
│ ├── init.py
│ ├── product.py
│ ├── scraper.py
├── data
├── notebooks
│ └── testing.ipynb
├── main.py
├── README.md
└── requirements.txt

- **utils**: Contains the main application files.

  - `__init__.py`: Initializes the app module.
  - `product.py`: Defines the Product class.
  - `scraper.py`: Defines the MercadonaScraper class.

- **data**: Placeholder for storing scraped data.

- **notebooks**: Jupyter notebooks for testing and exploration.

- **main.py**: The main entry point for the application.

- **README.md**: Project documentation explaining the purpose, structure, and usage.

- **requirements.txt**: Lists the dependencies required to run the project.

## Getting Started

1. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt

   ```

2. Run the main script:
   ```bash
   python main.py
   ```

Data Processing

    The scraped data is stored in a Pandas DataFrame for easy analysis.
    Columns such as "Precio" and "Unidad" are processed to convert them into a suitable format.

Streamlit Web App

    A Streamlit web app is planned to visualize and explore the product data by categories.

Contributions

Feel free to contribute by opening issues or creating pull requests. Your feedback and contributions are highly appreciated!
