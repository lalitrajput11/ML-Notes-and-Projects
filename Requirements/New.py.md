
  
Creating requirements.txt and main.py, then installing dependencies
requirements.txt
main.py
pip install -r requirements.txt
fastapi
uvicorn
youtube-transcript-api
google-generativeai
python-dotenv
requests


lalitrajput@lalitrajput-dy5:~/Text Summarizer and Questions-Answer$ ^C
lalitrajput@lalitrajput-dy5:~/Text Summarizer and Questions-Answer$ pip install -r requirements.txt

Defaulting to user installation because normal site-packages is not writeable
Collecting fastapi
  Downloading fastapi-0.127.0-py3-none-any.whl (112 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 112.1/112.1 KB 4.8 MB/s eta 0:00:00
Collecting uvicorn
  Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 68.5/68.5 KB 21.3 MB/s eta 0:00:00
Collecting youtube-transcript-api
  Downloading youtube_transcript_api-1.2.3-py3-none-any.whl (485 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 485.1/485.1 KB 25.2 MB/s eta 0:00:00
Collecting google-generativeai
  Downloading google_generativeai-0.8.6-py3-none-any.whl (155 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.1/155.1 KB 51.2 MB/s eta 0:00:00
Collecting python-dotenv
  Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
Requirement already satisfied: requests in /home/lalitrajput/.local/lib/python3.10/site-packages (from -r requirements.txt (line 6)) (2.32.3)
Requirement already satisfied: pydantic>=2.7.0 in /home/lalitrajput/.local/lib/python3.10/site-packages (from fastapi->-r requirements.txt (line 1)) (2.7.4)
Collecting starlette<0.51.0,>=0.40.0
  Using cached starlette-0.50.0-py3-none-any.whl (74 kB)
Collecting annotated-doc>=0.0.2
  Using cached annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Requirement already satisfied: typing-extensions>=4.8.0 in /home/lalitrajput/.local/lib/python3.10/site-packages (from fastapi->-r requirements.txt (line 1)) (4.12.2)
Requirement already satisfied: h11>=0.8 in /home/lalitrajput/.local/lib/python3.10/site-packages (from uvicorn->-r requirements.txt (line 2)) (0.14.0)
Requirement already satisfied: click>=7.0 in /usr/lib/python3/dist-packages (from uvicorn->-r requirements.txt (line 2)) (8.0.3)
Collecting defusedxml<0.8.0,>=0.7.1
  Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Collecting google-ai-generativelanguage==0.6.15
  Downloading google_ai_generativelanguage-0.6.15-py3-none-any.whl (1.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 26.1 MB/s eta 0:00:00
Requirement already satisfied: tqdm in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-generativeai->-r requirements.txt (line 4)) (4.66.1)
Requirement already satisfied: google-auth>=2.15.0 in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-generativeai->-r requirements.txt (line 4)) (2.31.0)
Requirement already satisfied: google-api-core in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-generativeai->-r requirements.txt (line 4)) (2.19.1)
Requirement already satisfied: google-api-python-client in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-generativeai->-r requirements.txt (line 4)) (2.135.0)
Requirement already satisfied: protobuf in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-generativeai->-r requirements.txt (line 4)) (4.25.5)
Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.3 in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 4)) (1.24.0)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/lib/python3/dist-packages (from requests->-r requirements.txt (line 6)) (1.26.5)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests->-r requirements.txt (line 6)) (2020.6.20)
Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3/dist-packages (from requests->-r requirements.txt (line 6)) (3.3)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/lalitrajput/.local/lib/python3.10/site-packages (from requests->-r requirements.txt (line 6)) (3.3.2)
Requirement already satisfied: rsa<5,>=3.1.4 in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-auth>=2.15.0->google-generativeai->-r requirements.txt (line 4)) (4.9)
Requirement already satisfied: cachetools<6.0,>=2.0.0 in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-auth>=2.15.0->google-generativeai->-r requirements.txt (line 4)) (5.3.3)
Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/lib/python3/dist-packages (from google-auth>=2.15.0->google-generativeai->-r requirements.txt (line 4)) (0.2.1)
Requirement already satisfied: pydantic-core==2.18.4 in 

