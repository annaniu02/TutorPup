
import os
import random
from supabase import create_client, Client

os.environ["SUPABASE_URL"] = "https://jjjvrciysvivtfzqdxbj.supabase.co"
os.environ["SUPABASE_KEY"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpqanZyY2l5c3ZpdnRmenFkeGJqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTY5MjU0MDUsImV4cCI6MjAzMjUwMTQwNX0.B4XP_SAihW2RMLu-Iyys2418FtFYIwM37XAQ_ZgA5OI"

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)