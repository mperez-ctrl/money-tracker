"""
If a transaction's Merchant text contains one of these substring (case-insensitive), 
it's auto-assigned that CategoryID/SubcategoryID instead of being left blank for manual assignment.

"""
# substring to match, CategoryID, SubcategoryID
merchant_rules = [
    # -------------- 1 Housing --------------
    ## 1	1	Rent
    ("rent", 1, 1),
    ## 1	2	Internet
    ("wi-fi", 1, 2),
    ("ATT              PAYMENT", 1, 2),
    ## 1	3	Electricity
    ## 1	4	Gas Utility
    ## 1	5	Home Insurance

    # -------------- 2 Dining -------------- 
    ## 2	6	Groceries
    ("vons", 2, 6),
    ("WM SUPERCENTER", 2, 6),
    ("WALMART.COM", 2, 6),
    ("WAL-MART", 2, 6),
    ("Walmart+", 2, 6),
    ## 2	7	Coffee
    ("COFFEE", 2, 7),
    ("CAFE", 2, 7),
    ("NATURES BREW", 2, 7),
    ## 2	8	Fast Food
    ("PANDA EXPRESS", 2, 8),
    ("MCDONALD'S", 2, 8),
    ("EL POLLO LOCO", 2, 8),
    ("POPEYES", 2, 8),
    ("TAQUERIA", 2, 8),
    ("TACOS", 2, 8),
    ("ROCK AND REILLYS", 2, 8),
    ("CPI*UNIVERSITY", 2, 8),
    ("USC HOSP", 2, 8),
    ## 2	9	Restaurants
    ("NICKS SOUTH LAKE AVE", 2, 9),
    ("PALENQUE KITCHEN", 2, 9),
    ## 2	10	Food Delivery
    ("grubhub", 2, 10),

    # ------------- Transportation  ------------ 
    ## 3	11	Gasoline
    ("COSTCO GAS", 3, 11),
    ("EXXON", 3, 11),
    ("CHEVRON", 3, 11),
    ("arco", 3, 11),
    ## 3	12	Parking
    ("PARKING", 3, 12),
    ("GARAGE", 3, 12),
    ("USC TRANSP", 3, 12),
    ## 3	13	Ride Share
    ("LYFT", 3, 13),
    ## 3	14	Public Transit
    ("LA METRO", 3, 12),
    ("LAMTRO", 3, 12),
    ## 3	15	Auto Maintenance
    ## 3	16	Auto Insurance
    ("AAA CA MBR", 3, 16),
    ("STATE FARM", 3, 16),
    ## 3	17	Auto Registration/DMV

    # ------------ Health & Wellness ------------ 
    ## 4	18	Doctor Visits
    ("KECKMED", 4, 18),
    ## 4	19	Pharmacy/Medications
    ("CVS PHARMACY", 4, 19),
    ("www.cvs.com", 4, 19),
    ## 4	20	Urgent Care
    ## 4	21	Mental Health
    ("RULA HEALTH", 4, 21),
    ## 4	22	Fitness Memberships
    ("LA Fitness", 4, 22),
    ("LAMUAYTHAI", 4, 22),

    # ------------------ Pets ------------------- 
    ## 5	23	Pet Insurance
    ("METLIFE PET", 5, 23),
    ## 5	24	Pet Food
    ("chewy", 5, 24),
    ("petco", 5, 24),
    ## 5	25	Veterinary Care

    # ----------------- Shopping ---------------- 
    ## 6	26	Clothing & Accessories
    ("target", 6, 26),
    ("uniqlo", 6, 26),
    ("oldnavy.com", 6, 26),
    ("old navy", 6, 26),
    ("TIKTOK SHOP", 6, 26),
    ## 6	27	Beauty & Personal Care
    ("HELLO SUGAR", 6, 27),
    ("ZEN MASSAGE", 6, 27),
    ("ULTA", 6, 27),
    ("GARIMA S BROWS", 6, 27),
    ("NAIL SALON", 6, 27),
    ## 6	28	Home Goods
    ("AMAZON MARKEPLACE", 6, 28),
    ("IKEA", 6, 28),
    ## 6	29	Electronics
    ## 6	30	Books & Stationery
    ## 6	31	General Merchandise

    # --------------- Entertainment --------------- 
    ## 7	32	Streaming Subscriptions
    ("YouTube", 7, 32),
    ("patreon", 7, 32),
    ("HBO Max", 7, 32),
    ("PEACOCK", 7, 32),
    ## 7	33	Movies 
    ("AMC",7,33),
    ## 7	34	Activities & Events
    ("KNOTT'S BERRY FARM", 7, 34),
    ## 7	35	Hobbies & Gaming

    # ------------------ Travel ------------------ 
    ## 8	36	Flights
    ("VOLARIS", 8, 36),
    ("ALASKA AIRLINES", 8, 36),
    ## 8	37	Lodging
    ("AIRBNB", 8, 36),

    # ---------------- Education ----------------- 
    ## 9	38	Tuition & Courses
    ("ACT*Los Angeles Unifie", 9, 38),
    ("UDEMY", 9, 38),
    ## 9	39	Bookstore/Supplies

    # -------------- 10	Debt & Fees -------------- 
    ## 10	40	Credit Card Payment
    ("CAPITAL ONE MOBILE PYMT", 10, 40),
    ("MOBILE PAYMENT - THANK YOU", 10, 40),
    ## 10	41	Student Loan Payment
    ("Department of Education", 10, 41),
    ## 10	42	Interest Charges
    ("INTEREST CHARGE", 10, 42),
    ## 10	43	Bank/Service Fees
    ("Overdraft Fee", 10, 43),

    # ----------- 11 Savings & Investments --------- 
    ## 11	44	Roth IRA Contribution
    ("FID BKG SVC", 11, 44),
    ## 11	45	Savings
    ("GOLDMAN SACHS", 11, 45),

    # ---------- 12	Personal Transfers ---------- 
    ## 12	46	Zelle Sent
    ## 12	47	Zelle Received

    # ---------- 13	Uncategorized ---------- 
]

def auto_categorize(merchant):
    merchant_upper = merchant.upper()
    for pattern, category_id, subcategory_id in merchant_rules:
        if pattern in merchant_upper:
            return category_id, subcategory_id
    return None, None
