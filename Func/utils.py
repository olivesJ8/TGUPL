import aiohttp
import asyncio
import os
import time
from urllib.parse import urlparse

async def get_file_info(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.head(url, allow_redirects=True) as response:
                if response.status != 200:
                    return {"error": f"URL not accessible, status: {response.status}"}

                # Check if URL is downloadable
                content_type = response.headers.get("Content-Type", "")
                if "text/html" in content_type:
                    return {"error": "URL is not a direct file link"}

                # Get file size
                file_size = response.headers.get("Content-Length")
                file_size = int(file_size) if file_size else None

                # Extract filename
                content_disposition = response.headers.get("Content-Disposition", "")
                if "filename=" in content_disposition:
                    filename = content_disposition.split("filename=")[-1].strip().strip('"')
                else:
                    filename = os.path.basename(urlparse(url).path)

                # If filename is missing, generate one
                if not filename:
                    filename = f"file_{int(time.time())}"

                return {
                    "url": url,
                    "filename": filename,
                    "file_size": file_size,
                    "is_downloadable": True
                }
        except Exception as e:
            return {"error": str(e)}

