from flask import Flask, request, jsonify
from smart_suggestions import suggest_better_product

app = Flask(__name__)

@app.route("/score", methods=["POST"])
def score_product():
    data = request.json
    packaging = data.get("packaging")
    transport = data.get("transport")
    certifications = data.get("certifications", [])

    score = 0
    if packaging == "biodegradable":
        score += 40
    elif packaging == "recyclable":
        score += 20
    if transport == "local":
        score += 30
    if "FSC" in certifications or "Fair Trade" in certifications:
        score += 30

    return jsonify({"eco_score": min(score, 100)})

# ✅ MOVE THIS ABOVE app.run
@app.route("/suggest", methods=["POST"])
def suggest():
    data = request.json
    reason, suggestion = suggest_better_product(data)
    return jsonify({
        "suggestion": suggestion,
        "reason": reason
    })

# ✅ Entry point at the end
if __name__ == "__main__":
    app.run(debug=True)