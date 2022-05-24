var showTime = document.getElementById('clickme')
var showDisplay = document.getElementById('demo')
showTime.onclick = function () {
    showDisplay.innerHTML = Date();
}