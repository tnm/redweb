<html>
 <head>
  <title>{{title}}</title>
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
  <script src="/static/vanadium-min.js" type="text/javascript"></script> 
</head>

<body> 
     
<p>Add a key:</p>

<form name="input" action="/keyvalue/add/" method="post">

    <p><input type="text" name="key" input class=":required" /></p>
    <p>Add a value:</p>
    <p><input type="text" name="value" input class=":required" /></p>

    <input type="submit" value="Add" />

</form>

<form name="input2" action="/keyvalue/delete/" method="post">
    <p>Delete a key:</p>
    <p><input type="text" name="key_delete" /></p>

    <input type="submit" value="Delete" />

</form>

<p><strong>All keys:</strong> </p>

%for all_keys in all_keys:
<p><a href="/keyvalue/show/{{all_keys}}"> {{all_keys}}</p>
%end

</body>
</html>


