// CREATE FAMILY
$('#create-family').on('click', function () {
    $('#form-family').show();
})

$('#add-family').on('click', function (event) {
    event.preventDefault();
    $.ajax({
        url: "create-family/",
        type: "POST",
        data: {
            name: $('#family-name').val(),
        },
        success: function (json) {
            location.reload()
        },
    });

});


// UPDATE
$('.update-btn').on('click', function () {
    const id = $(this).val();
    $(`[data-id=${id}]`).show();
    console.log(id)
});

$('.update-save-btn').on('click', function (event) {
    event.preventDefault();

    const id = $(this).val();
    const values = {};
    const inputs = $(`[data-id=${id}] .update-form :input`);

    console.log(id)
    console.log(inputs)
    inputs.each(function (el) {
        values[el.name] = $(this).val();
    });


    $.ajax({
        url: "update/",
        type: "POST",
        data: {
            pk: id,
            name: $('#update-name'+id).val(),
            family: $('#update-family'+id).val(),
            healthy: $('#update-healthy'+id).val(),
            legs: $('#update-legs'+id).val(),
        },
        success: function () {
            location.reload();
        },
    });
});


// CREATE
$('#create-animal').on('click', function () {
    $('#form').show();
})

$('#add-animal').on('click', function (event) {
    event.preventDefault();
    $.ajax({
        url: "/",
        type: "POST",
        data: {
            name: $('#post-name').val(),
            family: $('#post-family').val(),
            healthy: $('#post-healthy').val(),
            legs: $('#post-legs').val(),
        },
        success: function (json) {
            location.reload()
        },
    });

});


// DELETE
$('.delete-animal').on('click', function () {
    const pk = $(this).val();
    $.ajax({
        url: "delete/",
        type: "POST",
        data: {
            pk: pk,
        },
        success: function () {
            location.reload()
        },
    });
})


// CLOSE BUTTONS
$('#b-d-c').on('click', function () {
    $('#form').hide();
})
$('.close').on('click', function () {
    $('.my-modal').hide();
})
$('#b-c-f').on('click', function () {
    $('#form-family').hide();
})