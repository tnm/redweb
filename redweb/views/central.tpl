<html>
 <head>

 <title>Redweb | web interface for Redis</title>

  <link type="text/css" href="/static/style.css" rel="stylesheet" />
  
  <script type="text/javascript" src="/static/jquery-1.3.2.min.js"></script>
  <script type="text/javascript" src="/static/jquery-ui-1.7.2.custom.min.js"></script>
  <script type="text/javascript" src="/static/vanadium-min.js" ></script> 
  <script type="text/javascript">
  $(document).ready(function(){
    $(".accordion").accordion({ fillSpace: true, collapsible: true });  });
  </script>


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


 </head>


<body> 

<div id="header-wrap"> 
<div id="header-content">
<h1>Returned: <strong class="red">{{returned_value}}</strong></h1>
</div>
</div>


<div class="sidebar">

<h2>Redis Dashboard</h2>
<hr />

<p>Database Size: <strong>{{db_size}}</strong> Keys</p>

<form name="save" action="/save/" method="post">
<input type = "submit" value ="Save">
</form>

<form name="bgsave" action="/bgsave/" method="post">
<input type = "submit" value ="Background Save">
</form>

<form name="lastsave" action="/lastsave/" method="post">
<input type = "submit" value ="Time of Last Save">
</form>

<hr />

<h3>Detailed Database Info</h3>
<div>
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

<div id="tabs">
	<ul>
		<li><a href="#strings">Strings</a></li>
		<li><a href="#lists">Lists</a></li>
		<li><a href="#sets">Sets</a></li>
		<li><a href="#zsets">Sorted Sets</a></li>
	</ul>

<div id="strings">
<div class="accordion">

	<h3><a href="#">SET | Set a string value for a given key</a></h3>
	
	<div>
	<form name="string_set" action="/strings/set/" method="post">
   	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
   	<p><label for="value">Value:</label> <input type="text" name="value" input class=":required :only_on_submit input_form" /></p>
    	<p class="submit"><input type="submit" class="submit_form" value="Set" /></p>
    	</form>
	</div>

	<h3><a href="#">GET | Get a string value for a given key</a></h3>
	<div>
    	<form name="string_get" action="/strings/get/" method="post">
    	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    	<p class="submit"><input type="submit" class="submit_form" value="Get" /></p>
	</form>
	</div>

	<h3><a href="#">GETSET | Set a new string value for a given key, and return the old value</a></h3>
	
	<div>
	<form name="string_getset" action="/strings/getset/" method="post">
   	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
   	<p><label for="value">Value:</label> <input type="text" name="value" input class=":required :only_on_submit input_form" /></p>
    	<p class="submit"><input type="submit" class="submit_form" value="Set" /></p>
    	</form>
	</div>

	<h3><a href="#">SETNX | Set a string value for a given key, only if the key doesn't exist</a></h3>
	
	<div>
	<form name="string_setnx" action="/strings/setnx/" method="post">
   	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
   	<p><label for="value">Value:</label> <input type="text" name="value" input class=":required :only_on_submit input_form" /></p>
    	<p class="submit"><input type="submit" class="submit_form" value="Set" /></p>
    	</form>
	</div>

	<h3><a href="#">INCR | Increment a value by 1</a></h3>
	<div>
    	<form name="string_get" action="/strings/increment/" method="post">
    	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    	<p class="submit"><input type="submit" class="submit_form" value="Increment" /></p>
	</form>
	</div>

	<h3><a href="#">DECR | Decrement a value by 1</a></h3>
	<div>
    	<form name="string_decr" action="/strings/decrement/" method="post">
    	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    	<p class="submit"><input type="submit" class="submit_form" value="Increment" /></p>
	</form>
	</div>

	<h3><a href="#">INCRBY | Increment a value by an amount</a></h3>
	<div>
    	<form name="string_incr" action="/strings/incrementby/" method="post">
    	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    	<p><label for="amount">Amount:</label> <input type="text" name="amount" input class=":required :only_on_submit input_form" /></p>
    	<p class="submit"><input type="submit" class="submit_form" value="Increment" /></p>
	</form>
	</div>

	<h3><a href="#">DECRBY | Decrement a value by an amount</a></h3>
	<div>
    	<form name="string_decr" action="/strings/decrementby/" method="post">
    	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
    	<p><label for="amount">Amount:</label> <input type="text" name="amount" input class=":required :only_on_submit input_form" /></p>
	<p class="submit"><input type="submit" class="submit_form" value="Decrement" /></p>
	</form>
	</div>

</div>
</div>


