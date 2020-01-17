num = int(input("Enter a number : "));

i = 2;
isPrime = True;
while i < (num/2) : 
	if (num % i) == 0 : 
		isPrime = False;
		print ("is divisible by : ")
		print (i);
	
	i= i + 1;

if isPrime==True :
	print("num is Prime : ");	
else :
	print("num is not Prime : ");
		
