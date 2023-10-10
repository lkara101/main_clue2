import pymongo
from flask import Flask, render_template, request

# https://www.w3schools.com/python/python_mongodb_find.asp
client = pymongo.MongoClient("mongodb+srv://lkara4:oaj2612ceW85TxlR@cluster1.ctkteaw.mongodb.net/?retryWrites=true&w=majority")
db = client["clueExport"]
collection = db["questions"]

app = Flask(__name__)

# Create a text index on the field you want to search (e.g., 'text_field')
# This should be done only once for your collection
#DONE -> collection.create_index([("question", pymongo.TEXT)])

# Perform the text search and sort by frequency
@app.route('/', methods=['GET', 'POST'])
def index():
    results = []

    if request.method == 'POST':
        search_string = request.form['search_string']
        sort_by = request.form['sort_by']  # Get the selected sorting option

        # Perform the text search and sort by the selected field
        if sort_by == 'relevance':
            sort_field = [("score", {"$meta": "textScore"})]
        elif sort_by == 'newest':
            sort_field = [("date", pymongo.DESCENDING)]  # Replace with your field name
        elif sort_by == 'oldest':
            sort_field = [("date", pymongo.ASCENDING)]  # Replace with your field name
        # Add more sorting options as needed

        # Define the text search query
        query = {"$text": {"$search": search_string}}

        # Perform the text search and sorting
        results = collection.find(query).sort(sort_field)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)



