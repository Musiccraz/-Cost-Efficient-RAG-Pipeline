import hashlib

def generate_chunk_id(chunk):

    content = (
        chunk.metadata.get("source","")
        + str(chunk.metadata.get("page",""))
        + chunk.page_content

    )

    return hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()