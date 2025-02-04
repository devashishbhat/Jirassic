from flask import Blueprint, jsonify, request
from services.user_services import register_user_service, login_user_service, get_user_task, generate_task_and_save

user_bp = Blueprint('user', __name__)

@user_bp.route('/health-check', methods=['GET'])
def health_checl():
    return jsonify({"message": "User route Status-200"})

@user_bp.route("/register", methods=['POST'])
async def register_user():
    userObject = request.get_json()
    return await register_user_service(userObject)

@user_bp.route("/login", methods=['POST'])
async def login_user():
    user_data = request.get_json()
    return await login_user_service(user_data)

@user_bp.route("/get-task", methods=['GET'])
async def get_task_db():
    user_id = request.args.get('userId')
    return await get_user_task(user_id)

# @user_bp.route("/generate-tasks", methods=['POST'])
# async def task_generator():
#     generatedTranscript = request.get_json()
#     return await generate_task_and_save(generatedTranscript)

@user_bp.route("/generate-tasks", methods=['POST'])
async def task_generator():
    print("Generate tasks endpoint hit")
    user_data = request.get_json()
    print(f"Generate tasks data: {user_data}")
    # Temporarily return a simple response for testing
    # return jsonify({"message": "Tasks generated successfully"}), 200
    return await generate_task_and_save(user_data)

