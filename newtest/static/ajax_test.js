function submit() {
    axios.get('/ajax/input/', {
            params: {
                input: $("#name").val()
            }
        })
        .then(function (response) {
            // handle success
            console.log(response);
            $("#output").html(response.data);
            $("#output").show();
        })
        .catch(function (error) {
            // handle error
            console.log(error);
            alert(error);
        });
}

function init() {
    $("#submit").click(function () {
        submit();
    });
    $("#output").hide();
}

$(function () {
    init();
});