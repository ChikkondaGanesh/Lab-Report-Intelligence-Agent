import pdfplumber
import re

# Master alias dictionary
TEST_ALIASES = {
    "Hemoglobin": ["hemoglobin", "haemoglobin", "hb", "hgb", "h.b"],
    "WBC": ["wbc", "w.b.c", "white blood cells"],
    "RBC": ["rbc", "r.b.c", "red blood cells"],
    "Platelets": ["platelets", "platelet count"],
    "Hematocrit": ["hematocrit", "hct", "pcv", "p.c.v"],
    "MCV": ["mcv"],
    "MCH": ["mch"],
    "MCHC": ["mchc"],
    "RDW": ["rdw"],

    "Blood Sugar (Fasting)": [
        "fasting blood sugar", "fbs", "blood sugar fasting"
    ],
    "Blood Sugar (Random)": [
        "random blood sugar", "rbs", "blood sugar random"
    ],
    "HbA1c": ["hba1c", "hb a1c", "glycated hemoglobin"],

    "Total Cholesterol": ["total cholesterol", "cholesterol"],
    "LDL": ["ldl", "ldl cholesterol"],
    "HDL": ["hdl", "hdl cholesterol"],
    "Triglycerides": ["triglycerides", "tg"],

    "ALT": ["alt", "sgpt"],
    "AST": ["ast", "sgot"],
    "Bilirubin": ["bilirubin"],
    "Alkaline Phosphatase": ["alkaline phosphatase", "alp"],
    "Albumin": ["albumin"],

    "Creatinine": ["creatinine"],
    "Urea": ["urea", "bun"],
    "eGFR": ["egfr"],

    "Sodium": ["sodium", "na"],
    "Potassium": ["potassium", "k"],
    "Chloride": ["chloride", "cl"],
    "Calcium": ["calcium"],

    "TSH": ["tsh"],
    "T3": ["t3"],
    "T4": ["t4"],

    "CRP": ["crp", "c-reactive protein", "c.r.p"],
    "ESR": ["esr"],

    "Vitamin D": ["vitamin d", "vit d", "25-oh vitamin d"],
    "Vitamin B12": ["vitamin b12", "b12"],
    "Iron": ["iron"],
    "Ferritin": ["ferritin"]
}


def normalize_test_name(raw_name):
    raw_name = raw_name.lower().strip()

    # Remove dots and extra spaces
    raw_name = raw_name.replace(".", "")
    raw_name = re.sub(r"\s+", " ", raw_name)

    for standard_name, aliases in TEST_ALIASES.items():
        for alias in aliases:
            if alias in raw_name:
                return standard_name

    return None


def clean_number(value):
    value = value.replace(",", "")
    return float(value)


def parse_lab_report(pdf_path):
    parsed_data = []

    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    lines = text.split("\n")

    for line in lines:

        test_name = normalize_test_name(line)

        if test_name:

            # Split line AFTER test name
            parts = line.split(test_name, 1)

            if len(parts) > 1:
                after_name = parts[1]

                # Find numbers ONLY after test name
                numbers = re.findall(r"\d+\.?\d*", after_name)

                if numbers:
                    try:
                        value = float(numbers[0])
                        if "lakh" in after_name.lower():
                            value = value * 100000
                        parsed_data.append({
                            "test": test_name,
                            "value": value
                        })

                    except:
                        continue

    return parsed_data
    #......