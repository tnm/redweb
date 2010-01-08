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


    <h2>Change the key's value ( {{key}} | {{value}} ):</h2>


    <form name="edit" action="/keyvalue/add/" method="post">
    
    <p>Key:
    <p><input type="text" name="key" value="{{key}}" readonly input class=":required :only_on_submit input_form" /></p>
    
    <p>Value:</p>
    <p><input type="text" name="value" value="{{value}}" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Make the Change" />

    </form>

<hr />

    <form name="key_delete" action="/keyvalue/delete/" method="post">
    
    <h2>Delete the key:</h2>
    <p><input type="text" name="key_delete" readonly input class=":required :only_on_submit input_form" value="{{key}}" /></p>

    <input type="submit" class="submit_form" value="Delete" />

    </form>
 
</div>

</div>

</body>
</html>

