import json
from bson import ObjectId
from pymongo import MongoClient

# Connect to the MongoDB server
class Export_Database:
    def json_encoder(obj):
        """JSON encoder function to handle ObjectId serialization."""
        if isinstance(obj, ObjectId):
            return str(obj)
        raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

    def Export_database(DatabaseName,export_path):
        client = MongoClient('mongodb://localhost:27017')
        # Select the database
        db = client[DatabaseName]

        # Get the list of collection names in the database
        collection_names = db.list_collection_names()

        # Iterate over the collection names
        for collection_name in collection_names:
            # Select the collection
            collection = db[collection_name]

            # Query the collection to retrieve the documents
            documents = collection.find()

            # Define the output file path for this collection
            output_file = f"{export_path}/{collection_name}.json"

            # Define an empty list to store the documents
            data = []

            # Iterate over the documents and add them to the list
            for document in documents:
                data.append(document)

            # Write the data to the output file in JSON format
            with open(output_file, 'w') as file:
                json.dump(data, file, indent=4, default=Export_Database.json_encoder)
            print(f"Export completed for collection: {collection_name}")

        # Close the MongoDB connection
        client.close()