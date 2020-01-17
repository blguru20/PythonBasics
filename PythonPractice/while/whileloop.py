lst = [1,2,9,3,7];

index = 0; 
product = 1;

while index < len(lst) :
	product*=lst[index];
	index+=1;

print(product);
