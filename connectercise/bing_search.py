import json
import requests

def read_bing_key():
    bing_api_key = None
    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline().strip()
    except:
        try:
            with open('../bing.key') as f:
                bing_api_key = f.readline().strip()
        except:
            raise IOError('bing.key file not found')
    
    if not bing_api_key:
        raise KeyError('Bing key not found')

    return bing_api_key

def run_query(search_terms):
    bing_key = read_bing_key()
    search_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
    headers = {'Ocp-Apim-Subscription-Key': bing_key}
    params = {'q': search_terms, 'textDecorations': True, 'textFormat': 'HTML'}

    # Issue the request, given the details above.
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    results = []
    for result in search_results['webPages']['value']:
        results.append({
            'title': result['name'],
            'link': result['url'],
            'summary': result['snippet']})
    return results

def main():
    search = input("Please enter your search query here: ")
    print(run_query(search))

if __name__ == '__main__':
    main()
