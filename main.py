from extractors.remote import extract_jobs_remote
from extractors.wwr import extract_jobs_wwr

remote = extract_jobs_remote("python")
wwr = extract_jobs_wwr("python")
result = remote + wwr

print(result)