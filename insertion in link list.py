class node:
    def __init__(self,val):
        self.data=val
        self.next=None

class linklist:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,val):
        if self.head==None:
            self.head=node(val)
            self.tail=self.head
        else:
            self.tail.next=node(val)
            self.tail=self.tail.next


def reverse(head):
    current=head
    prev=None
    temp=None
    while(current!=None):
        temp=current.next
        current.next=prev
        prev=current
        current=temp
    head=prev
    


def display(head):
    temp=head
    while(temp!=None):
        print(temp.data)
        temp=temp.next

n=int(input())
arr=[]
lis=linklist()
for i in range(n):
    val=int(input())
    lis.insert(val)
ll=reverse(lis.head)
display(lis.head)
