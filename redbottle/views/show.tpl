<html>
<head>
  <title>{{title}}</title>
  <link rel="stylesheet" type="text/css" href="/static/style.css" type="text/css" />
 </head>
 <body>

<div class="wrapper">

<div class="main">


    <h2>Edit the pair ({{key}} | {{value}}):</h2>


    <form name="edit" action="/keyvalue/add/" method="post">
    
    <p>Key:
    <p><input type="text" name="key" value="{{key}}" input class=":required input_form" /></p>
    
    <p>Value:</p>
    <p><input type="text" name="value" value="{{value}}" input class=":required input_form" /></p>

    <input type="submit" class="submit_form" value="Make the Change" />

    </form>

<hr />

    <form name="key_delete" action="/keyvalue/delete/" method="post">
    
    <p>Delete the key:</p>
    <p><input type="text" name="key_delete" class="input_form" value="{{key}}" /></p>

    <input type="submit" class="submit_form" value="Delete" />

    </form>
 
</div>

</div>

</body>
</html>

