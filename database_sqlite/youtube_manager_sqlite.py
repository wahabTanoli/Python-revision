import sqlite3
conn = sqlite3.connect("youtube_manager.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


'''
Functionality to the entry points and triggers for handling CRUD in a File
'''


def see_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, duration):
    # see_all_videos()
    cursor.execute(
        "INSERT INTO videos(name, time) VALUES(?, ?)", (name, duration))


def update_video(id, name, duration):
    cursor.execute(
        "UPDATE videos SET name=?, time=? WHERE id=?", (name, duration, id))


def delete_video(id):
    cursor.execute("DELETE FROM videos WHERW id=?", id)


def main():
    input_list = [
        "1. See all videos",
        "2. Add a video",
        "3. Update a video",
        "4. Delete a video",
        "5. Exit program"
    ]
    while True:
        print(f"******* WellCome to Youtube Video Manager ******** \n ")
        for i in input_list:
            print(i)

        user_input = input(
            "Choose A Number To Perform Your Required Functionality: ")

        match user_input:
            case '1':
                see_all_videos()
            case '2':
                name = input("enter video name: ")
                duration = input("enter video duration: ")
                add_video(name, duration)
            case '3':
                id = int(input("enter video number to edit: "))
                name = input("enter new video name: ")
                duration = input("enter new video duration: ")
                update_video(id, name, duration)
            case '4':
                id = int(input("enter video number to delete: "))
                delete_video(id)
            case _:
                print("invalid choice")

    conn.close()


if __name__ == "__main__":
    main()
