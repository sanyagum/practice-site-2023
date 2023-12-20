function deleteUser() {
    const input = document.querySelector('input[name="user"]').value;
    alert(`Пользователь ${input} удален!`);
}

function deleteLesson() {
    const id = document.querySelector('input[name="lessonId"]').value;
    fetch(`/lessons/${id}`, {
        method: 'POST',
        body: JSON.stringify({
            id: id,
        })
    }).then(()=>alert(`Учебный материал с id "${id}" удален`));
}

function createLesson() {
    const lessonName = document.querySelector('input[name="lessonName"]').value;
    const lessonDesc = document.querySelector('input[name="lessonDesc"]').value;
    const lessonContent = document.querySelector('textarea[name="lessonContent"]').value;
    fetch('/lessons', {
        method: 'POST',
        body: JSON.stringify({
            name: lessonName,
            description: lessonDesc,
            content: lessonContent,
        })
    }).then(()=>alert(`Учебный материал "${lessonName}" создан`));
}