function displayTime() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
  
    document.getElementById("time").innerHTML = 
      (hours < 10 ? "0" : "") + hours + ":" + 
      (minutes < 10 ? "0" : "") + minutes + ":" + 
      (seconds < 10 ? "0" : "") + seconds;
  }
  
  setInterval(displayTime, 1000);
  