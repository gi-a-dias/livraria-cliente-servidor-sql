import os
from pymongo import MongoClient
from dotenv import load_dotenv
import dns.resolver

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
dns.resolver.default_resolver = resolver

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)
db = client["livraria"]
colecao_livros = db["livros"]