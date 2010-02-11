<html>
 <head>

 <title>Redweb | web interface for Redis</title>

  <link type="text/css" href="/static/style.css" rel="stylesheet" />
  
  <script type="text/javascript" src="/static/jquery-1.3.2.min.js"></script>
  <script type="text/javascript" src="/static/jquery-ui-1.7.2.custom.min.js"></script>
  <script type="text/javascript" src="/static/vanadium-min.js" ></script> 
  <script type="text/javascript">
			$(function(){
	
				// Tabs
				$('#tabs').tabs();
				
				//hover states on the static widgets
				$('#dialog_link, ul#icons li').hover(
					function() { $(this).addClass('ui-state-hover'); }, 
					function() { $(this).removeClass('ui-state-hover'); }
				);
				
			});
  </script>

				<script type="text/javascript">
				$(document).ready(function() {
					$("#info").hide();
					$("#info_button").click(function() {
					$("#info").animate({height: "toggle"}, 500);
					});
				});
  </script>



</head>

<body> 
<div id="header-wrap"> 
<h1>Returned: <strong class="red">{{returned_value}}</strong></h1>
</div>

<div class="sidebar">
<h2>Database Infobox</h2>
<hr />
<p>Database Size: <strong>{{db_size}}</strong></p>
<hr />


<button id="info_button">Detailed Database Info</button>
<div id="info">
<p>{{info}}</p>
</div>
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




</div>


<div class="wrapper">


<div class="major">   

<div id = "tabs">
	<ul>
		<li><a href="#strings">Strings</a></li>
		<li><a href="#lists">Lists</a></li>
		<li><a href="#sets">Sets</a></li>
		<li><a href="#zsets">Sorted Sets</a></li>
</ul>



<div id="strings">
  
    <form name="string_set" action="/strings/set/" method="post">
   
    <h3>Set a string value for a given key (SET)</h3> 
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /> 
       Value:<input type="text" name="value" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Set" /></p>

    </form>
