# Jaipur Market Analysis

A project to analyze Jaipur's market landscape, focusing on data for working professionals, students, companies, and more. We gather and process data from Google Maps and other sources to generate insights for strategic decisions.


## Setup & Installation

1. **Clone & Enter Directory**:
   ```bash
   git clone https://github.com/yourusername/jaipur-market-analysis.git
   cd jaipur-market-analysis
   ```
# Create a Virtual Environment & Activate:

bash

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# Install Dependencies:

bash

    pip install -r requirements.txt

    Set Up Configurations:
        .env: Add API keys like GOOGLE_MAPS_API_KEY=your_key.
        config/config.yaml: Store location settings (e.g., radius).

Scripts

    data_collection.py: Collects data from the Google Maps API, saving it in data/raw/.
    data_processing.py: Cleans the data, saves processed files to data/processed/.
    generate_report.py: Generates summaries and visualizations.

Run any script with:

bash

python scripts/<script_name>.py

Notebooks

    data_exploration.ipynb: Initial data exploration.
    visualization.ipynb: Generate detailed visualizations.

Launch notebooks:

bash

jupyter notebook

Workflow

    Collect Data: data_collection.py
    Process Data: data_processing.py
    Analyze & Visualize: Jupyter notebooks
    Generate Reports: generate_report.py

Requirements

Install dependencies listed in requirements.txt:

bash

pip install -r requirements.txt
