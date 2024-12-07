from crawler import CrawlerClient

apikey = "123456"
client = CrawlerClient(apikey)

url = "https://www.sf.gov/"
prompt = "Find sections about services."
max_depth = 0

results = client.get_info(url, prompt, max_depth=max_depth)

print(results)
