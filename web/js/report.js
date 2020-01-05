function reqReport(){
    var data = JSON.stringify({
              "date": document.getElementById('dateField').value
          });
  
          alert(data)
  
          var url = "http://localhost:5000"
          var endpoint = "/GetReport"
          var replyObj
  
          var http = new XMLHttpRequest();
  
          http.open("POST", url + endpoint);
          http.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
  
          http.onreadystatechange = function () {
              var DONE = 4;       // 4 means that the request is done
              var OK = 200;       // 200 means a successful return
  
              if (http.readyState == DONE && http.status == OK && http.responseText) {
                  // JSON string
                  alert('in ready state')
                  replyString = http.responseText;
                  alert(replyString)
                  document.getElementById('testReturn').append(replyString)              }
          }
          http.send(data);
  
  }