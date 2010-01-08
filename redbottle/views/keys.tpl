<html>
 <head>

 <title>{{title}}</title>
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
  <script src="/static/vanadium-min.js" type="text/javascript"></script> 

  <link rel="stylesheet" type="text/css" href="/static/style.css" type="text/css" />

</head>

<body> 

<div class="wrapper">

<div class="main">     

    <form name="input" action="/keyvalue/add/" method="post">
   
    <h2>Add a Key-Value to the Redis Store</h2> 
    <p>Key:</p>
    <p><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    
    <p>Value:</p>
    <p><input type="text" name="value" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Add" />

    </form>

<hr />

    <form name="input2" action="/keyvalue/delete/" method="post">
    
    <h2>Delete a key:</h2>
    <p><input type="text" input class=":required :only_on_submit input_form" name="key_delete" /></p>

    <input type="submit" class="submit_form" value="Delete" />

    </form>

<hr />

     <h2>All keys:</h2>
     <p>Number of keys in store: {{db_size}}</p>

%for all_keys in all_keys:
<p><a href="/keyvalue/show/{{all_keys}}"> {{all_keys}}</p>
%end

</div>

</div>

</body>
</html>


