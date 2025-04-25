from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Function to generate random vehicle data
def generate_vehicle_data():
    sample_names = ["John Doe", "Jane Smith", "Alice Brown", "Michael Scott", "Pam Beesly", "Dwight Schrute", "Jim Halpert", "Angela Martin", "Oscar Martinez", "Stanley Hudson"]
    phone_prefixes = ["987", "912", "998", "876", "981", "932", "855", "812", "799", "707"]
    states = ["KL", "MH", "DL", "KA", "TN", "AP", "UP", "RJ", "GJ", "WB"]

    def generate_vehicle_number():
        state = random.choice(states)
        district = f"{random.randint(1, 99):02}"
        series = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
        number = f"{random.randint(1000, 9999)}"
        return f"{state}{district}{series}{number}"

    def generate_phone_number():
        prefix = random.choice(phone_prefixes)
        suffix = f"{random.randint(1000000, 9999999)}"
        return prefix + suffix

    vehicles = []
    for _ in range(7):
        vehicle = {
            "vehicle_no": generate_vehicle_number(),
            "owner_name": random.choice(sample_names),
            "owner_phone": generate_phone_number(),
            "fine_amount": random.randint(100, 5000)  # Random fine amount between 100 and 5000
        }
        vehicles.append(vehicle)

    return vehicles

# Mock data (initial 3 entries + 500 generated entries)
vehicles = [
    {"vehicle_no": "KL01AB1234", "owner_name": "John Doe", "owner_phone": "9876543210", "fine_amount": 500},
    {"vehicle_no": "MH02CD5678", "owner_name": "Jane Smith", "owner_phone": "9123456789", "fine_amount": 1200},
    {"vehicle_no": "DL03EF9101", "owner_name": "Alice Brown", "owner_phone": "9988776655", "fine_amount": 300},
] + generate_vehicle_data()

@app.route("/")
def index():
    return render_template("index.html", vehicles=vehicles)

@app.route("/search", methods=["POST"])
def search_vehicle():
    search_query = request.form.get("search_query", "").strip()
    filtered_vehicles = [v for v in vehicles if search_query in v["vehicle_no"]]
    return render_template("index.html", vehicles=filtered_vehicles)

if __name__ == "__main__":
    app.run(debug=True)
