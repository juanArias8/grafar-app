$(document).ready(function () {

    let plotContainer = document.getElementById('plotContainer');
    let progress = $(".progress");

    progress.hide(0);

    let functionField = "sin(x)+y^3";
    let aField = -6;
    let bField = 6;

    let data = buildJson(functionField, aField, bField);
    postFunction(data, plotContainer, progress);

    $("#formFunction").submit(function (event) {
            event.preventDefault();

            let functionField = $("#functionField").val();
            let aField = $("#aField").val();
            let bField = $("#bField").val();

            if (functionField !== "") {
                let data = buildJson(functionField, aField, bField);
                postFunction(data, plotContainer, progress);
            } else {
                M.toast({html: errorFields, classes: errorClasses});
            }
        }
    );
});

const errorResponse = 'Ha ocurrido un error, intenta con otra función o verifica que hayas ingresado los datos adecuados!';
const errorFields = 'Todos los campos son requeridos';
const errorClasses = 'rounded red lighten-2 black-text';
const infoClasses = 'rounded blue lighten-2 black-text';

function buildJson(functionField, aField, bField) {
    return JSON.stringify({
        "function": functionField,
        "a": aField,
        "b": bField
    });
}

function postFunction(data, plotContainer, progress) {
    $.ajax({
        type: "POST",
        url: "/function",
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        beforeSend: function () {
            Plotly.purge(plotContainer);
            progress.show(0);
        }
    }).done(function (response) {
        progress.hide(0);
        if (response.success === true) {
            if (response.type === 2) {
                buildGraph2d(response.message);
            } else if (response.type === 3) {
                buildGraph3d(response.message)
            } else {
                M.toast({html: errorResponse, classes: errorClasses});
            }
        } else {
            M.toast({html: errorResponse, classes: errorClasses});
        }
    }).fail(function (data) {
        M.toast({html: data, classes: infoClasses});
    });
}

function buildGraph2d(message) {
    let plotContainer = document.getElementById('plotContainer');
    let data = {};

    try {
        data = {
            x: JSON.parse(message.x),
            y: JSON.parse(message.y)
        };
    } catch (e) {
        M.toast({html: errorResponse, classes: errorClasses}, 4000);
    }

    Plotly.plot(plotContainer, [data]);
}

function buildGraph3d(message) {
    let plotContainer = document.getElementById('plotContainer');
    let data = {};

    try {
        data = {
            x: JSON.parse(message.x),
            y: JSON.parse(message.y),
            z: JSON.parse(message.z),
            type: 'surface'
        };
    } catch (e) {
        M.toast({html: errorResponse, classes: errorClasses}, 4000);
    }

    Plotly.plot(plotContainer, [data]);
}