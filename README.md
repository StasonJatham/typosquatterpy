# typosquatterpy

## 🚀 What is typosquatterpy?

**typosquatterpy** is a Python script that generates common typo domain variations of a given base domain (on a QWERTZ keyboard) using OpenAI's API and checks their availability on Strato. This tool helps in identifying potential typo-squatted domains that could be registered to protect a brand or business.

⚠️ **Disclaimer:** This project is not affiliated with Strato, nor is it their official API. Use this tool at your own risk!

---

## 🛠️ Installation

To use **typosquatterpy**, you need Python and the `requests` library installed. You can install it via pip:

```bash
pip install requests
```

---

## 📖 Usage

Run the script with the following steps:

1. Set your **base domain** (e.g., `example`) and **TLD** (e.g., `.de`).
2. Replace `api_key="sk-proj-XXXXXX"` with your actual OpenAI API key.
3. Run the script, and it will:
   - Generate the top 10 most common typo domains.
   - Check their availability using Strato’s unofficial API.

### Example Code Snippet

```python
base_domain = "karlcom"
tld = ".de"
typo_response = fetch_typo_domains_openai(base_domain, api_key="sk-proj-XXXXXX")
typo_domains_base = extract_domains_from_text(typo_response)
typo_domains = [domain.split(".")[0].rstrip(".") + tld for domain in typo_domains_base]
is_domain_available(typo_domains)
```

### Output Example

```bash
✅ karicom.de
❌ karlcomm.de
✅ krlcom.de
```

---

## ⚠️ Legal Notice

- **typosquatterpy** is not affiliated with Strato and does not use an official Strato API.
- The tool scrapes publicly available information, and its use is at your own discretion.
- Ensure you comply with any legal and ethical considerations when using this tool.

---

## 📜 License

This project is open-source and available under the MIT License. Feel free to contribute and improve it!

