from flask import jsonify, request, Blueprint
from .models import Task

api_bp = Blueprint('api', __name__)

@api_bp.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.get_all()
    return jsonify([task.to_dict() for task in tasks])

@api_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = Task.create(title=data['title'], description=data.get('description'))
    return jsonify(task.to_dict()), 201

@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict())

@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.update(title=data.get('title'), description=data.get('description'), done=data.get('done'))
    return jsonify(task.to_dict())

@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.delete()
    return '', 204