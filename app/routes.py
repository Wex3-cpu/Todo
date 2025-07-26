from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Todo
from app import db
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    todo_list = Todo.query.order_by(Todo.created_at).all()
    return render_template('index.html', todo_list=todo_list)

@bp.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    description = request.form.get('description')
    new_todo = Todo(title=title, description=description, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit.html', todo=todo)

@bp.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.index'))