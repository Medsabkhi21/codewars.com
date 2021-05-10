 nb_list = []
 for sub_interval in intervals:
        for i in range(sub_interval[0],sub_interval[1]):
            nb_list.append(i)
 return len(set(nb_list))