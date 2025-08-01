import os
import tempfile
from extract_emails import extract_emails

def create_text_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def test_extract_emails_normal():
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.txt")
        output_path = os.path.join(tmpdir, "output.txt")
        content = "Contact us at test@example.com and support@example.org."
        create_text_file(input_path, content)
        extract_emails(input_path, output_path)
        with open(output_path, 'r', encoding='utf-8') as f:
            emails = f.read().splitlines()
        print("DEBUG: Extracted emails:", emails)
        assert "test@example.com" in emails
        assert "support@example.org" in emails
        assert len(emails) == 2

def test_extract_emails_no_emails():
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.txt")
        output_path = os.path.join(tmpdir, "output.txt")
        content = "This text has no email addresses."
        create_text_file(input_path, content)
        extract_emails(input_path, output_path)
        with open(output_path, 'r', encoding='utf-8') as f:
            emails = f.read().splitlines()
        assert len(emails) == 0

def test_extract_emails_duplicates():
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.txt")
        output_path = os.path.join(tmpdir, "output.txt")
        content = "Email: duplicate@example.com, duplicate@example.com"
        create_text_file(input_path, content)
        extract_emails(input_path, output_path)
        with open(output_path, 'r', encoding='utf-8') as f:
            emails = f.read().splitlines()
        assert emails == ["duplicate@example.com"]

def test_extract_emails_malformed():
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.txt")
        output_path = os.path.join(tmpdir, "output.txt")
        content = "Valid: valid@example.com, Invalid: invalid@com, @missing.com"
        create_text_file(input_path, content)
        extract_emails(input_path, output_path)
        with open(output_path, 'r', encoding='utf-8') as f:
            emails = f.read().splitlines()
        assert "valid@example.com" in emails
        assert "invalid@com" not in emails
        assert "@missing.com" not in emails

if __name__ == "__main__":
    test_extract_emails_normal()
    test_extract_emails_no_emails()
    test_extract_emails_duplicates()
    test_extract_emails_malformed()
    print("All extract_emails tests passed.")
