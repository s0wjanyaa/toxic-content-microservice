import requests

BASE_URL = "http://localhost:8000"

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    print("Health:", r.status_code, r.json())

def test_version():
    r = requests.get(f"{BASE_URL}/version")
    print("Version:", r.status_code, r.json())

def test_analyze_text():
    test_cases = [
    {
        "user_id": "stu_1000",
        "post_id": "post_2000",
        "text": "You are so dumb and your post is pathetic"
    },
    {
        "user_id": "stu_1001",
        "post_id": "post_2001",
        "text": "Thank you for your help, I appreciate your support."
    },
    {
        "post_id": "stu_1002",
        "user_id": "post_2002",
        "text": "Stop harassing everyone, you creep!"
    },
    {
        "user_id": "stu_1003",
        "post_id": "post_2003",
        "text": "Kya bakwaas hai yeh!"
    },
    {
        "user_id": "stu_1004",
        "post_id": "post_2004",
        "text": "You are such an idiot. Nobody likes you here."
    },
    {
        "post_id": "stu_1005",
        "user_id": "post_2005",
        "text": "Tu kitna bada chutiya hai, samajhta nahi kya?"
    },
    {
        "user_id": "stu_1006",
        "post_id": "post_2006",
        "text": "This is f***ing stupid."
    },
    {
        "post_id": "stu_1007",
        "user_id": "post_2007",
        "text": "Nobody cares about your stupid opinions."
    },
    {
        "user_id": "stu_1008",
        "post_id": "post_2008",
        "text": "Merci beaucoup pour votre aide."
    },
    {
        "user_id": "stu_1010",
        "post_id": "post_2010",
        "text": "Great work on the project, well done!"
    }
    ]
    for case in test_cases:
        r = requests.post(f"{BASE_URL}/analyze-text", json=case)
        print("Input:", case["text"])
        print("Output:", r.status_code, r.json())
        print("-" * 40)

if __name__ == "__main__":
    test_health()
    test_version()
    test_analyze_text()