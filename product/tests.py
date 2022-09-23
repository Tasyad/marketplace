    # def get(self, request, id):
    #     cart = Cart.objects.get(user_id=id)
    #     products = Product.objects.all()
    #     serializer = CartSerializer(cart)
    #     list = []
    #     for i in products:
    #         list.append(i.description)
    #
    #     data = {
    #         "product": list
    #     }
    #     # return Response(data)
    #     return Response(serializer.data)
    # def get(self, request, id):
    #     cart = Cart.objects.get(user_id=id)
    #     serializer = CartSerializer(cart)
    #     return Response(serializer.data)
    # def get(self, request):
    #     products = Product.objects.all()
    #     price_list = []
    #     revenue = []
    #     for j in products:
    #         one = j.price * j.quantity
    #         price_list.append(j.price)
    #         revenue.append(one)
    #     post_count = len(price_list)
    #     revenue = sum(revenue)
    #     max_price = max(price_list)
    #     avg_price = sum(price_list) / len(price_list)
    #     min_price = min(price_list)
    #     data = {
    #         "max_price": max_price,
    #         "avg_price": avg_price,
    #         "min_price": min_price,
    #         "revenue": revenue,
    #         "number of posts": post_count
    #
    #     }
    #     return Response(data)
#