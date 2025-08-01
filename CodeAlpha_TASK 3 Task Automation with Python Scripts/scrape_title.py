import requests
import os
import re

def scrape_title(url, output_file):
    """
    Scrapes the title of the webpage at the given URL and saves it to output_file.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage: {e}")
        return

    # Extract the title using regex
    title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
    else:
        print("Title tag not found in the webpage.")
        return

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(title + '\n')

    print(f"Title saved to {output_file}")

if __name__ == "__main__":
    # Example usage - update the URL and output file as needed
    fixed_url = "https://www.example.com"
    output_file_path = "webpage_title.txt"
    scrape_title(fixed_url, output_file_path)
