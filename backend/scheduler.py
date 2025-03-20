from database import SessionLocal
from models import Employee, Shift

def assign_shifts():
    session = SessionLocal()
    shifts = session.query(Shift).filter(Shift.assigned_employee_id == None).all()
    employees = session.query(Employee).all()

    for shift in shifts:
        available_employees = [
            e for e in employees 
            if shift.role_needed == e.role and shift.day in e.availability
        ]
        
        if available_employees:
            assigned = available_employees[0]  # Sélection du premier employé dispo
            shift.assigned_employee_id = assigned.id
            session.commit()

    session.close()