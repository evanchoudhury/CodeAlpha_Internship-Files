import re
import os

def extract_emails(input_file, output_file):
    """
    Extracts all email addresses from the input_file and saves them to output_file.
    """
    if not os.path.exists(input_file):
        print(f"Input file does not exist: {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Regex pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)

    # Remove duplicates by converting to a set
    unique_emails = sorted(set(emails))

    with open(output_file, 'w', encoding='utf-8') as f:
        for email in unique_emails:
            f.write(email + '\n')

    print(f"Extracted {len(unique_emails)} unique email(s) to {output_file}")

if __name__ == "__main__":
    # Example usage - update these paths as needed
    input_txt_file = "input.txt"
    output_emails_file = "extracted_emails.txt"
    extract_emails(input_txt_file, output_emails_file)
