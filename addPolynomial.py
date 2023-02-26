nk list Node
class Node:
	def __init__(self, c, p):
		self.coeff = c
		self.pow = p
		self.next = None

# insert in linked list
def append(head, coeff, power):
	new_node = Node(coeff, power)

	while head.next != None:
		head = head.next
	head.next = new_node
#sum of polynomail p1 and p2 

def addPolynomial(p1, p2):
	res = Node(0, 0) # dummy node ...head of resultant list
	prev = res # pointer to last node of resultant list

	while p1 != None and p2 != None:
		if p1.pow < p2.pow:
			prev.next = p2
			prev = p2
			p2 = p2.next
		elif p1.pow > p2.pow:
			prev.next = p1
			prev = p1
			p1 = p1.next
		else:
			p1.coeff += p2.coeff
			prev.next = p1
			prev = p1
			p1 = p1.next
			p2 = p2.next

	if (p1 != None):
		prev.next = p1

	if (p2 != None):
		prev.next = p2

	return res.next


# Driver code
if __name__ == '__main__':

	# 1st Number 
	print("Zarib jomeleh aval : ")
	zFirst=int(input())
	print("Tawan jomelh aval : ")
	pFirst=int(input())
	
	print("Zarib jomelh dowm : ")
	zSecond=int(input())
	print("tawan jomelh dowm : ")
	pSecond=int(input())
	
	print("Zarib jomelh sevom : ")
	zthrid=int(input())
	print("tawan jomelh sevom : ")
	pthrid=int(input())
	
	poly1 = Node(zFirst, pFirst)
	append(poly1, zSecond, pSecond)
	append(poly1, zthrid, pthrid)

	# 2nd Number:
	
	print("Zarib jomeleh aval : ")
	bzFirst=int(input())
	print("Tawan jomelh aval : ")
	bpFirst=int(input())
	
	print("Zarib jomelh dowm : ")
	bzSecond=int(input())
	print("tawan jomelh dowm : ")
	bpSecond=int(input())
	
	print("Zarib jomelh sevom : ")
	bzthrid=int(input())
	print("tawan jomelh sevom : ")
	bpthrid=int(input())
	
	poly2 = Node(bzFirst, bpFirst)
	append(poly2, bzSecond, bpSecond)
	append(poly2, bzthrid, bpthrid)
    
	
	sum = addPolynomial(poly1, poly2)

	ptr = sum
	while ptr != None:
		# printing polynomial
		print(ptr.coeff, 'x^', ptr.pow, end="")
		if ptr.next != None:
			print(" + ", end="")
		ptr = ptr.next
	print()


