from flask import Blueprint, render_template, request
from pymongo import MongoClient
import json

with open('config.json', 'r') as config:
    db_connection = json.load(config)['db']

bp = Blueprint('lessons', __name__)

@bp.route('/lessons', methods=['GET', 'POST'])
def lessons():
    client = MongoClient(db_connection)
    
    if request.method == 'GET':
        lessons = client.lessons.lessons.find({})
        
        return render_template('lessons.html', lessons=lessons)
    
    elif request.method == 'POST':
        lsn = client.lessons.lessons.find_one({'$query':{},'$orderby':{'_id':-1}})
        id = 0 if not lsn else int(lsn['_id'])
        payload = request.get_json(force=True)
        client.lessons.lessons.insert_one({
            '_id': id+1,
            'name': f'{payload['name']}',
            'description': f'{payload['description']}',
            'content': f'{payload['content']}'
        })
        
        return '200'


@bp.route('/lessons/<lesson_id>', methods=['GET', 'POST'])
def concrete_lesson(lesson_id):
    client = MongoClient(db_connection)
    
    if request.method == 'GET':
        lesson = client.lessons.lessons.find_one({'_id': int(lesson_id)})
        
        return render_template('lesson.html', lesson=lesson)

    elif request.method == 'POST':
        client.lessons.lessons.delete_one({'_id': int(lesson_id)})
        
        return '200'