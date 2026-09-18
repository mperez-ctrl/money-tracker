"""
If a transaction's Merchant text contains one of these substring (case-insensitive), 
it's auto-assigned that CategoryID/SubcategoryID instead of being left blank for manual assignment.

"""
# substring to match, CategoryID, SubcategoryID
merchant_rules = [
    # 1 Housing
    # 1	1	Rent
    ("RENT", 1, 1)
    # 1	2	Wi-Fi / Internet
    # 1	3	Electricity
    # 1	4	Gas Utility
    # 1	5	Renters/Home Insurance
    # 2	Food & Dining
    # 2	6	Groceries
    # 2	7	Coffee & Cafes
    # 2	8	Fast Food
    # 2	9	Restaurants
    # 2	10	Food Delivery
    # 3	Transportation
    # 3	11	Gasoline
    # 3	12	Parking
    # 3	13	Ride Share
    # 3	14	Public Transit
    # 3	15	Auto Maintenance
    # 3	16	Auto Insurance
    # 3	17	Auto Registration/DMV
    # 4	Health & Wellness
    # 4	18	Doctor Visits
    # 4	19	Pharmacy/Medications
    # 4	20	Urgent Care
    # 4	21	Therapy/Mental Health
    # 4	22	Fitness Memberships
    # 5	Pets
    # 5	23	Pet Insurance
    # 5	24	Pet Food
    # 5	25	Veterinary Care
    # 6	Shopping
    # 6	26	Clothing & Accessories
    # 6	27	Beauty & Personal Care
    # 6	28	Home Goods
    # 6	29	Electronics
    # 6	30	Books & Stationery
    # 6	31	General Merchandise
    # 7	Entertainment
    # 7	32	Streaming Subscriptions
    # 7	33	Movies & Theaters
    # 7	34	Activities & Events
    # 7	35	Hobbies & Gaming
    # 8	Travel
    # 8	36	Flights
    # 8	37	Lodging
    # 9	Education
    # 9	38	Tuition & Courses
    # 9	39	Bookstore/Supplies
    # 10	Debt & Fees
    # 10	40	Credit Card Payment
    # 10	41	Student Loan Payment
    # 10	42	Interest Charges
    # 10	43	Bank/Service Fees
    # 11	Savings & Investments
    # 11	44	Roth IRA Contribution
    # 11	45	Savings Transfer
    # 12	Personal Transfers
    # 12	46	Zelle Sent
    # 12	47	Zelle Received
    # 13	Uncategorized
]

def auto_categorize(merchant):
    merchant_upper = merchant.upper()
    for pattern, category_id, subcategory_id in merchant_rules:
        if pattern in merchant_upper:
            return category_id, subcategory_id
    return None, None
