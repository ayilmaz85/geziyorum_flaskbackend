from flask import Blueprint, jsonify
from geziyorum.models import Employees, User


apiEmployees = Blueprint("apiEmployees", __name__, url_prefix="/api/employees")


@apiEmployees.route("/")
def employees():
    try:
        allUsers = Employees.get_all_employees()
        users = []

        for user in allUsers:
            print(user)
            users.append(
                {
                    "id": user.EMPLOYEE_ID,
                    "username": user.FIRST_NAME,
                    "email": user.LAST_NAME,
                    "password": user.EMAIL,
                }
            )

        return jsonify({"success": True, "data": users, "count": len(users)})
    except Exception as e:
        # print("ERROR in users: ", e)
        return jsonify({"success": False, "message": "There is an error.."})

    # PHONE_NUMBER = db.Column(db.String)
    # HIRE_DATE = db.Column(db.String)
    # JOB_ID = db.Column(db.String)
    # SALARY = db.Column(db.String)
    # COMMISSION_PCT = db.Column(db.String)
    # MANAGER_ID = db.Column(db.String)
    # DEPARTMENT_ID = db.Column(db.String)
