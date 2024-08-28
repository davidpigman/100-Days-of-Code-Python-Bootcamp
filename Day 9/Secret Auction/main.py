# TODO-1: Ask the user for input
bids = {}
more_bids = True
while more_bids:
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    bid = input("What's your bid? ")
    other_bidders = input("Are there any other bidders?  Type 'yes' or 'no' ")
    if other_bidders == 'no':
        more_bids = False

# TODO-2: Save data into dictionary {name: price}
    bids[name] = bid

print(f"bids {bids}")

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

highest_bid = 0
for bidder in bids:
    bid = int(bids[bidder])

    print(f"bidder {bidder} bid {bid}")
    if bid > highest_bid:
      highest_bidder = bidder
      highest_bid = bid


print(f"The winner is {highest_bidder} with a bid of {highest_bid}")
