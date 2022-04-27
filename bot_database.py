from mysql import connector

# import psycopg2
from psycopg2.errors import UndefinedColumn
from cus_class import Customers

class CafeDB:
    def __init__(self) -> None:
        self.connection = connector.connect(
            host='localhost',
            database='projects',
            username='root',
            password='root'
        )
        # self.connection = psycopg2.connect(
        #     host='ec2-23-20-224-166.compute-1.amazonaws.com',
        #     port='5432',
        #     user='phpsatylwrtmqu',
        #     database='d4kss672r1772k',
        #     password='f6cf494ebe1a941ef21cc52bbba0e17dbd416951f0521f0808f8ca3577ef90f3'
        # )
    
    async def read_from_db(self,query):
        c = self.connection.cursor()
        c.execute(query)
        return c.fetchall()

    async def write_to_db(self,query):
        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()    
        c.close()

    # This method works with table "customers" 
    async def update_column_values(self,user_id: int,col: str, val: any):
        """
        Update any value of column that avialabel in data base 
        and function askes user_id: int, column name: str, value: any
        """
        try:
            if type(val) == int:
                query = f"""
                UPDATE customers SET {col} = {val} WHERE user_id = {user_id}
                """
            else:
                query = f"""
                UPDATE customers SET {col} = '{val}' WHERE user_id = {user_id}
                """
            await self.write_to_db(query)
        except UndefinedColumn:
            return 404
            
    # This method works with table "customers" 
    async def update_all_data(self,user_id):
        query = f"""
        UPDATE customers SET step = {1},last_choice = 'None',seria = 'None',status = 'None'
        WHERE user_id = {user_id}
        """
        print("User is updated!")
        await self.write_to_db(query)
    
    # This method works with table "customers" 
    async def add_user_into_db(self,user_id,name):
        try:
            query = f"""
            INSERT INTO customers (user_id,name,step) VALUES ({user_id},'{name}',{1})
            """
            await self.write_to_db(query)
        except SyntaxError:
            print('SytaxError is existed!')
            query = f"INSERT INTO customers (user_id,step) VALUE ({user_id},{1})"
            await self.write_to_db(query)

        print("User is added successfully!")

    # This methods works with table "books"
    async def update_books(self,user_id,amount,food):
        uid = await self.get_user_data('id','customers','user_id',user_id)
        cost = await self.get_user_data('cost','national_foods','food_name',food)
        if await self.is_food_exist(food=food,uid=uid[0]):
            coun = await self.get_amount_food(food=food,uid=uid[0])
            query = f"""
            UPDATE books SET amount_food = {int(coun) + int(amount)} WHERE customer_food = '{food}' and id = {uid[0]}
            """
        else:
            if cost != 0:
                cost = cost[0]
            query = f"""
            INSERT INTO books (id,customer_food,amount_food,cost_food) VALUES
            ({uid[0]},'{food}',{amount},{cost})
            """
        await self.write_to_db(query)

    # This method works with table "books"
    async def get_amount_food(self,food,uid):
        query = f"""
        SELECT amount_food,customer_food FROM books WHERE id = {uid}
        """
        data = await self.read_from_db(query)
        for i in data:
            if food == i[1]:
                return i[0]
        return 0
    # This method works with table "books"
    async def is_food_exist(self,food,uid):
        query = f"""
        SELECT customer_food FROM books WHERE id = {uid}
        """
        data = await self.read_from_db(query)
        for i in data:
            if food in i:
                return True
                
        return False

    # This method works with table "customers"
    async def get_user_step(self,user_id):
        query = f"SELECT step FROM customers WHERE user_id = {user_id}"
        step = await self.read_from_db(query)
        step = list(step[0])
        return step

    # This method works with table "books"
    async def check_list(self,user_id):
        query = f"""
        SELECT customer_food, amount_food, cost_food FROM books WHERE id = {user_id}
        """
        data = await self.read_from_db(query)
        if len(data) != 0:  return data
        else:   return 0
    
    # This method works with table "books"
    async def delete_from_books(self,uid):
        query = f"DELETE FROM books WHERE id = {uid}"
        await self.write_to_db(query)
        print('Customer books were deleted successfuly!')
    
    async def delete_one_from_books(self,uid,food):
        if not await self.is_food_exist(food=food,uid=uid):
            return False
        query = f"""DELETE FROM books WHERE id = {uid} and customer_food = '{food}'
        """
        await self.write_to_db(query)
        return True

    async def update_sales_table(self,uid,name,amount,seria):
        query = f"""
        INSERT INTO sales (id,name,orders_summary,time,date,seria) 
        VALUES ({uid},'{name}',{amount},now(),now(),'{seria}')
        """
        await self.write_to_db(query)

    async def get_user_data(self,what: str, table_name: str, column_name: str, value: any):
        if type(value) == int:
            query = f"SELECT {what} FROM {table_name} WHERE {column_name} = {value}"
        else: 
            query = f"""SELECT {what} FROM {table_name} WHERE {column_name} = '{value}'
            """
        # print(query)
        data = await self.read_from_db(query)
        # print(data)
        try:
            data = list(data[0])
            return data
        except IndexError:
            return 0

    async def get_menu(self,category):
        query = f"""
        SELECT status,food_name,cost FROM national_foods WHERE abs_name='{category}'
        """
        data = await self.read_from_db(query)
        if len(data) != 0: return data
        else: return 0

    async def is_data_exist(self,what: str, where: str, column_name: str, value: any):
        if type(value) == int:
            query = f"SELECT {what} FROM {where} WHERE {column_name} = {value}"
        else:
            query = f"""
            SELECT {what} FROM {where} WHERE {column_name} = '{value}'
            """

        data = await self.read_from_db(query)
        if len(data) != 0: return True
        else: return False

    async def update_all_value_from_books(self,user_id):
        uid = await self.get_user_data('id','customers','user_id',user_id)
        uid = uid[0]
        await self.delete_from_books(uid=uid) 
    
    async def write_courier_to_table(self, courier: str, seria: str):
        query = f"""UPDATE sales SET courier = '{courier}' WHERE seria = '{seria}'
        """
        await self.write_to_db(query)
        print('Updating was successfuly!')
    
    async def update_books_sc(self, col: str, val: any, uid: int, food: str):
        try:
            query = f"""UPDATE books SET {col} = {val} WHERE id = {uid} and customer_food = "{food}"
            """
            print(query)
            await self.write_to_db(query)
        except TypeError:
            query = f"""UPDATE books SET {col} = {val} WHERE id = {uid} and customer_food = "{food}"
            """
            await self.write_to_db(query)
            
    async def m_to_create_btns(self,uid: int):
        """This method works to get all customer's foods"""
        query = f"SELECT customer_food FROM books WHERE id = {uid}"
        foods = await self.read_from_db(query)
        if len(foods) != 0:
            return foods
        else : return 0

    async def get_all_data(self,user_id: int):
        query = f"SELECT user_id,name,phone_number,language FROM customers WHERE user_id = {user_id}"
        data = await self.read_from_db(query)
        try:
            data = list(data[0])
        except IndexError:
            data = data
        return data

    async def get_data_from_db(self,user_id):
        query = f"""
            SELECT * FROM customers WHERE user_id = {user_id}
        """
        data = await self.read_from_db(query)
        try:
            data = data[0]
            return Customers(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9])
        except IndexError:
            print("Expected error!")

           