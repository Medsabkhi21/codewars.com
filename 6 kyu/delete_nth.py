def delete_nth(order,max_e):
 final=list()
 for i in order :
        if final.count(i)<max_e:
            final.append(i)
 return final 