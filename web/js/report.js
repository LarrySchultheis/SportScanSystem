
$(document).ready(function(){

    var input = $('#dateField')[0]  //document.getElementById("dateField")
    console.log(input)
    input.addEventListener("keyup", function(event){
        if (event.keyCode === 13){
            $('#submitBtn').click()
        }
    })
})

function reqReport(){
var data = JSON.stringify({
            "date": document.getElementById('dateField').value
        });

        var url = "http://localhost:5000"
        var endpoint = "/GetReport"

        var http = new XMLHttpRequest();

        http.open("POST", url + endpoint);
        http.responseType = "blob"
        http.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        http.setRequestHeader('Cache-Control', 'no-cache')

        http.onload = function () {

            var blob = http.response
            //console.log(http.getAllResponseHeaders());
            var fileName = http.getResponseHeader('Content-Disposition')
            fileName = fileName.replace('attachment; filename=', '')
            console.log(fileName);
            //console.log(http);
            //console.log(blob)
            var link = document.createElement('a')
            //console.log(link)
            link.href = window.URL.createObjectURL(blob)

            link.download=fileName
            link.click()
            
        }
        http.send(data);
}
