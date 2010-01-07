<html>
<head>
  <title>{{title}}</title>
 </head>
 <body>
<h2>Edit the pair ({{key}} | {{value}}):</h2>

<form name="input" action="/keyvalue/add/" method="post">
    <p>Key:
    <p><input type="text" name="key" value="{{key}}" input class=":required" /></p>
    <p>Value:</p>
    <p><input type="text" name="value" value="{{value}}" input class=":required" /></p>

    <input type="submit" value="Change" />

</form>

<hr />

<form name="input2" action="/keyvalue/delete/" method="post">
    <p>Delete the key:</p>
    <p><input type="text" name="key_delete" value="{{key}}" input class=":required" /></p>

    <input type="submit" value="Delete" />

</form>
 

</body>
</html>

