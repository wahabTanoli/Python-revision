from pymongo import MongoClient
from bson import ObjectId
client = MongoClient(
    "mongodb+srv://wahabtanoli24_db_user:mquzkjvwUJ3kMfDt@cluster0.p3kxway.mongodb.net/")
db = client["youtube_manager"]
videos_collection = db['videos']

client.admin.command("ping")  # fails loudly if auth/network is wrong
# print(videos_collection)

# result = videos_collection.insert_one({"name": "test video", "time": "10:00"})
# print("Inserted:", result.inserted_id)


def list_all_videos():
    for vid in videos_collection.find({}):
        print(
            f"id: {vid['_id']}, name: {vid['name']}, duration: {vid['time']}")


def add_new_video(data):
    videos_collection.insert_one(
        {"name": data["name"], "time": data["duration"]})
    print("new video added with name:", data['name'])


def update_video(id, data):

    result = videos_collection.update_one({"_id": ObjectId(id)},
                                          {"$set": {"name": data["name"], "time": data["duration"]}})
    if result.matched_count:

        print("***Record updated!*** \n")
    else:
        print("*** Video not found!\n")


def delete_video(id):
   result= videos_collection.delete_one({'_id': ObjectId(id)})
       


def main():
    print('''
          ****************------ python with mongo simple --------**************** \n''')
    while True:
        print("1.List all videos")
        print("2.Add a videos")
        print("3.Update videos")
        print("4.Delete a Video")
        print("5.Exit program \n")

        choice = input("\n Choose required number to manage videos: ")
        match choice:
            case "1":
                list_all_videos()
            case "2":
                name = input("enter video name: ")
                duration = input("enter video duration: ")
                data = {"name": name, "duration": duration}
                add_new_video(data)
            case "3":
                id = input("enter video number to update: ")
                name = input("enter new video name: ")
                duration = input("enter new video duration: ")
                data = {"name": name, "duration": duration}
                update_video(id, data)
            case "4":
                id = input("enter video number to delete: ")
                delete_video(id)
            case _:
                print("invalid key")


if __name__ == "__main__":
    main()
