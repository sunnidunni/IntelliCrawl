# AI Crawler

**AI Crawler** is a web scraping tool that allows users to crawl a webpage and extract relevant information based on a user-specified prompt. It supports both static and dynamic content scraping using the `requests` library and Selenium. The extracted data is processed using machine learning models for relevance and can be saved and downloaded in JSON format.

## Features

- **Web Crawling**: Crawl web pages recursively and extract sections based on headings.
- **Content Extraction**: Extract content under headings and subheadings (e.g., `h1`, `h2`, `h3` tags).
- **Machine Learning Integration**: Uses a sentence-transformer model to analyze relevance to user queries.
- **Dynamic Scraping**: Supports scraping pages that require JavaScript rendering via Selenium.
- **JSON Output**: Save extracted content in a well-structured, indented JSON format.
- **Downloadable Results**: User interface for downloading the extracted data as a JSON file.

## Requirements

- Python 3.6+

### Install Dependencies:

```bash
pip install -r requirements.txt
```

## Setup

### Clone the Repository:

```bash
git clone https://github.com/sunnidunni/ai-crawler.git
cd ai-crawler
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### API:

To run the API just go into terminal and type `pip install .`

You can then use the API in a similar format as `example.py`

### Run the Flask Application to Show the Web Interface:

You can just run app.py, or in the `app.py` directory, start the Flask app:

```bash
python app.py
```

The server will run on `http://127.0.0.1:5000`.

## API Endpoints

### `POST /crawl`

This endpoint accepts a JSON payload with the following parameters:

- `url`: The URL of the webpage to crawl.
- `prompt`: A query or prompt that will be used to analyze the relevance of the extracted data.
- `max_depth` (Optional): The maximum depth of the crawl (default is `0`).

#### Example Request:

```json
{
  "url": "https://www.sf.gov/",
  "prompt": "What are the available services in San Francisco?",
  "max_depth": 2
}
```

#### Example Response:

```json
{
  "results": [
    {
      "score": 0.95,
      "section": "Services",
      "content": "Activities: Things to do in San Francisco."
    },
    {
      "score": 0.88,
      "section": "Building",
      "content": "Construction resources and property information."
    }
  ]
}
```

## Web Interface

On the web interface users can:

- Input a URL and prompt.
- Set the crawl depth.
- Trigger the crawl and receive results.
- Download the results in a JSON format.

Access the interface at `http://127.0.0.1:5000` after running the Flask app.

![image](https://github.com/user-attachments/assets/b5bddb2a-fd0d-4e06-a86d-28154319e35f)



### Downloading Results

Once you’ve performed a crawl, you can download the results as a JSON file by clicking the **Download** button in the web interface.


## Notes

- **Dynamic Scraping**: To scrape dynamic content (e.g., JavaScript-rendered content), set the `use_dynamic` flag to `True` when initializing the crawler in the `CrawlerClient` class.
- **Limitations**: Be mindful of website terms of service. Ensure you respect `robots.txt` and avoid overloading servers with too many requests.
- **Scores**: Scores are all above 0. The higher the score the more probable that a scraped text is related to the prompt. A score of 20+ is almost always directly related.

