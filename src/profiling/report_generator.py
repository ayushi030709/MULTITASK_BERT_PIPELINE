"""
report_generator.py

Generates:
1. report.json
2. report.md

Directory Structure
-------------------
reports/
    dataset_name/
        report.json
        report.md
        plots/
"""

import json
from pathlib import Path


class ReportGenerator:

    def __init__(self, output_dir="reports"):

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    ####################################################################
    # JSON REPORT
    ####################################################################

    def save_json(self, dataset_name, report):

        dataset_dir = self.output_dir / dataset_name
        dataset_dir.mkdir(parents=True, exist_ok=True)

        json_path = dataset_dir / "report.json"

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4, ensure_ascii=False, default=str)

        return json_path

    ####################################################################
    # MARKDOWN REPORT
    ####################################################################

    def save_markdown(self, dataset_name, report):

        dataset_dir = self.output_dir / dataset_name
        dataset_dir.mkdir(parents=True, exist_ok=True)

        md_path = dataset_dir / "report.md"

        with open(md_path, "w", encoding="utf-8") as f:

            f.write(f"# Dataset Profiling Report\n\n")
            f.write(f"**Dataset:** `{dataset_name}`\n\n")

            ############################################################
            # DATASET INFORMATION
            ############################################################

            f.write("## Dataset Information\n\n")

            for split, info in report["dataset_information"].items():

                f.write(f"### {split}\n\n")
                f.write(f"- Rows: **{info['rows']}**\n")
                f.write(f"- Columns: **{info['num_columns']}**\n")
                f.write(f"- Column Names: {', '.join(info['columns'])}\n\n")

            ############################################################
            # TEXT STATS
            ############################################################

            f.write("---\n\n")
            f.write("## Text Statistics\n\n")

            for split, stats in report["text_statistics"].items():

                f.write(f"### {split}\n\n")

                for key, value in stats.items():
                    f.write(f"- {key}: **{value}**\n")

                f.write("\n")

            ############################################################
            # MISSING VALUES
            ############################################################

            f.write("---\n\n")
            f.write("## Missing Values\n\n")

            for split, values in report["missing_values"].items():

                f.write(f"### {split}\n\n")

                for column, count in values.items():
                    f.write(f"- {column}: {count}\n")

                f.write("\n")

            ############################################################
            # DUPLICATES
            ############################################################

            f.write("---\n\n")
            f.write("## Duplicate Rows\n\n")

            for split, value in report["duplicates"].items():
                f.write(f"- **{split}** : {value}\n")

            f.write("\n")

            ############################################################
            # LABEL DISTRIBUTION
            ############################################################

            f.write("---\n\n")
            f.write("## Label Distribution\n\n")

            for split, distribution in report["label_distribution"].items():

                f.write(f"### {split}\n\n")

                if len(distribution) == 0:

                    f.write("No label information found.\n\n")
                    continue

                for label, count in distribution.items():
                    f.write(f"- {label}: {count}\n")

                f.write("\n")

            ############################################################
            # RANDOM EXAMPLES
            ############################################################

            f.write("---\n\n")
            f.write("## Random Examples\n\n")

            for split, examples in report["random_examples"].items():

                f.write(f"### {split}\n\n")

                for i, example in enumerate(examples, start=1):

                    f.write(f"#### Example {i}\n\n")

                    for key, value in example.items():
                        f.write(f"- **{key}** : {value}\n")

                    f.write("\n")

        return md_path

    ####################################################################
    # GENERATE
    ####################################################################

    def generate(self, dataset_name, report):

        print(f"[INFO] Generating reports for {dataset_name}")

        json_path = self.save_json(dataset_name, report)
        md_path = self.save_markdown(dataset_name, report)

        print(f"[SUCCESS] JSON Report : {json_path}")
        print(f"[SUCCESS] Markdown Report : {md_path}")

        return {
            "json": str(json_path),
            "markdown": str(md_path)
        }