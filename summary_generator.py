def generate_summary(final_report, score, risk):

    abnormal_tests = [t for t in final_report if t["status"] in ["Low", "High"]]

    if not abnormal_tests:
        return (
            "Good news! 🎉\n\n"
            "All your test results are within the healthy range.\n"
            "This means your body indicators are looking stable right now.\n\n"
            "To keep it that way:\n"
            "• Eat balanced meals\n"
            "• Stay active\n"
            "• Drink enough water\n"
            "• Get proper sleep\n\n"
            f"Your Overall Health Score is {score}/100 ({risk})."
        )

    summary = []
    summary.append("Here’s what your report means in simple terms:\n")

    for test in abnormal_tests:
        name = test["test"]
        status = test["status"]

        if name in ["Hemoglobin", "RBC", "Hematocrit"]:
            message = (
                f"• Your {name} level is {status.lower()}. "
                "This may make you feel tired or low on energy because your blood "
                "might not be carrying oxygen efficiently.\n"
            )

        elif name == "WBC":
            message = (
                f"• Your {name} level is {status.lower()}. "
                "This usually means your body could be fighting an infection or stress.\n"
            )

        elif name in ["Blood Sugar (Fasting)", "Blood Sugar (Random)", "HbA1c"]:
            message = (
                f"• Your blood sugar level is {status.lower()}. "
                "If it stays high for a long time, it can increase the risk of diabetes. "
                "Simple changes in food and daily activity can help manage this.\n"
            )

        elif name in ["Total Cholesterol", "LDL", "HDL", "Triglycerides"]:
            message = (
                f"• Your {name} level is {status.lower()}. "
                "This can affect heart health over time if not managed properly.\n"
            )

        elif name in ["ALT", "AST", "Bilirubin"]:
            message = (
                f"• Your {name} level is {status.lower()}. "
                "This might mean your liver is slightly stressed.\n"
            )

        elif name in ["Creatinine", "Urea", "eGFR"]:
            message = (
                f"• Your {name} level is {status.lower()}. "
                "This may suggest your kidneys need a little extra care.\n"
            )

        elif name in ["Vitamin D", "Vitamin B12", "Iron", "Ferritin"]:
            message = (
                f"• Your {name} level is {status.lower()}. "
                "Low levels can sometimes make you feel weak or tired.\n"
            )

        else:
            message = (
                f"• Your {name} result is {status.lower()}. "
                "It would be good to monitor this and maintain a healthy lifestyle.\n"
            )

        summary.append(message)

    summary.append(
        "\nWhat you can do next:\n"
        "• Focus on healthy home-cooked meals\n"
        "• Include fruits and vegetables daily\n"
        "• Exercise at least 30 minutes a day\n"
        "• Reduce junk and sugary foods\n"
        "• Stay hydrated\n"
    )

    summary.append(
        f"\nYour Overall Health Score is {score}/100 ({risk}).\n"
        "This score gives a general idea of your health and does not replace medical advice."
    )

    return "\n".join(summary)
    #..