/home/lalitrajput/.local/lib/python3.10/site-packages (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1)) (2.18.4)
Requirement already satisfied: annotated-types>=0.4.0 in /home/lalitrajput/.local/lib/python3.10/site-packages (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1)) (0.7.0)
Requirement already satisfied: anyio<5,>=3.6.2 in /home/lalitrajput/.local/lib/python3.10/site-packages (from starlette<0.51.0,>=0.40.0->fastapi->-r requirements.txt (line 1)) (4.4.0)
Requirement already satisfied: googleapis-common-protos<2.0.dev0,>=1.56.2 in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-api-core->google-generativeai->-r requirements.txt (line 4)) (1.63.2)
Requirement already satisfied: uritemplate<5,>=3.0.1 in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-api-python-client->google-generativeai->-r requirements.txt (line 4)) (4.1.1)
Requirement already satisfied: google-auth-httplib2<1.0.0,>=0.2.0 in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-api-python-client->google-generativeai->-r requirements.txt (line 4)) (0.2.0)
Requirement already satisfied: httplib2<1.dev0,>=0.19.0 in /usr/lib/python3/dist-packages (from google-api-python-client->google-generativeai->-r requirements.txt (line 4)) (0.20.2)
Requirement already satisfied: exceptiongroup>=1.0.2 in /home/lalitrajput/.local/lib/python3.10/site-packages (from anyio<5,>=3.6.2->starlette<0.51.0,>=0.40.0->fastapi->-r requirements.txt (line 1)) (1.2.1)
Requirement already satisfied: sniffio>=1.1 in /home/lalitrajput/.local/lib/python3.10/site-packages (from anyio<5,>=3.6.2->starlette<0.51.0,>=0.40.0->fastapi->-r requirements.txt (line 1)) (1.3.1)
Requirement already satisfied: grpcio<2.0dev,>=1.33.2 in /home/lalitrajput/.local/lib/python3.10/site-packages (from google-api-core->google-generativeai->-r requirements.txt (line 4)) (1.66.1)
Collecting grpcio-status<2.0.dev0,>=1.33.2
  Downloading grpcio_status-1.76.0-py3-none-any.whl (14 kB)
Requirement already satisfied: pyparsing!=3.0.0,!=3.0.1,!=3.0.2,!=3.0.3,<4,>=2.4.2 in /usr/lib/python3/dist-packages (from httplib2<1.dev0,>=0.19.0->google-api-python-client->google-generativeai->-r requirements.txt (line 4)) (2.4.7)
Requirement already satisfied: pyasn1>=0.1.3 in /usr/lib/python3/dist-packages (from rsa<5,>=3.1.4->google-auth>=2.15.0->google-generativeai->-r requirements.txt (line 4)) (0.4.8)
Collecting grpcio<2.0dev,>=1.33.2
  Downloading grpcio-1.76.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (6.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.6/6.6 MB 17.9 MB/s eta 0:00:00
Collecting grpcio-status<2.0.dev0,>=1.33.2
  Downloading grpcio_status-1.75.1-py3-none-any.whl (14 kB)
  Downloading grpcio_status-1.75.0-py3-none-any.whl (14 kB)
  Downloading grpcio_status-1.74.0-py3-none-any.whl (14 kB)
  Downloading grpcio_status-1.73.1-py3-none-any.whl (14 kB)
  Downloading grpcio_status-1.73.0-py3-none-any.whl (14 kB)
  Downloading grpcio_status-1.72.2-py3-none-any.whl (14 kB)
  Downloading grpcio_status-1.72.1-py3-none-any.whl (14 kB)
  Downloading grpcio_status-1.71.2-py3-none-any.whl (14 kB)
Collecting protobuf
  Downloading protobuf-5.29.5-cp38-abi3-manylinux2014_x86_64.whl (319 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 319.9/319.9 KB 51.7 MB/s eta 0:00:00
Installing collected packages: uvicorn, python-dotenv, protobuf, grpcio, defusedxml, annotated-doc, youtube-transcript-api, starlette, grpcio-status, fastapi, google-ai-generativelanguage, google-generativeai
  Attempting uninstall: protobuf
    Found existing installation: protobuf 4.25.5
    Uninstalling protobuf-4.25.5:
      Successfully uninstalled protobuf-4.25.5
  Attempting uninstall: grpcio
    Found existing installation: grpcio 1.66.1
    Uninstalling grpcio-1.66.1:
      Successfully uninstalled grpcio-1.66.1
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
tensorflow 2.17.0 requires protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3, but you have protobuf 5.29.5 which is incompatible.
Successfully installed annotated-doc-0.0.4 defusedxml-0.7.1 fastapi-0.127.0 google-ai-generativelanguage-0.6.15 google-generativeai-0.8.6 grpcio-1.76.0 grpcio-status-1.71.2 protobuf-5.29.5 python-dotenv-1.2.1 starlette-0.50.0 uvicorn-0.40.0 youtube-transcript-api-1.2.3

lalitrajput@lalitrajput-dy5:~/Text Summarizer and Questions-Answer$
