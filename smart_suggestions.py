from unicodedata import category

products = [
    {
        "name": "Plastic Toothbrush",
        "category": "toiletries",
        "eco_score": 32,
        "packaging": "plastic",
        "transport": "imported",
        "certifications": []
    },
    {
        "name": "Bamboo Toothbrush",
        "category": "toiletries",
        "eco_score": 87,
        "packaging": "biodegradable",
        "transport": "local",
        "certifications": ["B Corp"]
    },
    {
        "name": "Organic Soap Bar",
        "category": "toiletries",
        "eco_score": 80,
        "packaging": "paper",
        "transport": "local",
        "certifications": ["FSC"]
    },
    {
        "name": "Imported Body Wash",
        "category": "toiletries",
        "eco_score": 40,
        "packaging": "plastic",
        "transport": "imported",
        "certifications": []
    }
]

def suggest_better_product(input_product):
    category=input_product["category"]
    score= input_product["eco_score"]

    #find products in same category with better score
    alternatives=[
        p for p in products
        if p["category"]==category and p["eco_score"]>score
    ]

    #sort by highest eco score
    alternatives.sort(key=lambda x: x["eco_score"], reverse=True)

    if not alternatives:
        return "No better alternative found.", None

    best=alternatives[0]

    #reasoning logic
    reasons=[]
    if best["packaging"]!=input_product["packaging"]:
        reasons.append(f"better packaging ({best['packaging']})")
    if best["transport"]!=input_product["transport"]:
        reasons.append(f"shorter transport ({best['transport']})")
    if len(best["certifications"])>len(input_product["certifications"]):
        reasons.append("more certifications")

    reason_text="Improved because of: " + ", ".join(reasons)

    return reason_text, best

if __name__ == "__main__":
    input_product={
        "name": "Plastic Toothbrush",
        "category": "toiletries",
        "eco_score": 32,
        "packaging": "plastic",
        "transport": "imported",
        "certifications": []
    }

    reason, suggestion = suggest_better_product(input_product)

    if suggestion:
        print(f"Suggested Product: {suggestion['name']} (Score: {suggestion['eco_score']})")
        print(reason)
    else:
        print(reason)