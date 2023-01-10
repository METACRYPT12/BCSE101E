class customer:
    def __init__(self, cust_id, product, quantity, rate):
        self.cust_id = int(cust_id)
        self.product = product
        self.quantity = int(quantity)
        self.rate = float(rate)
        self.total_price = self.quantity * self.rate


def Fn1(provided_cust_id):
    cust_total = 0
    for obj in custList:
        if (obj.cust_id == provided_cust_id):
            cust_total = cust_total + obj.total_price
    print(cust_total)


def Fn2():
    max_ord, min_ord = 0, custList[0].quantity
    max_prod, min_prod = custList[0].product, custList[0].product
    for obj in custList:
        if (obj.quantity > max_ord):
            max_ord = obj.quantity
            max_prod = obj.product
        if (obj.quantity < min_ord):
            min_ord = obj.quantity
            min_prod = obj.product
    print("Maximum Ordered Product ", max_prod)
    print("Minimum Ordered Product ", min_prod)


def Fn3():
    cust_order_list = {}
    for obj in custList:
        if (obj.cust_id not in cust_order_list):
            cust_order_list.update({obj.cust_id: obj.quantity})
        else:
            cust_order_list[obj.cust_id] = cust_order_list[obj.cust_id] + obj.quantity
    x = {k: v for k, v in sorted(
        cust_order_list.items(), key=lambda item: item[1], reverse=True)}
    print("Customer with maximum Order ", list(x.keys())[0])


n = int(input())
m = int(input())
tmp = []
custList = []
data = open("230106\customer_purchase.txt", "r+")
data.write("customerId,Product,Quantity,rate,TotalPrice\n")
for i in range(m):
    tmp = input().strip().split()
    custList.append(customer(*tmp))
    obj = custList[i]
    data.write("{0},{1},{2},{3},{4}\n".format(
        obj.cust_id, obj.product, obj.quantity, obj.rate, obj.total_price))
Fn1(111)
Fn1(222)
Fn1(333)
Fn2()
Fn3()
total_session_purchase = 0
for obj in custList:
    total_session_purchase = total_session_purchase + obj.total_price
data.write("TotalAmount: Rs:{0}".format(total_session_purchase))
data.seek(0)
print(data.read())
