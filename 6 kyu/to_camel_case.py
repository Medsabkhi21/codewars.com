def to_camel_case(text):

   x=text.replace("-","_").split('_')
   y=[x[0],]
   for i in x[1:]:
    y.append(i.title())
   return ''.join(y) 