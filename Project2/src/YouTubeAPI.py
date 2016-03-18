import os

class YouTubeAPI:

    def __init__(self, info):
        self.checkInputs(info)

        osCommand = "youtube-dl --extract-audio --audio-format mp3 -o " + info['directory'] + "/%(title)s.%(ext)s " + info['url']
        print("oscommand - " + osCommand)

        fileName = os.system("youtube-dl --get-filename -o %(title)s https://www.youtube.com/watch?v=xAWtuxhdUDE")
        print("fileName - " + fileName)
        #os.system(osCommand)
        #os.system("youtube-dl --extract-audio --audio-format mp3 -o C:\\Users\Matt\Downloads\Music\%(title)s.%(ext)s(uploader) https://www.youtube.com/watch?v=Hn1BapsppXM")

        downloadFileName = info['directory'] + "/" + str(fileName) + ".mp3"
        print("downloadFileName - " + downloadFileName)

        trackInfo = info['artist'] + " - " + info['album'] + " - " + info['title']
        newFileName =  info['directory'] + "/" + trackInfo + ".mp3"
        print("newFileName - " + newFileName)

        #os.rename(downloadFileName, newFileName)

    def checkInputs(self, info):
        for entry in info:
            if info[entry] is None:
                info[entry] = ''