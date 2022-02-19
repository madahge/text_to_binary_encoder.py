# text to binary encoder


<h4> Python3 code to demonstrate working of
<h4> Converting String to binary
<h4> Using join() + ord() + format()
  
<h3> initializing string 
test_str = "GeeksforGeeks"<br><br>
  
<h3> printing original string 
print("The original string is : " + str(test_str))<br><br>
  
<h4> using join() + ord() + format()
<h3> Converting String to binary
res = ''.join(format(ord(i), '08b') for i in test_str)<br><br>
  
<h3> printing result 
print("The string after binary conversion : " + str(res))
