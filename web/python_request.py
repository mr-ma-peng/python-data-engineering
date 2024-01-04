import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'accept': 'application/vnd.github.v3+json'}
result = requests.get(url, headers=headers)
print(f"status code: {result.status_code}")

response = result.json()
print(f"total repositories: {response['total_count']}")