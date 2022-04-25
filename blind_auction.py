bidders = {}
auction_live = True
bid = 0

print("Welcome to the silent auction!")

while auction_live:
    
    name = input("What is your name? ")
    bid = input("What is your bid? ")
    bid = int(bid)
    bidders[name] = bid
    
    any_more = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if any_more == "no":
        auction_live = False

def get_key(val):
    for key, value in bidders.items():
        if val == value:
            return key
 
    return "key doesn't exist"

highest_bid = 0
highest_bidder = " "

for person, bid in bidders.items():
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = get_key(bid)

# print(bidders)
print(f"{highest_bidder} was the highest bidder at {highest_bid}.")