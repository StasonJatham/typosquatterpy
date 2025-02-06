import requests
import time
import random
import re 

def fetch_webpage(url, headers):
    """Fetches a webpage with the specified URL and headers."""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as error:
        print(f"⚠️ Error fetching {url}: {error}")
        return None

def fetch_typo_domains_openai(base_domain, api_key):
    """Fetches the top 10 typo domains using OpenAI API."""
    openai_api_url = "https://api.openai.com/v1/chat/completions"
    request_payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are an assistant that generates typo domain variations."},
            {"role": "user", "content": f"Generate the top 10 most common typo domains for {base_domain} in germany on QWERTZ keyboard. Only return a numbered list, no explanations."}
        ]
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(openai_api_url, json=request_payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    except requests.RequestException as error:
        print(f"⚠️ Error fetching typo domains for {base_domain}: {error}")
        return None

def extract_domains_from_text(response_text):
    """Extracts domain names from a text response using regex."""
    if not response_text:
        return []
    domain_pattern = r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"
    return re.findall(domain_pattern, response_text)

def is_domain_available(domain_names):
    """Checks if a list of domains is available on Strato."""    
    for index, domain_name in enumerate(domain_names, start=1):
        strato_api_url = f"https://www.strato.de/orca/domain_name_search/get_domain_status/by_domain_name/strato/DE/{domain_name}"
        request_headers = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Safari/605.1.15",
        }
        
        response = fetch_webpage(strato_api_url, request_headers)
        if response:
            try:
                response_data = response.json()
                domain_status = response_data.get("domain_status", {}).get(domain_name, -1)
                
                if domain_status == 0:
                    print(f"✅ {domain_name}")
                else:
                    print(f"❌ {domain_name}")
            except ValueError:
                print("⚠️ Error parsing JSON response.")
        
        if index % 5 == 0:
            delay = random.uniform(0, 2)
            time.sleep(delay)
    
if __name__ == "__main__":
    base_domain = "karlcom"
    tld = ".de"
    typo_response = fetch_typo_domains_openai(base_domain, api_key="sk-proj-XXXXXX")
    typo_domains_base = extract_domains_from_text(typo_response)
    typo_domains = [domain.split(".")[0].rstrip(".") + tld for domain in typo_domains_base]
    is_domain_available(typo_domains)
