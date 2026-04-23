# Create a Python program that defines a dictionary to store information about your favorite book.
# Include the title, author, publication year,
# and genre as key-value pairs. Print out the dictionary.
# and do at least 5 dictionary methods on it.

fav_book= {
    "title": "Netaji a Biography for The Young ",
    "author": "Krishna Bose",
    "published_year":"1995",
    "genre": "History",
}
print("fav_book: ", fav_book)
print("Title: ", fav_book["title"])
fav_book.pop("title")
fav_book["Title"]= "Netaji a Biography for The Young ".strip().title()
fav_book.update({"published_year": "1 January 1995"})
fav_book["description"] = "A concise biography of Netaji Subhas Chandra Bose meant for the young. The book will help to inculcate in the rising generation the basic human qualities like partriotism, national unity, self-sacrifice, courage and a concern for the poor of which Netaji was the shining example"

print(fav_book)
print("=======loops==========")
for key, value in fav_book.items():
    print(key, value)
print("=================")
for item in fav_book:
    print(item, fav_book[item])


fav_book.popitem()
fav_book.clear()
