function button() {
  var topic = document.getElementById("topicInput").value;
  var oReq = new XMLHttpRequest();
  oReq.addEventListener("load", requestDone);
  oReq.open("GET", "http://captionmasterapi.antonpaqu.in/quote?word=" + topic);
  oReq.send();
}

function requestDone() {
  document.getElementById("quote").innerText = this.responseText;
}
