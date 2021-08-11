def breed_calculator():
    print("Welcome do ProBreederBR Breed Calculator")
    print("This calculator was based on WhoopDeeDoo's Breeding calculator.")
    print("https://www.desmos.com/calculator/hqzmebd2nj")
    print("https://www.youtube.com / whoopdeedoo56")
    print("@Whoopdeedoo12")

    # expected value of selling of the bred axie (in USD)
    # You should use the lowest value found in the Marketplace
    selling_value = 500

    # price of 1 AXS in USD
    AXS_price = 40.86

    # price of 1 SLP in USD
    SLP_price = 0.2139

    # quantity of AXS used in one breeding
    AXS_per_breed = 2

    # quantity of SLP used per breed count per couple
    # SLP_one_breed = 300
    # SLP_two_breeds = 900 (600+300)
    # SLP_three_breeds = 1800 (900+600+300)
    # SLP_four_breeds = 3300 (1500+900+600+300)
    # SLP_five_breeds = 5700 (2400+1500+900+600+300)
    # SLP_six_breeds = 9600 (3900+2400+1500+900+600+300)
    # SLP_seven_breeds = 15900 (6300+3900+2400+1500+900+600+300)
    SLP_used = [0, 300, 900, 1800, 3300, 5700, 9600, 15900]

    for breed in range (1,8):
        total_selling_value = breed * selling_value
        total_cost = SLP_used[breed] * SLP_price + breed * (AXS_per_breed * AXS_price)
        profit = total_selling_value - total_cost
        ending_credit = "profit"
        if profit < 0:
            ending_credit = "loss"
        print("\nWhen you breed these axies", breed, "times, you will have a", ending_credit, "of", profit, "USD")
        print("Because you will sell them by", total_selling_value, "USD", "and have a cost of", total_cost, "for breeding them." )
        print("To avoid losses you should sell each child for at least", total_cost/breed, "USD")





if __name__ == '__main__':
    breed_calculator()


