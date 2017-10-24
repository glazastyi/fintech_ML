def discreter(discrete_values, float_array, only_borders = False):
    number_of_discrete_val = len(discrete_values)
    discreted_array = []
    for i in float_array:
        less_loc = -1
        for j in xrange(number_of_discrete_val):
            if i > discrete_values[j]:
                less_loc = j
        
        if less_loc <= -1:
            discreted_array.append(discrete_values[0])
        elif less_loc >= number_of_discrete_val - 1:
            discreted_array.append(discrete_values[number_of_discrete_val - 1])
        else:
            if only_borders:
                discreted_array.append(i)
            else:
                if i - discrete_values[less_loc] > discrete_values[less_loc+1] - i:
                    discreted_array.append(discrete_values[less_loc+1])
                else:
                    discreted_array.append(discrete_values[less_loc])
    return discreted_array