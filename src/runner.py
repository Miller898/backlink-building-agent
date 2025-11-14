thonimport json
import logging
from pathlib import Path

from extractors.parser import PageParser
from extractors.contact_utils import extract_contacts
from outreach.sequence_generator import generate_sequences
from outputs.exporters import export_results

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def load_keywords():
    sample_path = Path(__file__).resolve().parents[1] / "data" / "keywords.sample.json"
    if not sample_path.exists():
        raise FileNotFoundError("keywords.sample.json not found.")
    with open(sample_path, "r") as f:
        return json.load(f)

def main():
    logging.info("Starting backlink scraper run...")

    keywords = load_keywords()
    parser = PageParser()

    results = []

    for keyword in keywords:
        logging.info(f"Processing keyword: {keyword}")
        pages = parser.search(keyword)

        for page in pages:
            logging.info(f"Parsing: {page['url']}")
            page_data = parser.parse(page["url"])

            contacts = extract_contacts(page_data.get("html", ""))

            sequence = generate_sequences(
                title=page_data.get("title", ""),
                description=page_data.get("description", ""),
                url=page["url"]
            )

            results.append({
                "articleUrl": page["url"],
                "title": page_data.get("title", ""),
                "description": page_data.get("description", ""),
                "emails": contacts.get("emails", []),
                "facebooks": contacts.get("facebooks", []),
                "linkedIns": contacts.get("linkedIns", []),
                "twitters": contacts.get("twitters", []),
                "sequence": sequence
            })

    export_results(results)
    logging.info("Scraper completed.")

if __name__ == "__main__":
    main()