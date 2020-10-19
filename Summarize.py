import NLP
import re
from youtube_transcript_api import YouTubeTranscriptApi
def transcribe (youtube_url):
    api_key = 'AIzaSyCyxIlwMmP2PoqyWbnpTuLHn0pH0toKDjA'
    regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')

    match = regex.match(youtube_url)

    if not match:
        print('no match')
    video_id = match.group('id')
    data = YouTubeTranscriptApi.get_transcript(video_id)
    final_text = ''
    for line in data:
        final_text += line['text']

    NLP.summary(final_text)


transcribe('https://www.youtube.com/watch?v=RmTxvkhzFPo')

#
# url = 'https://gdata.youtube.com/feeds/api/videos/'+ID+'/captions'
# response = requests.request("GET", url)
# print(response)
