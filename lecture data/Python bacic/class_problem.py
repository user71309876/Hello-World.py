class House:
    def __init__(self, location, house_type,deal_type,price,completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year
    
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
            ,self.price, self.completion_year)
        
h1=House("강남","아파트","매매","10억",2010)
h1.show_detail()