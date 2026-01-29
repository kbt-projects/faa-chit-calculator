from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows your frontend to call the backend

# -----------------------------
# Step 1: Define your formulas
# -----------------------------
def calculate_result(a, b, c):
    """
    Replace this function with your Excel logic.
    Example: Excel formula = (A + B) * C
    """
    # Example logic — replace with your own
    result = (a + b) * c
    return result

# -----------------------------
# Step 2: API endpoint
# -----------------------------
@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    # Extract inputs from JSON
    a = float(data.get("a", 0))
    b = float(data.get("b", 0))
    c = float(data.get("c", 1))  # default to 1 if missing

    # Call the formula function
    result = calculate_result(a, b, c)

    # Return as JSON
    return jsonify({"result": result})

@app.route("/", methods=["GET"])
def root():
    return "Backend is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
