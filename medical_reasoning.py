import json
from rag.rag_engine import get_rag_response

with open("knowledge/icd_mapping.json") as f:
    ICD_DATA = json.load(f)

with open("knowledge/diet_recommendations.json") as f:
    DIET_DATA = json.load(f)


def generate_medical_report(final_report):

    abnormal = [i for i in final_report if i["status"] in ["Low", "High"]]

    if not abnormal:
        return "All values are within normal range."

    full_report = ""

    for test in abnormal:

        key = f"{test['status']} {test['test']}"

        explanation = get_rag_response(key)

        disease_info = ICD_DATA.get(key, {})
        diet_info = DIET_DATA.get(key, [])

        full_report += f"\n🔎 {test['test']} ({test['status']})\n"
        full_report += explanation + "\n"

        if disease_info:
            full_report += f"\nPossible Condition: {disease_info['disease']}"
            full_report += f"\nICD‑10 Code: {disease_info['icd_code']}\n"

        if diet_info:
            full_report += "\nLifestyle Suggestions:\n"
            for d in diet_info:
                full_report += f"- {d}\n"

        full_report += "\n-----------------------------\n"

    return full_report
    #...