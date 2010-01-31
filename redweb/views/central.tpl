<html>
 <head>

 <title>redweb</title>
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
  <script src="/static/vanadium-min.js" type="text/javascript"></script> 

  <link rel="stylesheet" type="text/css" href="/static/style.css" type="text/css" />

</head>

<body> 

<div class="wrapper">

<div class="main">     
    <p>number of keys: {{db_size}} </p>

    <h2>Strings</h2>

    <form name="string_set" action="/strings/set/" method="post">
   
    <h3>set a string value for a given key (SET):</h3> 
    <p>Key:</p>
    <p><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    
    <p>Value:</p>
    <p><input type="text" name="value" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Set" />

    </form>

    <form name="string_get" action="/strings/get/" method="post">
   
    <h3>get a string value for a given key (GET):</h3> 
    <p>Key:</p>
    <p><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    
    <input type="submit" class="submit_form" value="Get" />

    </form>

    <hr />
	
    <h2>Lists</h2>

    <form name="list_rightpush" action="/lists/rightpush/" method="post">
    
    <h3>append element to the tail of a list (RPUSH)</h3>
    <p>Key:</p>
    <p><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    
    <p>Element:</p>
    <p><input type="text" name="element" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Right Push" />

    </form>

    <hr />

    <form name="list_leftpush" action="/lists/leftpush/" method="post">

    <h3>append element to the head of a list (LPUSH)</h3>
    <p>Key:</p>
    <p><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    
    <p>Element</p>
    <p><input type="text" name="element" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Left Push" />

    </form>

    <hr />

    <h2>Sets</h2>

    <form name="set_add" action="/sets/add/" method="post">

    <h3>add a member to a set (SADD)</h3>
    <p>Key:</p>
    <p><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    
    <p>Member</p>
    <p><input type="text" name="member" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Add" />

    </form>
   
    <hr />

    <form name="set_remove" action="/sets/remove/" method="post">

    <h3>remove a member to a set (SREM)</h3>
    <p>Key:</p>
    <p><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    
    <p>Member</p>
    <p><input type="text" name="member" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Remove" />

    </form>




   



</div>

</div>

</body>
</html>


