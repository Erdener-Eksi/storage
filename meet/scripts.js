document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('meeting-form');
    const meetingList = document.getElementById('meeting-list');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const meeting = {
            topic: form.topic.value,
            date: form.date.value,
            startTime: form.startTime.value,
            endTime: form.endTime.value,
            participants: form.participants.value
        };

        await fetch('http://localhost:5000/api/meetings', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(meeting)
        });

        loadMeetings();
        form.reset();
    });

    async function loadMeetings() {
        const response = await fetch('http://localhost:5000/api/meetings');
        const meetings = await response.json();

        meetingList.innerHTML = '';
        meetings.forEach(meeting => {
            const li = document.createElement('li');
            li.textContent = `${meeting.topic} - ${meeting.date} ${meeting.startTime} - ${meeting.endTime}`;
            li.appendChild(createEditButton(meeting));
            li.appendChild(createDeleteButton(meeting.id));
            meetingList.appendChild(li);
        });
    }

    function createEditButton(meeting) {
        const button = document.createElement('button');
        button.textContent = 'Düzenle';
        button.addEventListener('click', () => {
            form.topic.value = meeting.topic;
            form.date.value = meeting.date;
            form.startTime.value = meeting.startTime;
            form.endTime.value = meeting.endTime;
            form.participants.value = meeting.participants;

            form.onsubmit = async (event) => {
                event.preventDefault();
                await fetch(`http://localhost:5000/api/meetings/${meeting.id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        topic: form.topic.value,
                        date: form.date.value,
                        startTime: form.startTime.value,
                        endTime: form.endTime.value,
                        participants: form.participants.value
                    })
                });
                form.reset();
                form.onsubmit = formSubmitHandler;
                loadMeetings();
            };
        });
        return button;
    }

    function createDeleteButton(id) {
        const button = document.createElement('button');
        button.textContent = 'Sil';
        button.addEventListener('click', async () => {
            await fetch(`http://localhost:5000/api/meetings/${id}`, {
                method: 'DELETE'
            });
            loadMeetings();
        });
        return button;
    }

    loadMeetings();
});
