thonimport json
from pathlib import Path
import logging

def export_results(results):
    output_dir = Path(__file__).resolve().parents[2] / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "output.sample.json"

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    logging.info(f"Results exported to {output_path}")