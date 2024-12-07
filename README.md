# **Crawler AI**

A lightweight web crawling API with semantic search capabilities. This API enables users to scrape web pages, extract structured content, and search for relevant information using advanced natural language processing.

## **Features**
- Scrapes web pages dynamically or statically.
- Extracts content sections based on headings.
- Performs semantic search on extracted content using `sentence-transformers`.
- Recursively scrapes linked pages up to a specified depth.
- Returns results in JSON format.

---

## **Getting Started**

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/crawler-api.git
   cd crawler-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the API:
   ```bash
   python app.py
   ```

---

### **API Endpoints**

#### **1. Crawl Endpoint**
`POST /crawl`

This endpoint performs a web crawl and semantic search based on the provided URL and prompt.

##### **Request Body**
- **`url`** *(string, required)*: The URL of the web page to crawl.
- **`prompt`** *(string, required)*: The search query for semantic search.
- **`max_depth`** *(integer, optional)*: The maximum depth for recursive crawling (default: `0`).

##### **Example Request**
```json
POST http://127.0.0.1:5000/crawl
Content-Type: application/json

{
  "url": "https://example.com",
  "prompt": "Find sections about technology.",
  "max_depth": 1
}
```

##### **Response**
- **200 OK**: Returns the extracted and filtered content based on the prompt.
- **400 Bad Request**: Invalid or missing input fields.
- **500 Internal Server Error**: If an error occurs during crawling or processing.

##### **Example Response**
```json
{
  "results": [
    [32.5, "Technology: This section covers the latest in tech innovations..."],
    [28.0, "Future Trends: Technology is evolving rapidly, with AI at the forefront..."]
  ]
}
```

---

### **Usage Examples**

#### **Using `curl`**
```bash
curl -X POST http://127.0.0.1:5000/crawl \
-H "Content-Type: application/json" \
-d '{
  "url": "https://example.com",
  "prompt": "Find sections about technology.",
  "max_depth": 1
}'
```

#### **Using Python**
```python
import requests

url = "http://127.0.0.1:5000/crawl"
data = {
    "url": "https://example.com",
    "prompt": "Find sections about technology.",
    "max_depth": 1
}

response = requests.post(url, json=data)
print(response.json())
```

---

### **Dependencies**
- `Flask`: For creating the REST API.
- `requests`: For static web scraping.
- `beautifulsoup4`: For HTML parsing.
- `selenium`: For dynamic web scraping.
- `sentence-transformers`: For semantic search.
- `numpy`: For efficient numerical operations.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

### **Development**

1. **Modify `app.py`**: Extend the API to add more endpoints if required.
2. **Test Locally**: Use tools like Postman or `curl` for testing.
3. **Deploy**: Deploy the API to a cloud platform (e.g., Heroku, AWS, or Google Cloud).

---

### **Contributing**
1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

### **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### **Contact**
For any questions or feedback, feel free to contact:

- **Name**: Your Name  
- **Email**: your-email@example.com  
- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)

---

Let me know if you'd like to customize it further!
