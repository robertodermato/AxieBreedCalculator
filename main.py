def breed_calculator():
    print("Welcome do ProBreederBR Breed Calculator")
    print("This calculator was based on WhoopDeeDoo's Breeding calculator.")
    print("https://www.desmos.com/calculator/hqzmebd2nj")
    print("https: // www.youtube.com / whoopdeedoo56")
    print("@Whoopdeedoo12")

    # expected value of selling of the bred axie (in USD)
    # You should use the lowest value found in the Marketplace
    selling_value = 800

    # value of 1 AXS in USD
    AXS = 43.6

    # value of 1 SLP in USD
    SLP = 0.18

    # quantity of AXS used in one breeding
    AXS_per_breed = 4

    # quantity of SLP used per breed count per couple
    # SLP_one_breed = 300
    # SLP_two_breeds = 600
    # SLP_three_breeds = 900
    # SLP_four_breeds = 1500
    # SLP_five_breeds = 2400
    # SLP_six_breeds = 3900
    # SLP_seven_breeds = 6300
    SLP_used = [0, 300, 600, 900, 1500, 2400, 3900, 6300]

    for breed in range (1,8):
        profit = breed * selling_value - (SLP_used[breed] * SLP + breed*(AXS_per_breed * AXS))
        ending_credit = "profit"
        if profit < 0:
            ending_credit = "loss"
        print("When you breed these axies", breed, "times, you will have a", ending_credit, "of", profit, "USD")





if __name__ == '__main__':
    breed_calculator()


