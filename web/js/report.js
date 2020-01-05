
function reqReport(){
var data = JSON.stringify({
            "date": document.getElementById('dateField').value
        });

        alert(data)

        var url = "http://localhost:5000"
        var endpoint = "/GetReport"

        var http = new XMLHttpRequest();

        http.open("POST", url + endpoint);
        http.responseType = "blob"
        http.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');

        http.onload = function () {


            // JSON string

                // replyString = http.responseText;
                // console.log(replyString)

                // replyObj = JSON.parse(replyString)
                // var data = replyObj.teams
                // console.log(data)
                // element = document.getElementById("testReturn")

                var blob = http.response
                console.log(blob.size)
                var link = document.createElement('a')
                console.log(link)
                var docSrc = window.URL.createObjectURL(blob)
            
                var iframe = document.createElement('element')
                iframe.src = docSrc
                document.getElementById('iframeCont').append(iframe)
            
                link.href = docSrc
                link.download="report.docx"
                link.click()
            
        }
        http.send(data);
}

function createDoc(){

}