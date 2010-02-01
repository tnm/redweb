<html>
 <head>

 <title>redweb</title>
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
  <script src="/static/vanadium-min.js" type="text/javascript"></script> 

  <link rel="stylesheet" type="text/css" href="/static/style.css" type="text/css" />

</head>

<body> 

<div class="sidebar">

<h2>Your Database Infobox</h2>
<br />
<h3>Last Returned Value: <strong>{{returned_value}}</strong></h3>
<hr />
<p>Database Size: <strong>{{db_size}}</strong></p>
<hr />
<p>All Keys:</p>

<p>
%for all_keys in all_keys:
<form name="key_delete" action="/delete/" method="post">
<input type="text" name="key_delete" value="{{all_keys}}" readonly  />
<input type="submit" value="Delete" />
</form>
%end
</p>

</div>


<div class="wrapper">
<div class="main">   
<h1 class = "red"> Welcome to redweb.</h1>

<p>ping your database | about | help </p>
</div>

<div class="main">     


    <h2>Strings</h2>
<hr />

    <form name="string_set" action="/strings/set/" method="post">
   
    <h3>Set a string value for a given key (SET)</h3> 
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /> 
       Value:<input type="text" name="value" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Set" />

    </form>
<hr />

    <form name="string_get" action="/strings/get/" method="post">
   
    <h3>Get a string value for a given key (GET)</h3> 
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    
    <input type="submit" class="submit_form" value="Get" />

    </form>

    </div>
   
    <div class="main">     
	
    <h2>Lists</h2>
    <hr />

    <form name="list_rightpush" action="/lists/rightpush/" method="post">
    
    <h3>Append element to the tail of a list (RPUSH)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Element:<input type="text" name="element" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Right Push" />

    </form>

    <hr />

    <form name="list_leftpush" action="/lists/leftpush/" method="post">

    <h3>Append element to the head of a list (LPUSH)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Element:<input type="text" name="element" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Left Push" />

    </form>

    </div>
   
    <div class="main">   
    <h2>Sets</h2>
    <hr />

    <form name="set_add" action="/sets/add/" method="post">

    <h3>Add a member to a set (SADD)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Add" />

    </form>
   
    <hr />

    <form name="set_remove" action="/sets/remove/" method="post">

    <h3>Remove a member to a set (SREM)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Remove" />

    </form>

    </div>

    <div class="main">   

    </div>
</div>

</div>

</body>
</html>


