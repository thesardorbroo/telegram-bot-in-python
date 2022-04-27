class Customers:
    def __init__(self,uid,user_id,name,phone_number,step,last_choice,seria,status,language='uz',description = None) -> None:
        self.uid = uid
        self.user_id = user_id
        self.name = name
        self.phone_number = phone_number
        self.step = step
        self.last_choice = last_choice
        self.seria = seria
        self.status = status
        self.language = language
        self.descrpition = description

    async def get_obj_data(self):
        return [self.uid,self.user_id,self.name,self.phone_number,self.step,self.last_choice,self.seria,self.status,self.language,self.descrpition]

    async def ret_data(self):
        user_data = {
            "uid": self.uid,
            "user_id":self.user_id,
            "name":self.name,
            "phone_number":self.phone_number,
            "step":self.step,
            "last_choice":self.last_choice,
            "seria":self.seria,
            "status":self.status,
            "language":self.language,
            "descpition":self.descrpition,
        }
        return user_data