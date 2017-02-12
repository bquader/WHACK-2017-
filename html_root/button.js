function button() {
  var topic = document.getElementById("topicInput").value;
  var oReq = new XMLHttpRequest();
  oReq.addEventListener("load", requestDone);
  oReq.open("GET", "http://captionmasterapi.antonpaqu.in/quote?word=" + topic);
  oReq.send();
}

function requestDone() {
  var data = JSON.parse(this.responseText);
  document.getElementById("quote").innerText = data[0][0].replace(/&amp;/g, '&');
  document.getElementById("author").innerText = data[0][1];
}
