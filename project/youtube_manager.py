import json
'''
Functionality to the entry points and triggers for handling CRUD in a File
'''


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def see_all_videos(videos):
    for index, vid in enumerate(videos, 1):
        print(f"{index}: {vid}")


def add_video(videos):
    name = input("enter video title: ")
    duration = input("enter duration: ")
    videos.append({'name': name, 'duration': duration})
    save_data_helper(videos)


def update_video(videos):
    see_all_videos(videos)
    index = int(input("Enter a video number to update: "))

    if len(videos) >= index >= 1:
        name = input("enter new name: ")
        duration = input("enter new durations: ")
        videos[index-1] = {'name': name, "duration": duration}
        save_data_helper(videos)


def delete_video(videos):
    see_all_videos(videos)
    index = int(input("Enter a video number to update: "))

    if len(videos) >= index >= 1:
        del videos[index-1]
        save_data_helper(videos)

'''
Entry point  
'''


def main():

    videos = load_data()
    input_list = [
        "1. See all videos",
        "2. Add a video",
        "3. Update a video",
        "4. Delete a video",
        "5. Exit program"
    ]
    while True:
        print(f"******* WellCome to Youtube Video Manager ********")
        for i in input_list:
            print(i)

        user_input = input(
            "Choose A Number To Perform Your Required Functionality: ")

        match user_input:
            case '1':
                see_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()
