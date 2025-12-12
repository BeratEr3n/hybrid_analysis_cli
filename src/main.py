from core.api import APIClient
from core.search import SearchService
from core.classifier import TargetClassifier
from core.submission import SubmissionService

client = APIClient()
classifier = TargetClassifier()

search = SearchService(client, classifier)

submission = SubmissionService(client)


target1 = "cb65edf4cd4cc7130b06f43ac547c72101b9d720b96137a3b49975e903ae2309"
target2 = "https://motchilltv.you/AsyncClient.exe"
target3 = "entertainio.us"
target4 = "104.21.24.204"
target5 = "20250689408.pdf"

#resp = search.search(target5)
# ---------------------------
url = "https://motchilltv.you/AsyncClient.exe"
file_path = r"C:\Users\bttm\Desktop\hybrit\dist\test.exe" 

environment_id = 140

#resp1 = submission.submit_url(url=url, environment_id=environment_id)

resp2 = submission.submit_file(file_path=file_path, environment_id= environment_id)

# --------------------------
print(resp2)