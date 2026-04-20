from src.database.config import supabase
import bcrypt

def hash_pass(password):
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()

def check_pass(password,hashed_password):
    return bcrypt.checkpw(password.encode(),hashed_password.encode())

def check_teacher_exists(username):
    response=supabase.table("teachers").select("username").eq("username",username).execute()
    return len(response.data)>0
    
def create_teacher(username,name,password):
    data={
        "username":username,
        "name":name,
        "password":hash_pass(password)
    }
    response=supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username,password):
    response=supabase.table("teachers").select("username","password").eq("username",username).execute()
    if response.data:
        teacher=response.data[0]
        if check_pass(password,teacher["password"]):
            return teacher
    return None

def check_pass(password,hashed_password):
    return bcrypt.checkpw(password.encode(),hashed_password.encode())

def get_all_students():
    response=supabase.table("students").select("*").execute()
    return response.data