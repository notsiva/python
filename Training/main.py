def calculate_love_score(boy_name,girl_name):
    word1="true"
    word2="love"
    combined_name=boy_name+girl_name
    
    t=combined_name.count("t")
    r=combined_name.count("r")
    u=combined_name.count("u")
    e=combined_name.count("e")
    true=t+r+u+e
    
    l=combined_name.count("l")
    o=combined_name.count("o")
    v=combined_name.count("v")
    e=combined_name.count("e")
    love=l+o+v+e
    
    print(true+love)
    
calculate_love_score("sivakaran","swetha")
        
    


    
    