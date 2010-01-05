<html>
 <head>
  <title>{{title}}</title>
 </head>
 <body> 
     

    <p>Add a key:</p>
    <form name="input" action="/keyvalue/add/" method="post">
<input type="text" name="key" />
    <p>Add a value:</p>
<input type="text" name="value" />
<input type="submit" value="Add" />
</form>

    <form name="input2" action="/keyvalue/delete/" method="post">
    <p>Delete a key:</p>
<input type="text" name="key_delete" />

<input type="submit" value="Delete" />

</form>

 
</body>
</html>

