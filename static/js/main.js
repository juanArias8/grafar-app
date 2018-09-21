$(document).ready(function () {

    let plotContainer = document.getElementById('plotContainer');
    let progress = $(".progress");

    progress.hide(0);

    $("#formFunction").submit(function (event) {
            event.preventDefault();

            let functionField = $("#functionField").val();
            let aField = $("#aField").val();
            let bField = $("#bField").val();

            if (functionField !== "") {
                let data = JSON.stringify({
                    "function": functionField,
                    "a": aField,
                    "b": bField
                });
                $.ajax({
                    type: "POST",
                    url: "/function",
                    data: data,
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    beforeSend: function () {
                        Plotly.purge(plotContainer);
                        progress.show("slow");
                    }
                }).done(function (response) {
                    progress.hide(0);
                    if (response.success === true) {
                        if (response.type === 2) {
                            buildGraph2d(response.message);
                        } else if (response.type === 3) {
                            buildGraph3d(response.message)
                        } else {
                            console.log("Error")
                        }
                    } else {
                        console.log("Error")
                    }
                }).fail(function (data) {
                    console.log(data)
                });
            } else {
                Materialize.toast(
                    'Todos los campos son requerridos!',
                    3000,
                    'rounded'
                );
            }
        }
    );
});


function buildGraph2d(message) {
    let plotContainer = document.getElementById('plotContainer');
    let data = {
        x: JSON.parse(message.x),
        y: JSON.parse(message.y)
    };

    Plotly.plot(plotContainer, [data]);
}

function buildGraph3d(message) {
    let plotContainer = document.getElementById('plotContainer');
    let data = {
        x: JSON.parse(message.x),
        y: JSON.parse(message.y),
        z: JSON.parse(message.z),
        type: 'surface'
    };

    Plotly.plot(plotContainer, [data]);
}