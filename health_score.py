def calculate_health_score(final_report):
    if not final_report:
        return 0, "No Data"

    score = 100

    high_importance = ["HbA1c", "Creatinine", "eGFR", "LDL"]
    medium_importance = ["Hemoglobin", "WBC", "Platelets",
                         "Total Cholesterol", "Triglycerides",
                         "ALT", "AST"]

    for item in final_report:
        if item["status"] in ["Low", "High"]:

            if item["test"] in high_importance:
                score -= 10
            elif item["test"] in medium_importance:
                score -= 7
            else:
                score -= 4

    if score < 0:
        score = 0

    if score >= 85:
        risk = "Low Risk"
    elif score >= 65:
        risk = "Moderate Risk"
    else:
        risk = "High Risk"

    return score, risk