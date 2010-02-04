<html>
 <head>

 <title>redweb | web interface for Redis</title>
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
  <script src="/static/vanadium-min.js" type="text/javascript"></script> 

  <link rel="stylesheet" type="text/css" href="/static/style.css" type="text/css" />

</head>

<body> 
<div id="header-wrap"> 
<h1>Returned: <strong class="red">{{returned_value}}</strong></h1>
</div>

<div class="sidebar">
<h2>Database Infobox</h2>
<hr />
<p>Go to: <a href="#strings">Strings</a> | <a href="#lists">Lists</a> | <a href="#sets">Sets</a> | <a href="#zsets">Sorted Sets</a></p>
<hr />
<p>Database Size: <strong>{{db_size}}</strong></p>
<hr />
<p>Search for keys: (use <strong>*</strong> for wildcard)</p>
    <form name="search" action="/search/" method="post">
    <input type="text" name="key" input class=":required :only_on_submit input_form" />
    <input type="submit" value="Search" /></p>

    </form>
<p>Results:</p>
%for results in search_result:
<form name="key_delete" action="/delete/" method="post">
<input type="text" name="key_delete" value="{{results}}" readonly  />
<input type="submit" value="Delete" />
</form>
%end


<hr />

</div>


<div class="wrapper">


<div class="main">   
<h1 class = "red"> Redweb.</h1>
<p>Redweb is a web interface for Redis, by Ted Nyman. It's MIT licensed, so go ahead and <a href="https://github.com/tnm/redweb">fork Redweb</a>on GitHub!</div>

 <a name="strings"></a>
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
   <a name="lists"></a>
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

    <hr />

    <form name="list_length" action="/lists/length/" method="post">

    <h3>Return the length of a list (LLEN)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Get Length" />

    </form>

    <hr />

    <form name="list_lpop" action="/lists/leftpop/" method="post">

    <h3>Return and remove the first element of a list (LPOP)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Left Pop" />

    </form>

    <hr />

    <form name="list_rpop" action="/lists/rightpop/" method="post">

    <h3>Return and remove the last element of a list (RPOP)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Right Pop" />

    </form>


    </div>
   <a name="sets"></a>
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

    <h3>Remove a member from a set (SREM)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Remove" />

    </form>

    <hr />

    <form name="set_cardinality" action="/sets/cardinality/" method="post">

    <h3>Return the cardinality of a set (SCARD)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Return Cardinality" />

    </form>

    <hr />

    <form name="set_intersection" action="/sets/intersection/" method="post">

    <h3>For any number of sets, return the intersection of those sets (SINTER)</h3>
    <p>Keys (comma separated):<input type="text" name="key" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Return Intersection" />

    </form>
    
    <hr />

    <form name="set_union" action="/sets/intersection/" method="post">

    <h3>For any number of sets, return the the union of those sets (SUNION)</h3>
    <p>Keys (comma separated):<input type="text" name="key" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Return Union" />

    </form>

    <hr />

    <form name="set_members" action="/sets/members/" method="post">

    <h3>Return all members of a set (SMEMBERS)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Return Members" />

    </form>

    <hr />

    <form name="set_random" action="/sets/random/" method="post">

    <h3>Return a random member of a set, without removing it (SRANDMEMBER)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Return Random Member" />

    </form>

    </div>
    <a name="zsets"></a>
    <div class="main">   
    <h2>Sorted Sets</h2>
    <hr />
    <form name="zset_remove" action="/zsets/add/" method="post">
    <h3>Add a member to a sorted set (ZADD)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /></p>
       Score:<input type="text" name="score" input class=":required :only_on_submit input_form" />
    <input type="submit" class="submit_form" value="Add" />

    </form>
   
    <hr />

    <form name="zset_remove" action="/sets/remove/" method="post">

    <h3>Remove a member from a sorted set (ZREM)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Remove" />

    </form>

    <hr />

    <form name="zset_cardinality" action="/zsets/cardinality/" method="post">

    <h3>Return the cardinality of a sorted set (ZCARD)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /></p>

    <input type="submit" class="submit_form" value="Return Cardinality" />

    </form>


    </div>
</div>

</div>

</body>
</html>


