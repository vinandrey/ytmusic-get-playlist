from ytmusicapi import YTMusic
import json
import csv

ytmusic = YTMusic('browser.json')

while True:
    print('1: Export playlist to CSV')
    print('2: Show users playlists')
    print('3: Export liked songs')
    print('4: Show number of liked songs')
    print('9: Exit')
    user_input = input('Choose action: ')
    if user_input.upper() == '1':
        playlist_id = input('Please enter YT playlist ID: ')
        playlist = ytmusic.get_playlist(playlist_id, 1000)
        counter = 0
        for i in playlist['tracks']:
                if i['album'] is None:
                    i['album'] = {'name': '', 'id': ''}
                    counter = counter + 1
                    print(str(counter) + ': ' + 'Got Null string in Album :( ')
                if i['artists'] is None:
                    i['artists'] = {'name': '', 'id': ''}
                    print(str(counter) + ': ' + 'Got Null string in Artist :( ')

        file_name_csv = playlist['title'] + '.csv'
        file_name_json = playlist['title'] + '.json'
        # Open the CSV file in write mode
        with open(file_name_csv, 'w', newline='', encoding='utf-8') as csvfile:
            # Create a CSV writer
            csv_writer = csv.writer(csvfile)
            # Write header row
            # csv_writer.writerow(['Title', 'Artist', 'Album'])
            # Write data rows
            for i in playlist['tracks']:
                csv_writer.writerow([i['title'], i['artists'][0]['name'], i['album']['name']])
            print('Export csv. DONE! : ' + file_name_csv)

        # Open a file in write mode ('w')
        with open(file_name_json, "w") as file:
            json.dump(playlist, file)
        print(' ')
        print('Export json. DONE! : ' + file_name_json)
        print('----------------------------------------------------')
        print(' ')
    elif user_input.upper() == '2':
        playlists = ytmusic.get_library_playlists(50)
        print('----------------------------------------------------')
        print('Got playlists: ', len(playlists))
        counter = 0
        for j in playlists:
            counter = counter + 1
            print(str(counter) + ': Title: ' + j['title'])
            print('     ID: ' + j['playlistId'])
            print('     Description: ' + j['description'])            
            print(' ')
        print('----------------------------------------------------')
        print(' ')
    elif user_input.upper() == '3':
        likes = ytmusic.get_liked_songs(1000)
        counter = 0
        for i in likes['tracks']:
                if i['album'] is None:
                    i['album'] = {'name': '', 'id': ''}
                    counter = counter + 1
                    print(str(counter) + ': ' + 'Got Null string in Album :( ')
                if i['artists'] is None:
                    i['artists'] = {'name': '', 'id': ''}
                    print(str(counter) + ': ' + 'Got Null string in Artist :( ')

        file_name_csv = 'likes.csv'
        file_name_json = 'likes.json'
        # Open the CSV file in write mode
        with open(file_name_csv, 'w', newline='', encoding='utf-8') as csvfile:
            # Create a CSV writer
            csv_writer = csv.writer(csvfile)
            # Write header row
            # csv_writer.writerow(['Title', 'Artist', 'Album'])
            # Write data rows
            for i in likes['tracks']:
                csv_writer.writerow([i['title'], i['artists'][0]['name'], i['album']['name']])
            print('Export csv. DONE! : ' + file_name_json)
        # Open a file in write mode ('w')
        with open(file_name_json, "w") as file:
            json.dump(playlist, file)
        print(' ')
        print('Export json. DONE! : ' + file_name_json)
        print('----------------------------------------------------')
        print(' ')
    elif user_input.upper() == '4':
        likes = ytmusic.get_liked_songs(1000)
        print(' ')
        print('You love ' + str(likes['trackCount']) + ' songs. Total Duration ' + str(likes['duration_seconds']/3600) + ' hours.')
        print('----------------------------------------------------')
        print(' ')
    elif user_input.upper() == '9':
        break
    else:
        print('Incorrect action.')