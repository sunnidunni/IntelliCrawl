import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from sentence_transformers import SentenceTransformer, util
import numpy as np
import re
from urllib.parse import urljoin
import json

def update_and_combine(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1 and dict1[key] != value:
            # Combine the values into a list
            dict1[key] += '\n'+ value
        else:
            dict1[key] = value
    return dict1


class Crawler:
    def __init__(self, use_dynamic=False):
        self.use_dynamic = use_dynamic
        if use_dynamic:
            options = Options()
            options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=options)

    def scrape_page(self, url, depth, max_depth, visited):
        if depth > max_depth or url in visited:
            return {}
        visited.add(url)  # Mark the URL as visited
        try:
            # Send a GET request
            if self.use_dynamic:
                self.driver.get(url)
                html = self.driver.page_source
            else:
                response = requests.get(url)
                html = response.text

            # Parse the HTML content
            soup = BeautifulSoup(html, 'html.parser')

            # Extract sections based on headings
            sections = {}
            for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5']):  # Adjust based on heading levels used
                section_title = heading.get_text(strip=True)
                next_node = heading.find_next_sibling()
                section_content = []

                # Collect content until the next heading or end of the document
                while next_node and next_node.name not in ['h1', 'h2', 'h3','h4', 'h5']:
                    if next_node.name in ['p', 'div']:
                        section_content.append(re.sub(r'\n+', '\n', next_node.get_text()))
                    next_node = next_node.find_next_sibling()

                sections[section_title] = ' '.join(section_content)

            # Find all links on the page
            links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]


            # Recursively scrape linked pages
            for link in links:

                sections = update_and_combine(sections, self.scrape_page(link, depth + 1, max_depth, visited))

            return sections

        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
            return {}



    def get_info(self, url, prompt, max_depth=0):
        sections = self.scrape_page(url, 0, max_depth, set())
        docs = [x+':: '+y for x,y in zip(list(sections.keys()), list(sections.values()))]
        #list(filter(lambda x: len(x) > 20, text.split('\n')))

        # Load the model
        model = SentenceTransformer(
            'sentence-transformers/multi-qa-mpnet-base-dot-v1')

        # Encode query and documents
        query_emb = model.encode(prompt)
        doc_emb = model.encode(docs)

        # Compute dot score between query and all document embeddings
        scores = util.dot_score(query_emb, doc_emb)[0].cpu().tolist()

        # Combine docs & scores
        doc_score_pairs = list(zip(docs, scores))

        # Output passages & scores
        lst = []
        for doc, score in doc_score_pairs:
            lst.append(score)
        lst2 = []
        for doc, score in doc_score_pairs:
            if score > 16:
                lst2.append([score, doc])

        contents = list(map(lambda x: str(x[0])+":: "+x[1], lst2))
        result = {'url':url,'sections':[]}

        for item in contents:
            result['sections'].append({'score': item.split(":: ")[0],'heading':item.split(":: ")[1],'content':item.split(":: ")[2].replace('\n',' ')})
        return result