<div id="lists">
<div class="accordion">	
    
 	<h3><a href="#">RPUSH | Append element to the tail of a list</a></h3>
	<div>
 	<form name="list_rightpush" action="/lists/rightpush/" method="post">
	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" />
    	<p><label for="element">Element:</label><input type="text" name="element" input class=":required :only_on_submit input_form" /></p>
   	<p class="submit"> <input type="submit" class="submit_form" value="Right Push" /></p> 
	</form>
	</div>

  	<h3><a href="#">LPUSH | Append element to the head of a list</a></h3>
	<div>
 	<form name="list_leftpush" action="/lists/leftpush/" method="post">
	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
	<p><label for="element">Element:</label> <input type="text" name="element" input class=":required :only_on_submit input_form" /></p>
	<p class="submit"><input type="submit" class="submit_form" value="Left Push" /></p>
	</form>
 	</div>  

 	<h3><a href="#">LLEN | Return the length of a list</a></h3>
	<div>
 	<form name="list_length" action="/lists/length/" method="post">
 	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
 	<p class="submit"><input type="submit" class="submit_form" value="Get Length" /></p>
	</form>
	</div>

	<h3><a href="#">LRANGE | Return a range of elements from a list</a></h3>
    	<div>
	<form name="list_range" action="/lists/range/" method="post">
	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
	<p><label for="start">Start:</label> <input type="text" name="start" input class=":required :only_on_submit input_form" /></p>
	<p><label for="end">End:</label> <input type="text" name="end" input class=":required :only_on_submit input_form" /></p>
	<p class="submit"> <input type="submit" class="submit_form" value="Return Elements" /></p>
	</form>
	</div>

 	<h3><a href="#">LTRIM | Trim a list so it contains just a specific range of elements</a></h3>
	<div>    
	<form name="list_trim" action="/lists/trim/" method="post">
	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
   	<p><label for="start">Start:</label><input type="text" name="start" input class=":required :only_on_submit input_form" /></p>
  	<p><label for="end">End:</label> <input type="text" name="end" input class=":required :only_on_submit input_form" /></p>
  	<p class="submit"> <input type="submit" class="submit_form" value="Trim" /></p>
 	</form>
 	</div>

  	<h3><a href="#">LINDEX | Return an indexed element for a particular key</a></h3>
  	<div>
	<form name="list_index" action="/lists/lindex/" method="post">
 	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
	<p><label for="index">Index:</label> <input type="text" name="index" input class=":required :only_on_submit input_form" /></p>
	<p class="submit"> <input type="submit" class="submit_form" value="Return Element" /></p>
	</form>
	</div>

	<h3><a href="#">LSET | Set an element at index</a></h3>
    	<div>
	<form name="list_set" action="/lists/set/" method="post">
	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
	<p><label for="index">Index:</label> <input type="text" name="index" input class=":required :only_on_submit input_form" /></p>
	<p><label for="element">Element:</label> <input type="text" name="element" input class=":required :only_on_submit input_form" /></p>
	<p class="submit"> <input type="submit" class="submit_form" value="Set" /></p>
	</form>
	</div>

	<h3><a href="#">LREM | For any element in a key, remove a specified number of those elements (the count)</a></h3>
    	<div>
	<form name="list_remove" action="/lists/remove/" method="post">
	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
	<p><label for="count">Count:</label> <input type="text" name="count" input class=":required :only_on_submit input_form" /></p>
	<p><label for="element">Element:</label> <input type="text" name="element" input class=":required :only_on_submit input_form" /></p>
	<p class="submit"> <input type="submit" class="submit_form" value="Remove" /></p>
	</form>
	</div>

  	<h3><a href="#">LPOP | Return and remove the first element of a list</a></h3>
    	<div>
	<form name="list_lpop" action="/lists/leftpop/" method="post">
  	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
	<p class="submit"> <input type="submit" class="submit_form" value="Left Pop" /></p>
	</form>
	</div>

    	<h3><a href="#">RPOP | Return and remove the last element of a list</a></h3>
    	<div>
	<form name="list_rpop" action="/lists/rightpop/" method="post">
  	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
  	<p class="submit"><input type="submit" class="submit_form" value="Right Pop" /></p>
	</form>
	</div>

</div>
</div>

