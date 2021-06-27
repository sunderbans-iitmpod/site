dayv = document.querySelector('#dayv')
hourv = document.querySelector('#hourv')
minv = document.querySelector('#minv')
secv = document.querySelector('#secv')
over = document.querySelector('#over')
dayt = document.querySelector('#dayt')
hourt = document.querySelector('#hourt')
mint = document.querySelector('#mint')
sect = document.querySelector('#sect')

function settime(){
  timenow = new Date()
  timethen = new Date('2021-07-01 23:59')
  ms = timethen - timenow
  if(ms > 0){
    sec = (ms/1000);
    min = sec / 60;
    sec %= 60;
    hour = min / 60;
    min %= 60;
    day = hour / 24;
    hour %= 24;
    dayv.innerHTML = Math.floor(day).toString().padStart(2,'0');
    hourv.innerHTML = Math.floor(hour).toString().padStart(2,'0');
    minv.innerHTML = Math.floor(min).toString().padStart(2,'0');
    secv.innerHTML = Math.floor(sec).toString().padStart(2,'0');
    over.style = "display:none"
  }
  else {
    dayt.style = "display:none"
    hourt.style = "display:none"
    mint.style = "display:none"
    sect.style = "display:none"
    over.style = "display:inline"
  }
}

settime()
setInterval(settime,1000)