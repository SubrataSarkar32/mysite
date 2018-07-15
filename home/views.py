from django.template import Template, Context
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    t = Template('''<!DOCTYPE html>
<html>
<head>
<style>
* {
    box-sizing: border-box;
}

body {
    font-family: Arial;
    padding: 10px;
    background: White;
}

/* Header/Blog Title */
.header {
    padding: 30px;
    text-align: center;
    background: white;
}

.header h1 {
    font-size: 50px;
    color: White;

}

/* Style the top navigation bar */
.topnav {
    overflow: hidden;
    background-color: #333;
}

/* Style the topnav links */
.topnav a {
    float: left;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

/* Change color on hover */
.topnav a:hover {
    background-color: #ddd;
    color: black;
}

/* Create two unequal columns that floats next to each other */
/* Left column */
.leftcolumn {
    float: left;
    width: 75%;
    background-color: White;
}

/* Right column */
.rightcolumn {
    float: left;
    width: 25%;
    background-color: White;
    padding-left: 20px;
}

/* Fake image */
.fakeimg {
    background-color: #aaa;
    width: 100%;
    padding: 20px;
}

/* Add a card effect for articles */
.card {
    background-color: white;
    padding: 20px;
    margin-top: 20px;
}

/* Clear floats after the columns */
.row:after {
    content: "";
    display: table;
    clear: both;
}

/* Footer */
.footer {
    padding: 20px;
    text-align: center;
    background: #ddd;
    margin-top: 20px;
}

/* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 800px) {
    .leftcolumn, .rightcolumn {
        width: 100%;
        padding: 0;
    }
}

/* Responsive layout - when the screen is less than 400px wide, make the navigation links stack on top of each other instead of next to each other */
@media screen and (max-width: 400px) {
    .topnav a {
        float: none;
        width: 100%;
    }
}
</style>
<script>
function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}
</script>
</head>
<body onload="startTime()">

<div class="header" style="background: YellowGreen;">
  <h1>Alice Assistant</h1>
  <p style="color:White;">Home</p>
</div>

<div class="topnav">
  <a href="http://subratasarkar32.pythonanywhere.com/home">Home</a>
  <a href="http://subratasarkar32.pythonanywhere.com/admin">Admin</a>
  <a href="http://subratasarkar32.pythonanywhere.com/polls">Poll</a>
  <a href="#" >Link</a>
  <a href="#" style="float:right">{{ current_date| date:"D d M Y" }}<div id="txt"></div></a>
</div>

<div class="row">
  <div class="leftcolumn">
    <div class="card" style="background-color:Gold;color: White;">
      <h2>ALICE</h2>
      <h5>Your assistant this semester   Jul 9, 2018</h5>
      <div class="fakeimg" style="height:200px;">Image</div>
      <p>Image Description</p>
      <p>ALICE is your friend throughout your hard and sweet times in your college life. Alice is a digital assistant that aims to make your semester more planned and composed. You will have options to enter details of subjects you have and your reading frequency of these subject on a daily basis.Based on Machine Learning , Alice would recommend which subject to read and for how much period of time.
      </p>
    </div>
    <div class="card" style="background-color:Gold;color: White;">
      <h2>How Alice came into being...</h2>
      <h5>Your assistant this semester   Jul 9, 2018</h5>
      <div class="fakeimg" style="height:200px;">Image</div>
      <p>Image Description</p>
      <p>We have all faced that moment in our lives when we forgot about an assignment or exam and we end up preparing just the previous day. It was this thing that inspired us to make Alice. Though we don't garuntee Alice will complete those things for you(this might become a feature some time in distant future), but we are sure it won't fail reminding you of those things that need your attention right now.</p>
    </div>
  </div>
  <div class="rightcolumn">
  <div class="card" style="background-color: Violet;color: White;">
      <h2>About Us</h2>
      <div class="fakeimg" style="height:100px;">Image</div>
      <p>We are a group of inquisitive and explorative Undergrad CS students who takes pride for their passion in their subject.Group members:
      <ul>Pratyusha Singha</ul>
      <ul>Rashed Mehdi</ul>
      <ul>Saranya Naha Roy</ul>
      <ul>Soumya Mukherjee</ul>
      <ul>Subrata Sarkar</ul>
      Alice is our first project .This project is still in early stages with only 2 versions till now and a lot of bug fixes.
      It will soon be released under open source license.
      Alice is primarily written in C and Python with planned releases for linux and android with Jython and Cython integration .
      As of now ,Alice is available as a stand-alone application for desktop systems.</p>
    </div>
    <div class="card" style="background-color: Violet;color: White;">
      <h3>Alice screenshot</h3>
      <div class="fakeimg"><p>Image</p></div>
      <div class="fakeimg"><p>Image</p></div>
      <div class="fakeimg"><p>Image</p></div>
    </div>
    <div class="card" style="background-color: Violet;color: White;">
      <h3>Follow Alice</h3>
      <p><h3>Follow Alice on <a href="https://plus.google.com/u/0/101251349428109708954">Google+</a>.</h3></p>
    </div>
  </div>
</div>

<div class="footer" style="background-color:Tomato; color:White;">
  <h4><a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Alice</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://plus.google.com/u/0/101251349428109708954" property="cc:attributionName" rel="cc:attributionURL">Alice Devs</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.<br />Permissions beyond the scope of this license may be available at <a xmlns:cc="http://creativecommons.org/ns#" href="https://plus.google.com/u/0/101251349428109708954" rel="cc:morePermissions">https://plus.google.com/u/0/101251349428109708954</a>.</h4>
</div>

</body>
</html>
''')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)