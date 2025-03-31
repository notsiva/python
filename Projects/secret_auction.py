bids={}
while True:

    name=input("In Whose name you are bidding?: ")
    amount=int(input('What is the amount you are bidding?: $'))
    bids[name]=amount
    is_auction_over=input("Any other bidders? (y/n): \n")
    if is_auction_over!="y":    
        break
    
k=max(bids,key=bids.get)
print(f"{k} have won the bid! with ${bids[k]}")
        
        
