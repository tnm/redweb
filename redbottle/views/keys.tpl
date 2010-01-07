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

    <h1>Add a Key-Value to the Redis Store</h1>

    <form name="input" action="/keyvalue/add/" method="post">
    
    <p>Key:</p>
    <p><input type="text" name="key" input class=":required input_form" /></p>
    
    <p>Value:</p>
    <p><input type="text" name="value" input class=":required input_form" /></p>

    <input type="submit" class="submit_form" value="Add" />

    </form>

<hr />

    <form name="input2" action="/keyvalue/delete/" method="post">
    <p>Delete a key:</p>
    <p><input type="text" class="input_form" name="key_delete" /></p>

    <input type="submit" class="submit_form" value="Delete" />

    </form>

<hr />

<h2><strong>All keys:</strong></h2>

%for all_keys in all_keys:
<p><a href="/keyvalue/show/{{all_keys}}"> {{all_keys}}</p>
%end

</div>

</div>

</body>
</html>


