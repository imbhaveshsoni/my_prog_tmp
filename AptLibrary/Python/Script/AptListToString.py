def AptListToString(string,joinwithstr='',startcstr='',endcstr=''):  
    
        # initialize an empty string 
        result_string = startcstr
        
        # traverse in the string   
        for ele in string:  
            result_string += ele+joinwithstr

        result_string += endcstr
        
        # return string   
        return result_string  