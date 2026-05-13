import uuid

import flask
from flask import jsonify, make_response, request
from werkzeug.utils import secure_filename

from data import db_session
from data.event_object import Event


blueprint = flask.Blueprint(
    'event_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/events', methods=['GET', 'POST'])
def get_events():
    db_sess = db_session.create_session()

    if request.method == 'GET':
        try:
            events = db_sess.query(Event).all()

            return jsonify([item.to_dict() for item in events])
        except:
            return make_response(jsonify({'error': 'Couldn\'t connect to database'}), 500)


    if request.method == 'POST':
        try:
            event = Event()
            file = request.files['image']

            filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"

            file.save(f'data/img/events/{filename}')

            event.name = request.form['name']
            event.category = request.form['category']
            event.description = request.form['description']
            event.place = request.form['place']
            event.creator_id = request.form['creator_id']
            event.image_path = f'data/img/events/{filename}'
            event.start_date = request.form['start_date']
            event.end_date = request.form['end_date']

            db_sess.add(event)
            db_sess.commit()
        except:
            return make_response(jsonify({'error': 'Bad request'}), 400)
