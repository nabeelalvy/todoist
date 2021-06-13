function done(id) {
    $.ajax({
        url: '/todoit/done/',
        type: 'POST',
        data: {
            'task_id': id
        },
        dataType: 'json',
        success: function (data) {
            if (data) {
                alert(data['task']);
            }
        }
    });
    location.reload();
}