<div id="sets">
<div class="accordion">

 	<h3><a href="#">SADD | Add a member to a set</a></h3>
 	<div>
 	<form name="set_add" action="/sets/add/" method="post">
 	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
 	<p><label for="member">Member:</label> <input type="text" name="member" input class=":required :only_on_submit input_form" /></p>
 	<p class="submit"><input type="submit" class="submit_form" value="Add" /></p>
	</form>
	</div>

 	<h3><a href="#">SREM | Remove a member from a set</a></h3>
 	<div>
	<form name="set_remove" action="/sets/remove/" method="post">
	<p><label for="key">Key:</label><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
 	<p><label for="member">Member:</label><input type="text" name="member" input class=":required :only_on_submit input_form" /></p>
 	<p class="submit"> <input type="submit" class="submit_form" value="Remove" /></p>
	</form>
	</div>

   	<h3><a href="#">POP | Return and remove a random member from a set</a></h3>
	<div>
  	<form name="set_pop" action="/sets/pop/" method="post">
  	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
  	<p class="submit"> <input type="submit" class="submit_form" value="Pop" /></p>
	</form>
	</div>

	<h3><a href="#">SMOVE | Move a member of a set to another set</a></h3>
	<div>
	<form name="set_move" action="/sets/move/" method="post">
 	<p><label for="source_key">Source key:</label><input type="text" name="source_key" input class=":required :only_on_submit input_form" /></p>
 	<p><label for="destination_key">Dest. key:</label> <input type="text" name="destination_key" input class=":required :only_on_submit input_form" /></p>
 	<p><label for="member">Member:</label><input type="text" name="member" input class=":required :only_on_submit input_form" /></p>
 	<p class="submit"> <input type="submit" class="submit_form" value="Move" /></p>
	</form>
	</div>
   
    	<h3><a href="#">SCARD | Return the cardinality of a set</a></h3>
 	<div>
	<form name="set_cardinality" action="/sets/cardinality/" method="post">
 	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
 	<p class="submit"> <input type="submit" class="submit_form" value="Return Cardinality" /></p>
	</form>
	</div>

 	<h3><a href="#">SISMEMBER | Check if member is a member at a particular key</a></h3>
  	<div>
	<form name="set_ismember" action="/sets/ismember/" method="post">
 	<p><label for="key">Key:</label><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
  	<p><label for="member">Member:</label><input type="text" name="member" input class=":required :only_on_submit input_form" /></p>
 	<p class="submit"><input type="submit" class="submit_form" value="Check for membership" /></p>
	</form>
	</div>

  	<h3><a href="#">SINTER | For any number of sets, return the intersection of those sets</a></h3>
	<div>
	<form name="set_intersection" action="/sets/intersection/" method="post">
	<p><label for="key">Keys:</label><input type="text" name="key" input class=":required :only_on_submit input_form" /> (comma separated)</p>
 	<p class="submit"><input type="submit" class="submit_form" value="Return Intersection" /></p>
	</form>
	</div>

 	<h3><a href="#">SINTERSORE | For any number of sets, return the intersection and store to the destination key</a></h3>
	<div>
	<form name="set_interstore" action="/sets/interstore/" method="post">
  	<p><label for="destkey">Dest. key:</label> <input type="text" name="destkey" input class=":required :only_on_submit input_form" /></p>
 	<p><label for="key">Keys:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /> (comma separated)</p>
  	<p class="submit"> <input type="submit" class="submit_form" value="Return and Store Intersection" /></p>
	</form>
    	</div>

	<h3><a href="#">SUNION | For any number of sets, return the the union of those sets</a></h3>
	<div>
	<form name="set_union" action="/sets/union/" method="post">
 	<p><label for="key">Keys:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /> (comma separated)</p>
	<p class="submit"> <input type="submit" class="submit_form" value="Return Union" /></p>
	</form>
	</div>

	<h3><a href="#">SUNIONSTORE | For any number of sets, return the union and store it to the destination key</a></h3>
	<div>
  	<form name="set_unionstore" action="/sets/unionstore/" method="post">
 	<p><label for="destkey">Dest. key:</label> <input type="text" name="destkey" input class=":required :only_on_submit input_form" /></p>
 	<p><label for="key">Keys:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /> (comma separated)</p>
  	<p class="submit"> <input type="submit" class="submit_form" value="Return and Store Union" /></p>
	</form>
	</div>

	<h3><a href="#">SDIFF | For any number of sets, return the difference between the first set and all subsequent sets</a></h3>
	<div>
 	<form name="set_difference" action="/sets/difference/" method="post">
  	<p><label for="key">Keys</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /> (comma separated)</p>
  	<p class="submit"><input type="submit" class="submit_form" value="Return Difference" /></p>
	</form>
	</div>

 	<h3><a href="#">SDIFFSTORE | For any number of sets, return the difference and store it to a destination key</a></h3>
	<div>
  	<form name="set_diffstore" action="/sets/diffstore/" method="post">
  	<p><label for="destkey">Dest. key:</label> <input type="text" name="destkey" input class=":required :only_on_submit input_form" /></p>
  	<p><label for="key">Keys:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /> (comma separated)</p>
  	<p class="submit"><input type="submit" class="submit_form" value="Return and Store Difference" /></p>
	</form>
	</div>

	<h3><a href="#">SMEMBERS | Return all members of a set</a></h3>
	<div>
	<form name="set_members" action="/sets/members/" method="post">
  	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
 	<p class="submit"><input type="submit" class="submit_form" value="Return Members" /></p>
	</form>
	</div>

	<h3><a href="#">SRANDMEMBER | Return a random member of a set, without removing it</a></h3>
 	<div>
	<form name="set_random" action="/sets/random/" method="post">
 	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
 	<p class="submit"><input type="submit" class="submit_form" value="Return Random Member" /></p>
	</form>
	</div>

