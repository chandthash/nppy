# This script renames 12 video file that is provided to the following link.
# If you want this script to be run then download all the videos from the link.
# And also change the path to the directory where you have your all the downloaded file.
# We suggest you to store all the videos in one directory.
# Link to video: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
# This script is written in python v2.7.15 due to which the code may vary little bit than v3.x
# You can modified the code as per your will.
# Any improvement done in this script is welcomed and appreciated


import os


def rename_django_videos():
    video_path = r'C:\Users\6292s\Downloads\Video\Django'  # Change your location where video is!
    os.chdir(video_path)

    for videos_name in os.listdir(video_path):
        numbering = videos_name.split('-')[2].strip(' ').split(' ')[-1].zfill(2) + ' '

        '''videos_name gives you list of all videos in video_path:

                Python Django Tutorial- Full-Featured Web App Part 1 - Getting Started.MP4
                Python Django Tutorial- Full-Featured Web App Part 10 - Create, Update, and Delete Posts.MP4
                Python Django Tutorial- Full-Featured Web App Part 11 - Pagination.MP4
                Python Django Tutorial- Full-Featured Web App Part 12 - Email and Password Reset.MP4
                Python Django Tutorial- Full-Featured Web App Part 2 - Applications and Routes.MP4
                Python Django Tutorial- Full-Featured Web App Part 3 - Templates.MP4
                Python Django Tutorial- Full-Featured Web App Part 4 - Admin Page.MP4
                Python Django Tutorial- Full-Featured Web App Part 5 - Database and Migrations.MP4
                Python Django Tutorial- Full-Featured Web App Part 6 - User Registration.MP4
                Python Django Tutorial- Full-Featured Web App Part 7 - Login and Logout System.MP4
                Python Django Tutorial- Full-Featured Web App Part 8 - User Profile and Picture.MP4
                Python Django Tutorial- Full-Featured Web App Part 9 - Update User Profile.MP4

            ------------------------------------------------------------------------------------------------------------

            Now, videos_name.split('-') splits all the above list in '-'

                ['Python Django Tutorial', ' Full', 'Featured Web App Part 1 ', ' Getting Started.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 10 ', ' Create, Update, and Delete Posts.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 11 ', ' Pagination.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 12 ', ' Email and Password Reset.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 2 ', ' Applications and Routes.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 3 ', ' Templates.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 4 ', ' Admin Page.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 5 ', ' Database and Migrations.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 6 ', ' User Registration.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 7 ', ' Login and Logout System.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 8 ', ' User Profile and Picture.MP4']
                ['Python Django Tutorial', ' Full', 'Featured Web App Part 9 ', ' Update User Profile.MP4']

            ------------------------------------------------------------------------------------------------------------

            Then, videos_name.split('-')[2] slice the list and gets the third element i.e Featured Web App Part
                Featured Web App Part 1
                Featured Web App Part 10
                Featured Web App Part 11
                Featured Web App Part 12
                Featured Web App Part 2
                Featured Web App Part 3
                Featured Web App Part 4
                Featured Web App Part 5
                Featured Web App Part 6
                Featured Web App Part 7
                Featured Web App Part 8
                Featured Web App Part 9

            ------------------------------------------------------------------------------------------------------------

            videos_name.split('-')[2].strip(' ') strips spaces from both sides i.e left and right

            ------------------------------------------------------------------------------------------------------------

            videos_name.split('-')[2].strip(' ').split(' ') splits the Featured Web App Part list between the spaces
            and returns the list:
                ['Featured', 'Web', 'App', 'Part', '1']
                ['Featured', 'Web', 'App', 'Part', '10']
                ['Featured', 'Web', 'App', 'Part', '11']
                ['Featured', 'Web', 'App', 'Part', '12']
                ['Featured', 'Web', 'App', 'Part', '2']
                ['Featured', 'Web', 'App', 'Part', '3']
                ['Featured', 'Web', 'App', 'Part', '4']
                ['Featured', 'Web', 'App', 'Part', '5']
                ['Featured', 'Web', 'App', 'Part', '6']
                ['Featured', 'Web', 'App', 'Part', '7']
                ['Featured', 'Web', 'App', 'Part', '8']
                ['Featured', 'Web', 'App', 'Part', '9']

            ------------------------------------------------------------------------------------------------------------

            videos_name.split('-')[2].strip(' ').split(' ')[-1] returns the last element of the above list
                    1
                    10
                    11
                    12
                    2
                    3
                    4
                    5
                    6
                    7
                    8
                    9

            ------------------------------------------------------------------------------------------------------------

            videos_name.split('-')[2].strip(' ').split(' ')[-1].zfill(2) fills the above obtained number with extra 0 to
            make its lenght 2 and we get:
                    01
                    10
                    11
                    12
                    02
                    03
                    04
                    05
                    06
                    07
                    08
                    09

        and in each iteration you get the above value and store in numbering variable
        '''
        name = videos_name.split('-')
        '''Here, name stores the splitted list between '-' splitted by videos_name.split('-')

            ['Python Django Tutorial', ' Full', 'Featured Web App Part 1 ', ' Getting Started.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 10 ', ' Create, Update, and Delete Posts.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 11 ', ' Pagination.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 12 ', ' Email and Password Reset.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 2 ', ' Applications and Routes.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 3 ', ' Templates.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 4 ', ' Admin Page.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 5 ', ' Database and Migrations.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 6 ', ' User Registration.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 7 ', ' Login and Logout System.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 8 ', ' User Profile and Picture.MP4']
            ['Python Django Tutorial', ' Full', 'Featured Web App Part 9 ', ' Update User Profile.MP4']'''

        rename = numbering + name[-1].strip(' ')
        '''
            name[-1] slice the list to get the last element and
            name[-1].strip(' ') stripes spaces from the both sides of last element

        '''
        os.rename(videos_name, rename)   # Renaming the files

    print('Files are renamed')


if __name__ == '__main__':
    rename_django_videos()
