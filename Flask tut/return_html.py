<!DOCTYPE html>
<!-- saved from url=(0056)https://www.tutorialspoint.com/flask/flask_templates.htm -->
<html style="" class="js no-touch csstransforms3d csstransitions gr__tutorialspoint_com"><!--<![endif]--><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<!-- Basic -->

<title>Flask Templates</title>
<meta name="description" content="Flask Templates - Learn Flask in simple and easy steps starting from basic to advanced concepts with examples including Overview, Environment, Application, Routing, Variable Rules, URL Building, HTTP Methods, Templates, Static Files, Request Object, Sending Form Data to Template, Cookies, Sessions, Redirect and Errors, Message Flashing, File Uploading, Extensions, Mail, WTF, SQLite, SQLAlchemy, Sijax, Deployment, FastCGI.">
<meta name="keywords" content="Flask, Tutorial, Overview, Environment, Application, Routing, Variable Rules, URL Building, HTTP Methods, Templates, Static Files, Request Object, Sending Form Data to Template, Cookies, Sessions, Redirect and Errors, Message Flashing, File Uploading, Extensions, Mail, WTF, SQLite, SQLAlchemy, Sijax, Deployment, FastCGI.">
<!--<base href="https://www.tutorialspoint.com/">--><base href=".">
<link rel="shortcut icon" href="https://www.tutorialspoint.com/favicon.ico" type="image/x-icon">
<meta name="viewport" content="width=device-width,initial-scale=1.0,user-scalable=yes">
<meta property="og:locale" content="en_US">
<meta property="og:type" content="website">
<meta property="fb:app_id" content="471319149685276">
<meta property="og:site_name" content="www.tutorialspoint.com">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="author" content="tutorialspoint.com">
<script src="./return_html_files/osd.js.download"></script><script src="./return_html_files/ca-pub-7133395778201029.js.download"></script><script type="text/javascript" src="./return_html_files/script-min-v4.js.download"></script>
<link rel="stylesheet" href="./return_html_files/style-min.css">
<script>
function openNav() {	
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("right_obs").style.display = "block";
}
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("right_obs").style.display = "none";
}
function close_obs_sidenav(){
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("right_obs").style.display = "none";
}
</script>
<!-- Head Libs -->
<!--[if IE 8]>
<link rel="stylesheet" type="text/css" href="/theme/css/ie8.css">
<![endif]-->
<style>
#privacy-banner {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    max-width: 100%;
    padding: 1rem .5rem;
    background: #fff;
    z-index: 1030;
    color: #000;
    font-size: 14px;
    margin: 0;
    display: none;
    border-top: 2px solid rgb(130, 130, 130);
  }
  #privacy-banner p {
    margin: 0;
    color: #000;
    text-align: center;
  }
  #privacy-banner a {
    text-decoration: none;
    margin: 20px auto 0 auto;
    display: block;
    max-width: 150px;
  }
  #privacy-banner a:hover {
    text-decoration: underline;
  }
  #banner-learn {
    color: #000;
  }
  #banner-accept {
    padding: 7px 15px;
    color: #fff;
    border-radius: 5px;
    background:#737373 !important;
  }
  @media (min-width: 768px) {
    #privacy-banner {
      padding: 1.5rem .5rem;
    }
    #privacy-banner a {
      display: inline-block;
      margin: 0 10px;
    }
}
select{ border:0 !important; outline: 1px inset black !important; outline-offset: -1px !important; }
.btnsbmt{ background: #3fa783 !important;}
ul.nav-list.primary>li a.videolink{    background: none; margin: 0px; padding: 0px; border: 1px solid #d6d6d6;}
div.feature-box div.feature-box-icon, .col-md-3 .course-box, li.heading, div.footer-copyright { background: #3fa783 url(/images/pattern.png) repeat center center !important;}
.sub-main-menu .sub-menuu div:hover, .sub-main-menu .viewall, header nav ul.nav-main li a:hover, button.btn-responsive-nav, header div.search button.btn-default { background: #3fa783 !important;}
.submenu-item{ border-bottom: 2px solid #3fa783 !important; border-top: 2px solid #3fa783 !important }
.ace_scroller{overflow: auto!important;}
a.demo{font-family: "Open Sans",Arial,sans-serif; background:#3fa783; color:#fff; font-size:13px; padding:3px 10px; border:1px solid #d6d6d6; position:absolute; right:5px; margin:-6px 17px 0px 0px;}
a.demo:hover{opacity:.8}
</style>
<script>
$(document).ready(function() {
  $('input[name="q"]').keydown(function(event){
    if(event.keyCode == 13) {
      event.preventDefault();
      return false;
    }
  });
});
</script>
<link rel="preload" href="./return_html_files/f(5).txt" as="script"><script type="text/javascript" src="./return_html_files/f(5).txt"></script><link rel="preload" href="./return_html_files/f(6).txt" as="script"><script type="text/javascript" src="./return_html_files/f(6).txt"></script><link rel="preload" href="https://pagead2.googlesyndication.com/pagead/js/r20190522/r20190131/show_ads_impl.js" as="script"></head>
<body onload="prettyPrint()" data-gr-c-s-loaded="true" style="">
<div class="wrapLoader">
   <div class="imgLoader">
      <img src="./return_html_files/loading-cg.gif" alt="" width="70" height="70">
   </div>
</div>
<div id="right_obs" class="display-none" onclick="close_obs_sidenav()"></div>
<header>
   <div class="container">			
      <h1 class="logo">
      <a href="https://www.tutorialspoint.com/index.htm" title="tutorialspoint">
      <img alt="tutorialspoint" src="./return_html_files/logo.png">
      </a>
      </h1>			
      <ul class="tp-inline-block pull-right" id="tp-head-icons">
        <li>
           <div class="tp-second-nav tp-display-none tp-pointer" onclick="openNav()">
              <i class="fa fa-th-large fa-lg"></i>
           </div>
        </li>
     </ul>
     <button class="btn btn-responsive-nav btn-inverse" data-toggle="collapse" data-target=".nav-main-collapse" id="pull" style="top: 1665.199951171875px!important"> <i class="icon icon-bars"></i> </button>
      <nav>
         <ul class="nav nav-pills nav-top">
            <li><a href="https://www.tutorialspoint.com/about/about_careers.htm" style="background: #fffb09; font-weight: bold;"><i class="icon icon-suitcase"></i> Jobs</a></li>
            <li> <a target="_blank" href="https://www.tutorialspoint.com/programming_examples/"><i class="fa fa-cubes"></i> &nbsp;Examples</a> </li>
            <li> <a href="https://www.tutorialspoint.com/whiteboard.htm"><img src="./return_html_files/image-editor.png" alt="Whiteboard" title="Whiteboard"> &nbsp;Whiteboard</a> </li>
            <li> <a href="https://www.tutorialspoint.com/netmeeting.php"><i class="fa-camera"></i> &nbsp;Net Meeting</a> </li>
            <li> <a href="https://www.tutorialspoint.com/online_dev_tools.htm"> <i class="dev-tools-menu" style="opacity:.5"></i> Tools </a> </li>
            <li> <a href="https://www.tutorialspoint.com/articles/index.php"><i class="icon icon-file-text-o"></i> &nbsp;Articles</a> </li>            
            <li class="top-icons">
              <ul class="social-icons">
              <li class="facebook"><a href="https://www.facebook.com/tutorialspointindia" target="_blank" rel="nofollow" data-placement="bottom" title="tutorialspoint @ Facebook">Facebook</a></li>
              <li class="googleplus"><a href="https://plus.google.com/u/0/116678774017490391259/posts" target="_blank" rel="nofollow" data-placement="bottom" title="tutorialspoint @ Google+">Google+</a></li>
              <li class="twitter"><a href="https://www.twitter.com/tutorialspoint" target="_blank" rel="nofollow" data-placement="bottom" title="tutorialspoint @ Twitter">Twitter</a></li>
              <li class="linkedin"><a href="https://www.linkedin.com/company/tutorialspoint" target="_blank" rel="nofollow" data-placement="bottom" title="tutorialspoint @ Linkedin">Linkedin</a></li>
              <li class="youtube"><a href="https://www.youtube.com/channel/UCVLbzhxVTiTLiVKeGV7WEBg" target="_blank" rel="nofollow" data-placement="bottom" title="tutorialspoint YouTube">YouTube</a></li>
              </ul>
           </li>
         </ul>
      </nav>
    </div>
     <div class="sidenav" id="mySidenav">
     <div class="navbar nav-main">
      <div class="container">
         <nav class="nav-main mega-menu">
            <ul class="nav nav-pills nav-main" id="mainMenu">
               <li class="dropdown no-sub-menu"> <a class="dropdown" href="https://www.tutorialspoint.com/index.htm"><i class="icon icon-home"></i> Home</a> </li>   
               <li class="dropdown no-sub-menu"><a class="dropdown" href="https://www.tutorialspoint.com/questions/index.php"><i class="fa fa-send"></i> Q/A </a> </li>
               <li class="dropdown"><a class="dropdown" href="https://www.tutorialspoint.com/tutorialslibrary.htm"><span class="tut-lib"> Library </span></a></li>
               <li class="dropdown no-sub-menu"><a class="dropdown" href="https://www.tutorialspoint.com/videotutorials/index.htm"><i class="fa-toggle-right"></i> Videos </a></li>
               <li class="dropdown no-sub-menu"><a class="dropdown" href="https://www.tutorialspoint.com/tutor_connect/index.php"><i class="fa-user"> </i> Tutors</a></li>
               <li class="dropdown no-sub-menu"><a class="dropdown" href="https://www.tutorialspoint.com/codingground.htm"><i class="fa-code"></i> Coding Ground </a> </li>
               <li class="dropdown no-sub-menu"><a class="dropdown" href="https://store.tutorialspoint.com/"><i class="fa-usd"></i> Store </a> </li>
               <li class="dropdown no-sub-menu">
                  <div class="searchform-popup">
                     <input class="header-search-box" type="text" id="search-string" name="q" placeholder="Search your favorite tutorials..." onfocus="if (this.value == &#39;Search your favorite tutorials...&#39;) {this.value = &#39;&#39;;}" onblur="if (this.value == &#39;&#39;) {this.value = &#39;Search your favorite tutorials...&#39;;}" autocomplete="off" style="">
                     <div class="magnifying-glass"><i class="icon-search"></i> Search </div>
                 </div>
               </li>
            </ul>
         </nav>
        </div>
      </div>	
     </div>	
   	
</header>
<div style="clear:both;"></div>
<div role="main" class="main">
<div class="container">
<div class="row">
<div class="col-md-2">
<aside class="sidebar">
<style>
.ts{
   vertical-align:middle !important;
   text-align:center !important;   
}
</style>
<div class="mini-logo">
<img src="./return_html_files/flask-mini-logo.jpg" alt="Flask Tutorial">
</div>
<ul class="nav nav-list primary left-menu">
<li><a class="videolink" href="https://www.tutorialspoint.com/flask_framework_online_training/index.asp" target="_blank"><img src="./return_html_files/flask-video-tutorials.jpg" alt="Flask Video Tutorials"></a></li>
</ul>
<ul class="nav nav-list primary left-menu">
<li class="heading">Flask Tutorial</li>
<li><a href="https://www.tutorialspoint.com/flask/index.htm">Flask - Home</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_overview.htm">Flask - Overview</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_environment.htm">Flask - Environment</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_application.htm">Flask - Application</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_routing.htm">Flask - Routing</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_variable_rules.htm">Flask - Variable Rules</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_url_building.htm">Flask - URL Building</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_http_methods.htm">Flask - HTTP Methods</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_templates.htm" style="background-color: rgb(214, 214, 214);">Flask - Templates</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_static_files.htm">Flask - Static Files</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_request_object.htm">Flask - Request Object</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_sending_form_data_to_template.htm">Sending Form Data to Template</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_cookies.htm">Flask - Cookies</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_sessions.htm">Flask - Sessions</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_redirect_and_errors.htm">Flask - Redirect &amp; Errors</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_message_flashing.htm">Flask - Message Flashing</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_file_uploading.htm">Flask - File Uploading</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_extensions.htm">Flask - Extensions</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_mail.htm">Flask - Mail</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_wtf.htm">Flask - WTF</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_sqlite.htm">Flask - SQLite</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm">Flask - SQLAlchemy</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_sijax.htm">Flask - Sijax</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_deployment.htm">Flask - Deployment</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_fastcgi.htm">Flask - FastCGI</a></li>
</ul>
<ul class="nav nav-list primary left-menu">
<li class="heading">Flask Useful Resources</li>
<li><a href="https://www.tutorialspoint.com/flask/flask_quick_guide.htm">Flask - Quick Guide</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_useful_resources.htm">Flask - Useful Resources</a></li>
<li><a href="https://www.tutorialspoint.com/flask/flask_discussion.htm">Flask - Discussion</a></li>
</ul>
<ul class="nav nav-list primary push-bottom left-menu special">
<li class="sreading">Selected Reading</li>
<li><a target="_top" href="https://www.tutorialspoint.com/upsc_ias_exams.htm">UPSC IAS Exams Notes</a></li>
<li><a target="_top" href="https://www.tutorialspoint.com/developers_best_practices/index.htm">Developer's Best Practices</a></li>
<li><a target="_top" href="https://www.tutorialspoint.com/questions_and_answers.htm">Questions and Answers</a></li>
<li><a target="_top" href="https://www.tutorialspoint.com/effective_resume_writing.htm">Effective Resume Writing</a></li>
<li><a target="_top" href="https://www.tutorialspoint.com/hr_interview_questions/index.htm">HR Interview Questions</a></li>
<li><a target="_top" href="https://www.tutorialspoint.com/computer_glossary.htm">Computer Glossary</a></li>
<li><a target="_top" href="https://www.tutorialspoint.com/computer_whoiswho.htm">Who is Who</a></li>
</ul>
</aside>
</div>
<!-- PRINTING STARTS HERE -->
<div class="row">
<div class="content">
<div class="col-md-7 middle-col">
<h1>Flask – Templates</h1>
<hr>
<div style="padding-bottom:5px;padding-left:10px;text-align: center;">Advertisements</div>
<div style="text-align: center;">
<script type="text/javascript"><!--
google_ad_client = "pub-7133395778201029";
var width = document.getElementsByClassName("middle-col")[0].clientWidth - 15;
google_ad_width = width;
google_ad_height = 150;
google_ad_format = width + "x150_as";
google_ad_type = "image";
google_ad_channel = "";
//--></script>
<script type="text/javascript" src="./return_html_files/f(7).txt"> 
</script><ins id="aswift_0_expand" style="display:inline-table;border:none;height:150px;margin:0;padding:0;position:relative;visibility:visible;width:599px;background-color:transparent;"><ins id="aswift_0_anchor" style="display:block;border:none;height:150px;margin:0;padding:0;position:relative;visibility:visible;width:599px;background-color:transparent;"><iframe width="599" height="150" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0px;width:599px;height:150px;" src="./return_html_files/saved_resource(3).html"></iframe></ins></ins>
</div>
<hr>
<div class="pre-btn">
<a href="https://www.tutorialspoint.com/flask/flask_http_methods.htm"><i class="icon icon-arrow-circle-o-left big-font"></i> Previous Page</a>
</div>
<div class="nxt-btn">
<a href="https://www.tutorialspoint.com/flask/flask_static_files.htm">Next Page <i class="icon icon-arrow-circle-o-right big-font"></i>&nbsp;</a>
</div>
<div class="clearer"></div>
<hr>
<p>It is possible to return the output of a function bound to a certain URL in the form of HTML. For instance, in the following script, <b>hello()</b> function will render <b>‘Hello World’</b> with <b>&lt;h1&gt;</b> tag attached to it.</p>
<pre class="prettyprint notranslate prettyprinted" style=""><span class="kwd">from</span><span class="pln"> flask </span><span class="kwd">import</span><span class="pln"> </span><span class="typ">Flask</span><span class="pln">
app </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Flask</span><span class="pun">(</span><span class="pln">__name__</span><span class="pun">)</span><span class="pln">

</span><span class="lit">@app</span><span class="pun">.</span><span class="pln">route</span><span class="pun">(</span><span class="str">'/'</span><span class="pun">)</span><span class="pln">
</span><span class="kwd">def</span><span class="pln"> index</span><span class="pun">():</span><span class="pln">
   </span><span class="kwd">return</span><span class="pln"> </span><span class="str">'&lt;html&gt;&lt;body&gt;&lt;h1&gt;Hello World&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;'</span><span class="pln">

</span><span class="kwd">if</span><span class="pln"> __name__ </span><span class="pun">==</span><span class="pln"> </span><span class="str">'__main__'</span><span class="pun">:</span><span class="pln">
   app</span><span class="pun">.</span><span class="pln">run</span><span class="pun">(</span><span class="pln">debug </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">True</span><span class="pun">)</span></pre>
<p>However, generating HTML content from Python code is cumbersome, especially when variable data and Python language elements like conditionals or loops need to be put. This would require frequent escaping from HTML.</p>
<p>This is where one can take advantage of <b>Jinja2</b> template engine, on which Flask is based. Instead of returning hardcode HTML from the function, a HTML file can be rendered by the <b>render_template()</b> function.</p>
<pre class="prettyprint notranslate prettyprinted" style=""><span class="kwd">from</span><span class="pln"> flask </span><span class="kwd">import</span><span class="pln"> </span><span class="typ">Flask</span><span class="pln">
app </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Flask</span><span class="pun">(</span><span class="pln">__name__</span><span class="pun">)</span><span class="pln">

</span><span class="lit">@app</span><span class="pun">.</span><span class="pln">route</span><span class="pun">(</span><span class="str">'/'</span><span class="pun">)</span><span class="pln">
</span><span class="kwd">def</span><span class="pln"> index</span><span class="pun">():</span><span class="pln">
   </span><span class="kwd">return</span><span class="pln"> render_template</span><span class="pun">(‘</span><span class="pln">hello</span><span class="pun">.</span><span class="pln">html</span><span class="pun">’)</span><span class="pln">

</span><span class="kwd">if</span><span class="pln"> __name__ </span><span class="pun">==</span><span class="pln"> </span><span class="str">'__main__'</span><span class="pun">:</span><span class="pln">
   app</span><span class="pun">.</span><span class="pln">run</span><span class="pun">(</span><span class="pln">debug </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">True</span><span class="pun">)</span></pre>
<p>Flask will try to find the HTML file in the templates folder, in the same folder in which this script is present.</p>
<ul class="list">
<li>Application folder
<ul class="list">
<li>Hello.py</li>
<li>templates
<ul class="list">
<li>hello.html</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The term <b>‘web templating system’</b> refers to designing an HTML script in which the variable data can be inserted dynamically. A web template system comprises of a template engine, some kind of data source and a template processor.</p>
<p>Flask uses <b>jinga2</b> template engine. A web template contains HTML syntax interspersed placeholders for variables and expressions (in these case Python expressions) which are replaced values when the template is rendered.</p>
<p>The following code is saved as <b>hello.html</b> in the templates folder.</p>
<pre class="prettyprint notranslate prettyprinted" style=""><span class="dec">&lt;!doctype html&gt;</span><span class="pln">
</span><span class="tag">&lt;html&gt;</span><span class="pln">
   </span><span class="tag">&lt;body&gt;</span><span class="pln">
   
      </span><span class="tag">&lt;h1&gt;</span><span class="pln">Hello {{ name }}!</span><span class="tag">&lt;/h1&gt;</span><span class="pln">
      
   </span><span class="tag">&lt;/body&gt;</span><span class="pln">
</span><span class="tag">&lt;/html&gt;</span></pre>
<p>Next, run the following script from Python shell.</p>
<pre class="prettyprint notranslate prettyprinted" style=""><span class="kwd">from</span><span class="pln"> flask </span><span class="kwd">import</span><span class="pln"> </span><span class="typ">Flask</span><span class="pun">,</span><span class="pln"> render_template
app </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Flask</span><span class="pun">(</span><span class="pln">__name__</span><span class="pun">)</span><span class="pln">

</span><span class="lit">@app</span><span class="pun">.</span><span class="pln">route</span><span class="pun">(</span><span class="str">'/hello/&lt;user&gt;'</span><span class="pun">)</span><span class="pln">
</span><span class="kwd">def</span><span class="pln"> hello_name</span><span class="pun">(</span><span class="pln">user</span><span class="pun">):</span><span class="pln">
   </span><span class="kwd">return</span><span class="pln"> render_template</span><span class="pun">(</span><span class="str">'hello.html'</span><span class="pun">,</span><span class="pln"> name </span><span class="pun">=</span><span class="pln"> user</span><span class="pun">)</span><span class="pln">

</span><span class="kwd">if</span><span class="pln"> __name__ </span><span class="pun">==</span><span class="pln"> </span><span class="str">'__main__'</span><span class="pun">:</span><span class="pln">
   app</span><span class="pun">.</span><span class="pln">run</span><span class="pun">(</span><span class="pln">debug </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">True</span><span class="pun">)</span></pre>
<p>As the development server starts running, open the browser and enter URL as − <b>http://localhost:5000/hello/mvl</b></p>
<p>The <b>variable</b> part of URL is inserted at <b>{{ name }}</b> place holder.</p>
<img src="./return_html_files/web_templating_system_example.jpg" alt="Web Templating System Example">
<p>The <b>Jinga2</b> template engine uses the following delimiters for escaping from HTML.</p>
<ul class="list">
<li>{% ... %} for Statements</li>
<li>{{ ... }} for Expressions to print to the template output</li>
<li>{# ... #} for Comments not included in the template output</li>
<li># ... ## for Line Statements</li>
</ul>
<p>In the following example, use of conditional statement in the template is demonstrated. The URL rule to the <b>hello()</b> function accepts the integer parameter. It is passed to the <b>hello.html</b> template. Inside it, the value of number received (marks) is compared (greater or less than 50) and accordingly HTML is conditionally rendered.</p>
<p>The Python Script is as follows −</p>
<pre class="prettyprint notranslate prettyprinted" style=""><span class="kwd">from</span><span class="pln"> flask </span><span class="kwd">import</span><span class="pln"> </span><span class="typ">Flask</span><span class="pun">,</span><span class="pln"> render_template
app </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Flask</span><span class="pun">(</span><span class="pln">__name__</span><span class="pun">)</span><span class="pln">

</span><span class="lit">@app</span><span class="pun">.</span><span class="pln">route</span><span class="pun">(</span><span class="str">'/hello/&lt;int:score&gt;'</span><span class="pun">)</span><span class="pln">
</span><span class="kwd">def</span><span class="pln"> hello_name</span><span class="pun">(</span><span class="pln">score</span><span class="pun">):</span><span class="pln">
   </span><span class="kwd">return</span><span class="pln"> render_template</span><span class="pun">(</span><span class="str">'hello.html'</span><span class="pun">,</span><span class="pln"> marks </span><span class="pun">=</span><span class="pln"> score</span><span class="pun">)</span><span class="pln">

</span><span class="kwd">if</span><span class="pln"> __name__ </span><span class="pun">==</span><span class="pln"> </span><span class="str">'__main__'</span><span class="pun">:</span><span class="pln">
   app</span><span class="pun">.</span><span class="pln">run</span><span class="pun">(</span><span class="pln">debug </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">True</span><span class="pun">)</span></pre>
<p>HTML template script of <b>hello.html</b> is as follows −</p>
<pre class="prettyprint notranslate prettyprinted" style=""><span class="dec">&lt;!doctype html&gt;</span><span class="pln">
</span><span class="tag">&lt;html&gt;</span><span class="pln">
   </span><span class="tag">&lt;body&gt;</span><span class="pln">
      {% if marks&gt;50 %}
         </span><span class="tag">&lt;h1&gt;</span><span class="pln"> Your result is pass!</span><span class="tag">&lt;/h1&gt;</span><span class="pln">
      {% else %}
         </span><span class="tag">&lt;h1&gt;</span><span class="pln">Your result is fail</span><span class="tag">&lt;/h1&gt;</span><span class="pln">
      {% endif %}
   </span><span class="tag">&lt;/body&gt;</span><span class="pln">
</span><span class="tag">&lt;/html&gt;</span></pre>
<p>Note that the conditional statements <b>if-else</b> and <b>endif</b> are enclosed in delimiter <b>{%..%}</b>.</p>
<p>Run the Python script and visit URL <b>http://localhost/hello/60</b> and then <b>http://localhost/hello/30</b> to see the output of HTML changing conditionally.</p>
<p>The Python loop constructs can also be employed inside the template. In the following script, the <b>result()</b> function sends a dictionary object to template <b>results.html</b> when URL <b>http://localhost:5000/result</b> is opened in the browser.</p>
<p>The Template part of <b>result.html</b> employs a <b>for loop</b> to render key and value pairs of dictionary object <b>result{}</b> as cells of an HTML table.</p>
<p>Run the following code from Python shell.</p>
<pre class="prettyprint notranslate prettyprinted" style=""><span class="kwd">from</span><span class="pln"> flask </span><span class="kwd">import</span><span class="pln"> </span><span class="typ">Flask</span><span class="pun">,</span><span class="pln"> render_template
app </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Flask</span><span class="pun">(</span><span class="pln">__name__</span><span class="pun">)</span><span class="pln">

</span><span class="lit">@app</span><span class="pun">.</span><span class="pln">route</span><span class="pun">(</span><span class="str">'/result'</span><span class="pun">)</span><span class="pln">
</span><span class="kwd">def</span><span class="pln"> result</span><span class="pun">():</span><span class="pln">
   dict </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="str">'phy'</span><span class="pun">:</span><span class="lit">50</span><span class="pun">,</span><span class="str">'che'</span><span class="pun">:</span><span class="lit">60</span><span class="pun">,</span><span class="str">'maths'</span><span class="pun">:</span><span class="lit">70</span><span class="pun">}</span><span class="pln">
   </span><span class="kwd">return</span><span class="pln"> render_template</span><span class="pun">(</span><span class="str">'result.html'</span><span class="pun">,</span><span class="pln"> result </span><span class="pun">=</span><span class="pln"> dict</span><span class="pun">)</span><span class="pln">

</span><span class="kwd">if</span><span class="pln"> __name__ </span><span class="pun">==</span><span class="pln"> </span><span class="str">'__main__'</span><span class="pun">:</span><span class="pln">
   app</span><span class="pun">.</span><span class="pln">run</span><span class="pun">(</span><span class="pln">debug </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">True</span><span class="pun">)</span></pre>
<p>Save the following HTML script as <b>result.html</b> in the templates folder.</p>
<pre class="prettyprint notranslate prettyprinted" style=""><span class="dec">&lt;!doctype html&gt;</span><span class="pln">
</span><span class="tag">&lt;html&gt;</span><span class="pln">
   </span><span class="tag">&lt;body&gt;</span><span class="pln">
      </span><span class="tag">&lt;table</span><span class="pln"> </span><span class="atn">border</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="atv">1</span><span class="tag">&gt;</span><span class="pln">
         {% for key, value in result.iteritems() %}
            </span><span class="tag">&lt;tr&gt;</span><span class="pln">
               </span><span class="tag">&lt;th&gt;</span><span class="pln"> {{ key }} </span><span class="tag">&lt;/th&gt;</span><span class="pln">
               </span><span class="tag">&lt;td&gt;</span><span class="pln"> {{ value }} </span><span class="tag">&lt;/td&gt;</span><span class="pln">
            </span><span class="tag">&lt;/tr&gt;</span><span class="pln">
         {% endfor %}
      </span><span class="tag">&lt;/table&gt;</span><span class="pln">
   </span><span class="tag">&lt;/body&gt;</span><span class="pln">
</span><span class="tag">&lt;/html&gt;</span></pre>
<p>Here, again the Python statements corresponding to the <b>For</b> loop are enclosed in {%..%} whereas, the expressions <b>key and value</b> are put inside <b>{{ }}</b>.</p>
<p>After the development starts running, open <b>http://localhost:5000/result</b> in the browser to get the following output.</p>
<img src="./return_html_files/table_template_example.jpg" alt="Table Template Example">
<hr>
<div class="pre-btn">
<a href="https://www.tutorialspoint.com/flask/flask_http_methods.htm"><i class="icon icon-arrow-circle-o-left big-font"></i> Previous Page</a>
</div>
<div class="print-btn center">
<a href="https://www.tutorialspoint.com/cgi-bin/printpage.cgi" target="_blank"><i class="icon icon-print big-font"></i> Print</a>
</div>
<div class="nxt-btn">
<a href="https://www.tutorialspoint.com/flask/flask_static_files.htm">Next Page <i class="icon icon-arrow-circle-o-right big-font"></i>&nbsp;</a>
</div>
<hr>
<!-- PRINTING ENDS HERE -->
<div class="bottomgooglead">
<div class="bottomadtag">Advertisements</div>
<script><!--
var width = 580;
var height = 400;
var format = "580x400_as";
if( window.innerWidth < 468 ){
   width = 300;
   height = 250;
   format = "300x250_as";
}
google_ad_client = "pub-7133395778201029";
google_ad_width = width;
google_ad_height = height;
google_ad_format = format;
google_ad_type = "image";
google_ad_channel ="";
//--></script>
<script src="./return_html_files/f(7).txt">
</script><ins id="aswift_1_expand" style="display:inline-table;border:none;height:400px;margin:0;padding:0;position:relative;visibility:visible;width:580px;background-color:transparent;"><ins id="aswift_1_anchor" style="display:block;border:none;height:400px;margin:0;padding:0;position:relative;visibility:visible;width:580px;background-color:transparent;"><iframe width="580" height="400" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_1" name="aswift_1" style="left:0;position:absolute;top:0;border:0px;width:580px;height:400px;" src="./return_html_files/saved_resource(4).html"></iframe></ins></ins>
</div>
</div>
</div>
<div class="row">
<div class="col-md-3" id="rightbar">
<div class="simple-ad">
<a href="javascript:void(0)" onclick="var sTop = window.screen.height/2-(218); var sLeft = window.screen.width/2-(313);window.open(&#39;https://www.facebook.com/sharer.php?u=&#39; + &#39;https://www.tutorialspoint.com/flask/flask_templates.htm&#39;,&#39;sharer&#39;,&#39;toolbar=0,status=0,width=626,height=456,top=&#39;+sTop+&#39;,left=&#39;+sLeft);return false;">
<img src="./return_html_files/facebookIcon.jpg" alt="img">
</a>
<a href="javascript:void(0)" onclick="var sTop = window.screen.height/2-(218); var sLeft = window.screen.width/2-(313);window.open(&#39;https://twitter.com/share?url=&#39; + &#39;https://www.tutorialspoint.com/flask/flask_templates.htm&#39;,&#39;sharer&#39;,&#39;toolbar=0,status=0,width=626,height=456,top=&#39;+sTop+&#39;,left=&#39;+sLeft);return false;">
<img src="./return_html_files/twitterIcon.jpg" alt="img">
</a>
<a href="javascript:void(0)" onclick="var sTop = window.screen.height/2-(218); var sLeft = window.screen.width/2-(313);window.open(&#39;https://www.linkedin.com/cws/share?url=&#39; + &#39;https://www.tutorialspoint.com/flask/flask_templates.htm&amp;title=&#39;+ document.title,&#39;sharer&#39;,&#39;toolbar=0,status=0,width=626,height=456,top=&#39;+sTop+&#39;,left=&#39;+sLeft);return false;">
<img src="./return_html_files/linkedinIcon.jpg" alt="img">
</a>
<a href="javascript:void(0)" onclick="var sTop = window.screen.height/2-(218); var sLeft = window.screen.width/2-(313);window.open(&#39;https://plus.google.com/share?url=https://www.tutorialspoint.com/flask/flask_templates.htm&#39;,&#39;sharer&#39;,&#39;toolbar=0,status=0,width=626,height=456,top=&#39;+sTop+&#39;,left=&#39;+sLeft);return false;">
<img src="./return_html_files/googlePlusIcon.jpg" alt="img">
</a>
<a href="javascript:void(0)" onclick="var sTop = window.screen.height/2-(218); var sLeft = window.screen.width/2-(313);window.open(&#39;https://www.stumbleupon.com/submit?url=https://www.tutorialspoint.com/flask/flask_templates.htm&amp;title=&#39;+ document.title,&#39;sharer&#39;,&#39;toolbar=0,status=0,width=626,height=456,top=&#39;+sTop+&#39;,left=&#39;+sLeft);return false;">
<img src="./return_html_files/StumbleUponIcon.jpg" alt="img">
</a>
<a href="javascript:void(0)" onclick="var sTop = window.screen.height/2-(218); var sLeft = window.screen.width/2-(313);window.open(&#39;https://reddit.com/submit?url=https://www.tutorialspoint.com/flask/flask_templates.htm&amp;title=&#39;+ document.title,&#39;sharer&#39;,&#39;toolbar=0,status=0,width=626,height=656,top=&#39;+sTop+&#39;,left=&#39;+sLeft);return false;">
<img src="./return_html_files/reddit.jpg" alt="img">
</a>
</div>
<div class="rightgooglead">
<script><!--
google_ad_client = "pub-2537027957187252";
/* Right Side Ad */
google_ad_slot = "right_side_ad";
google_ad_width = 300;
google_ad_height = 250;
//--></script>
<script src="./return_html_files/f(7).txt">
</script><ins id="aswift_2_expand" style="display:inline-table;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;" data-ad-slot="right_side_ad"><ins id="aswift_2_anchor" style="display:block;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;"><iframe width="300" height="250" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_2" name="aswift_2" style="left:0;position:absolute;top:0;border:0px;width:300px;height:250px;" src="./return_html_files/saved_resource(5).html"></iframe></ins></ins>
</div>
<div class="rightgooglead">
<script><!--
google_ad_client = "pub-7133395778201029";
google_ad_width = 300;
google_ad_height = 600;
google_ad_format = "300x600_as";
google_ad_type = "image";
google_ad_channel ="";
//--></script>
<script src="./return_html_files/f(7).txt">
</script><ins id="aswift_3_expand" style="display:inline-table;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;"><ins id="aswift_3_anchor" style="display:block;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;"><iframe width="300" height="600" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_3" name="aswift_3" style="left:0;position:absolute;top:0;border:0px;width:300px;height:600px;" src="./return_html_files/saved_resource(6).html"></iframe></ins></ins>
</div>
<div class="rightgooglead">
<script><!--
google_ad_client = "pub-2537027957187252";
/* Right Side Ad */
google_ad_slot = "right_side_ad";
google_ad_width = 300;
google_ad_height = 250;
//-->
</script>
<script src="./return_html_files/f(7).txt">
</script><ins id="aswift_4_expand" style="display:inline-table;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;" data-ad-slot="right_side_ad"><ins id="aswift_4_anchor" style="display:block;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:300px;background-color:transparent;"><iframe width="300" height="250" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_4" name="aswift_4" style="left:0;position:absolute;top:0;border:0px;width:300px;height:250px;" src="./return_html_files/saved_resource(7).html"></iframe></ins></ins>
</div>
</div>
</div>
</div>
</div>
</div>

<div class="footer-copyright">
<div class="container">
<div class="row">
<div class="col-md-1">
<a href="https://www.tutorialspoint.com/index.htm" class="logo"> <img alt="Tutorials Point" class="img-responsive" src="./return_html_files/logo-footer.png"> </a>
</div>
<div class="col-md-4 col-sm-12 col-xs-12">
   <nav id="sub-menu">
      <ul>
         <li><a href="https://www.tutorialspoint.com/about/about_privacy.htm">Privacy Policy</a></li>
         <li><a href="https://www.tutorialspoint.com/about/about_cookies.htm">Cookies Policy</a></li>
         <li><a href="https://www.tutorialspoint.com/about/contact_us.htm">Contact</a></li>
      </ul>
   </nav>
</div>
<div class="col-md-3 col-sm-12 col-xs-12">
<p>© Copyright 2019. All Rights Reserved.</p>
</div>
<div class="col-md-4 col-sm-12 col-xs-12">
   <div class="news-group">
      <input type="text" class="form-control-foot search" name="textemail" id="textemail" autocomplete="off" placeholder="Enter email for newsletter" onfocus="if (this.value == &#39;Enter email for newsletter...&#39;) {this.value = &#39;&#39;;}" onblur="if (this.value == &#39;&#39;) {this.value = &#39;Enter email for newsletter...&#39;;}">
      <span class="input-group-btn"> <button class="btn btn-default btn-footer" id="btnemail" type="submit" onclick="javascript:void(0);">go</button> </span>
      <div id="newsresponse"></div>
   </div>
</div>
</div>
</div>
</div>
</div>
<div id="privacy-banner" style="display: inherit;">
  <div>
    <p>
      We use cookies to provide and improve our services. By using our site, you consent to our Cookies Policy.
      <a id="banner-accept" href="javascript:void(0)">Accept</a>
      <a id="banner-learn" href="https://www.tutorialspoint.com/about/about_cookies.htm" target="_blank">Learn more</a>
    </p>
  </div>
</div>
<script>
// Banner Trigger if Not Closed
if (!localStorage.bannerClosed) {
  document.getElementById('privacy-banner').style.display = "inherit";
} else {
  document.getElementById('privacy-banner').style.display = "none";
}
document.getElementById('banner-accept').addEventListener('click', function() {
  document.getElementById('privacy-banner').style.display = "none";
  localStorage.bannerClosed = 'true';
});
if (navigator.userAgent.match(/Opera|OPR\//)) {
  document.getElementById('privacy-banner').style.display = "inherit";
}
</script>
<!-- Libs -->
<script src="./return_html_files/custom-min.js.download"></script><a class="scroll-to-top visible" href="https://www.tutorialspoint.com/#" id="scrollToTop"><i class="icon icon-chevron-up icon-white"></i></a>
<script src="./return_html_files/urchin.js.download">
</script>
<script>
_uacct = "UA-232293-6";
urchinTracker();
$('.pg-icon').click(function(){
   $('.wrapLoader').show();
});
</script>



<div class="autocomplete-suggestions " style="top: 1717.2px; left: 0px; width: 0px;"></div><iframe id="google_osd_static_frame_997237304774" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;" src="./return_html_files/saved_resource(8).html"></iframe></body><iframe id="google_shimpl" style="display: none;" src="./return_html_files/saved_resource(9).html"></iframe><iframe id="google_esf" name="google_esf" src="./return_html_files/zrt_lookup.html" data-ad-client="ca-pub-7133395778201029" style="display: none;"></iframe></html>