</div>  
</div>


<div id="zsets">
<div class="accordion">

 	<h3><a href="#">ZADD | Add a member to a sorted set</a></h3>
 	<div>
	<form name="zset_remove" action="/zsets/add/" method="post">
 	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
 	<p><label for="member">Member:</label> <input type="text" name="member" input class=":required :only_on_submit input_form" /></p>
  	<p><label for="score">Score:</label> <input type="text" name="score" input class=":required :only_on_submit input_form" /></p>
  	<p class="submit"><input type="submit" class="submit_form" value="Add" /></p>
	</form>
	</div>
  
 	<h3><a href="#">ZREM | Remove a member from a sorted set</a></h3>
  	<div>
	<form name="zset_remove" action="/zsets/remove/" method="post">
 	<p><label for="key">Key:</label><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
 	<p><label for="member">Member:</label> <input type="text" name="member" input class=":required :only_on_submit input_form" /></p>
 	<p class="submit"> <input type="submit" class="submit_form" value="Remove" /></p>
	</form>
	</div>

 	<h3><a href="#">ZINCRBY | Increment a member by any amount</a></h3>
  	<div>
	<form name="zset_remove" action="/zsets/remove/" method="post">
 	<p><label for="key">Key:</label><input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
 	<p><label for="member">Member:</label> <input type="text" name="member" input class=":required :only_on_submit input_form" /></p>
 	<p><label for="amount">Amount:</label> <input type="text" name="amount" input class=":required :only_on_submit input_form" /></p>

 	<p class="submit"> <input type="submit" class="submit_form" value="Increment" /></p>
	</form>
	</div>

	<h3><a href="#">ZCARD | Return the cardinality of a sorted set</a></h3>
	<div>
	<form name="zset_cardinality" action="/zsets/cardinality/" method="post">
  	<p><label for="key">Key</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
  	<p class="submit"><input type="submit" class="submit_form" value="Return Cardinality" /></p>
	</form>
 	</div>

    	<h3><a href="#">ZSCORE | Return the score for a key and member</a></h3>
	<div>
	<form name="zset_score" action="/zsets/score/" method="post">
  	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
  	<p><label for="member">Member:</label> <input type="text" name="member" input class=":required :only_on_submit input_form" /></p>
 	<p class="submit"> <input type="submit" class="submit_form" value="Return Score" /></p>
	</form>
	</div>


	<h3><a href="#">ZRANGE | Return a range of elements from a list, without scores</a></h3>
    	<div>
	<form name="zset_range" action="/zsets/range/" method="post">
	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
	<p><label for="start">Start:</label> <input type="text" name="start" input class=":required :only_on_submit input_form" /></p>
	<p><label for="end">End:</label> <input type="text" name="end" input class=":required :only_on_submit input_form" /></p>
	<p class="submit"> <input type="submit" class="submit_form" value="Return Elements" /></p>
	</form>
	</div>

	<h3><a href="#">ZRANGE (with scores) | Return a range of elements from a list, with scores</a></h3>
    	<div>
	<form name="zset_range" action="/zsets/rangewithscores/" method="post">
	<p><label for="key">Key:</label> <input type="text" name="key" input class=":required :only_on_submit input_form" /></p>
	<p><label for="start">Start:</label> <input type="text" name="start" input class=":required :only_on_submit input_form" /></p>
	<p><label for="end">End:</label> <input type="text" name="end" input class=":required :only_on_submit input_form" /></p>
	<p class="submit"> <input type="submit" class="submit_form" value="Return Elements" /></p>
	</form>
	</div>



</div>    
</div>
</div>


<div id="footer-wrap">
<div id="header-content"><p><strong class="red">Redweb</strong> | a web interface for Redis, by Ted Nyman | MIT licensed. <a href="https://github.com/tnm/redweb">Fork Redweb</a> on GitHub | The <a href="http://code.google.com/p/redis/wiki/CommandReference">Redis Command Reference</a>
</div>
</div>

</div>

</div>

</body>
</html>