<hr />

    <form name="string_get" action="/strings/get/" method="post">
   
    <h3>Get a string value for a given key (GET)</h3> 
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Get" /></p>

    </form>

    </div>

 
    <div id="lists">
	
    <form name="list_rightpush" action="/lists/rightpush/" method="post">
    
    <h3>Append element to the tail of a list (RPUSH)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Element:<input type="text" name="element" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Right Push" /></p> 

    </form>

    <hr />

    <form name="list_leftpush" action="/lists/leftpush/" method="post">

    <h3>Append element to the head of a list (LPUSH)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Element:<input type="text" name="element" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Left Push" /></p>

    </form>

    <hr />

    <form name="list_length" action="/lists/length/" method="post">

    <h3>Return the length of a list (LLEN)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Get Length" /></p>

    </form>

    <hr />

    <form name="list_lpop" action="/lists/leftpop/" method="post">

    <h3>Return and remove the first element of a list (LPOP)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Left Pop" /></p>

    </form>

    <hr />

    <form name="list_rpop" action="/lists/rightpop/" method="post">

    <h3>Return and remove the last element of a list (RPOP)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Right Pop" /></p>

    </form>


   </div>

 
    <div id="sets">

    <form name="set_add" action="/sets/add/" method="post">

    <h3>Add a member to a set (SADD)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Add" /></p>

    </form>
   
    <hr />

    <form name="set_remove" action="/sets/remove/" method="post">

    <h3>Remove a member from a set (SREM)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Remove" /></p>

    </form>

    <hr />

    <form name="set_pop" action="/sets/pop/" method="post">

    <h3>Return and remove a random member from a set (POP)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Pop" /></p>

    </form>


    <hr />

    <form name="set_move" action="/sets/move/" method="post">
    <h3>Move a member of a set to another set (SMOVE)</h3>
    <p>Source Key:<input type="text" name="source_key" input class=":required :only_on_submit input_form" />
       Destination Key:<input type="text" name="destination_key" input class=":required :only_on_submit input_form" /><br />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" />
    <input type="submit" class="submit_form" value="Move" /></p>

    </form>
   
    <hr />

    <form name="set_cardinality" action="/sets/cardinality/" method="post">

    <h3>Return the cardinality of a set (SCARD)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Return Cardinality" /></p>

    </form>

    <hr />

    <form name="set_ismember" action="/sets/ismember/" method="post">

    <h3>Check if member is a member at a particular key - returns 1 if true (SISMEMBER)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Check for membership" /></p>

    </form>

    <hr />

    <form name="set_intersection" action="/sets/intersection/" method="post">

    <h3>For any number of sets, return the intersection of those sets (SINTER)</h3>
    <p>Keys (comma separated):<input type="text" name="key" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Return Intersection" /></p>

    </form>

    <hr />

    <form name="set_interstore" action="/sets/interstore/" method="post">

    <h3>For any number of sets, return the intersection and store to the destination key (SINTERSTORE)</h3>
 <p>Destination key:<input type="text" name="destkey" input class=":required :only_on_submit input_form" />
    Keys (comma separated):<input type="text" name="key" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Return and Store Intersection" /></p>

    </form>

    
    <hr />

    <form name="set_union" action="/sets/union/" method="post">

    <h3>For any number of sets, return the the union of those sets (SUNION)</h3>
    <p>Keys (comma separated):<input type="text" name="key" input class=":required :only_on_submit input_form" />
    <input type="submit" class="submit_form" value="Return Union" /></p>

    </form>

    <hr />

    <form name="set_unionstore" action="/sets/unionstore/" method="post">

    <h3>For any number of sets, return the union and store it to the destination key (SUNIONSTORE)</h3>
 <p>Destination key:<input type="text" name="destkey" input class=":required :only_on_submit input_form" />
    Keys (comma separated):<input type="text" name="key" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Return and Store Union" /></p>

    </form>


    <hr />

    <form name="set_difference" action="/sets/difference/" method="post">

    <h3>For any number of sets, return the difference between the first set and all subsequent sets (SDIFF)</h3>
    <p>Keys (comma separated):<input type="text" name="key" input class=":required :only_on_submit input_form" />
    <input type="submit" class="submit_form" value="Return Difference" /></p>

    </form>

    <hr />

    <form name="set_diffstore" action="/sets/diffstore/" method="post">

    <h3>For any number of sets, return the difference and store it to a destination key (SDIFFSTORE)</h3>
 <p>Destination key:<input type="text" name="destkey" input class=":required :only_on_submit input_form" />
    Keys (comma separated):<input type="text" name="key" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Return and Store Difference" /></p>

    </form>


    <hr />

    <form name="set_members" action="/sets/members/" method="post">

    <h3>Return all members of a set (SMEMBERS)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />

    <input type="submit" class="submit_form" value="Return Members" /></p>

    </form>

    <hr />

    <form name="set_random" action="/sets/random/" method="post">

    <h3>Return a random member of a set, without removing it (SRANDMEMBER)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />

    <input type="submit" class="submit_form" value="Return Random Member" /></p>

    </form>

    </div>  
 

    <div id="zsets">

    <form name="zset_remove" action="/zsets/add/" method="post">
    <h3>Add a member to a sorted set (ZADD)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /><br />
       Score:<input type="text" name="score" input class=":required :only_on_submit input_form" />
    <input type="submit" class="submit_form" value="Add" /></p>

    </form>
   
    <hr />

    <form name="zset_remove" action="/zsets/remove/" method="post">

    <h3>Remove a member from a sorted set (ZREM)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Remove" /></p>

    </form>

    <hr />

    <form name="zset_cardinality" action="/zsets/cardinality/" method="post">

    <h3>Return the cardinality of a sorted set (ZCARD)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
    <input type="submit" class="submit_form" value="Return Cardinality" /></p>

    </form>
 
    <hr />

    <form name="zset_score" action="/zsets/score/" method="post">

    <h3>Return the score for a key and member (ZSCORE)</h3>
    <p>Key:<input type="text" name="key" input class=":required :only_on_submit input_form" />
       Member:<input type="text" name="member" input class=":required :only_on_submit input_form" /><input type="submit" class="submit_form" value="Return Score" /></p>

    </form>


    </div>
    </div>

<div id = "footer-wrap">
<p><strong class="red">Redweb</strong> | a web interface for Redis, by Ted Nyman | MIT licensed. <a href="https://github.com/tnm/redweb">Fork Redweb</a> on GitHub | The <a href="http://code.google.com/p/redis/wiki/CommandReference">Redis Command Reference</a>

</div>

</div>

</div>

</body>
</html>


