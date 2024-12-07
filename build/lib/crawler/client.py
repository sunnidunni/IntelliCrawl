from .core import Crawler

class CrawlerClient:
    def __init__(self, apikey: str, use_dynamic: bool = False):
        # Initialize the Crawler and validate the API key
        self.validate_apikey(apikey)
        self.crawler = Crawler(use_dynamic=use_dynamic)

    def validate_apikey(self, apikey: str):
        """Validate the provided API key."""
        valid_key = '123456'  # Replace with a secure key mechanism
        if apikey != valid_key:
            raise ValueError("Invalid API Key")

    def get_info(self, url: str, prompt: str, max_depth: int = 0):
        return self.crawler.get_info(url, prompt, max_depth=max_depth)
