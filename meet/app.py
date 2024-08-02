from flask_sanal  import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meetings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    startTime = db.Column(db.String(5), nullable=False)
    endTime = db.Column(db.String(5), nullable=False)
    participants = db.Column(db.String(255), nullable=False)

db.create_all()

@app.route('/api/meetings', methods=['POST'])
def add_meeting():
    data = request.get_json()
    new_meeting = Meeting(
        topic=data['topic'],
        date=data['date'],
        startTime=data['startTime'],
        endTime=data['endTime'],
        participants=data['participants']
    )
    db.session.add(new_meeting)
    db.session.commit()
    return jsonify({'message': 'Meeting added'}), 201

@app.route('/api/meetings', methods=['GET'])
def get_meetings():
    meetings = Meeting.query.all()
    return jsonify([{
        'id': meeting.id,
        'topic': meeting.topic,
        'date': meeting.date,
        'startTime': meeting.startTime,
        'endTime': meeting.endTime,
        'participants': meeting.participants
    } for meeting in meetings])

@app.route('/api/meetings/<int:id>', methods=['PUT'])
def update_meeting(id):
    data = request.get_json()
    meeting = Meeting.query.get(id)
    if not meeting:
        return jsonify({'message': 'Meeting not found'}), 404

    meeting.topic = data['topic']
    meeting.date = data['date']
    meeting.startTime = data['startTime']
    meeting.endTime = data['endTime']
    meeting.participants = data['participants']
    db.session.commit()
    return jsonify({'message': 'Meeting updated'})

@app.route('/api/meetings/<int:id>', methods=['DELETE'])
def delete_meeting(id):
    meeting = Meeting.query.get(id)
    if not meeting:
        return jsonify({'message': 'Meeting not found'}), 404

    db.session.delete(meeting)
    db.session.commit()
    return jsonify({'message': 'Meeting deleted'})

if __name__ == '__main__':
    app.run(debug=True)
