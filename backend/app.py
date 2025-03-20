from flask import Flask, jsonify, request
from database import SessionLocal, engine, Base
from models import Employee, Shift
from scheduler import assign_shifts

app = Flask(__name__)

@app.route("/employees", methods=["GET"])
def get_employees():
    session = SessionLocal()
    employees = session.query(Employee).all()
    session.close()
    return jsonify([{"id": e.id, "name": e.name, "role": e.role} for e in employees])

@app.route("/shifts", methods=["GET"])
def get_shifts():
    session = SessionLocal()
    shifts = session.query(Shift).all()
    session.close()
    return jsonify([
        {"id": s.id, "day": s.day, "time": s.time, "role_needed": s.role_needed, "assigned_employee": s.assigned_employee.name if s.assigned_employee else None}
        for s in shifts
    ])

@app.route("/assign_shifts", methods=["POST"])
def trigger_assignment():
    assign_shifts()
    return jsonify({"message": "Shifts assigned successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
