# Toxic Content Detection Microservice
This repository hosts the Toxicity & Abuse Detection Microservice, an AI-powered solution developed to automatically identify harmful language in online user content. It provides a robust, offline and containerized API for efficient content moderation.

## Features

- **Multi-label classification:** Detects toxic, insult and harassment categories.
- **Offline operation:** No internet required after setup.
- **Configurable thresholds:** Easily adjust sensitivity via `config.json`.
- **REST API:** Built with FastAPI, easy to integrate.
- **Dockerized:** Simple deployment anywhere.
- **Language detection:** Flags non-English text as "abusive".

## 📁 Project Structure

```plaintext
TOXICITY_API/
│
├── app/
│   ├── main.py                         
│   └── classifier.py                    
│
├── models/
│   ├── tfidf_vectorizer.pkl            
│   └── toxic_classifier.pkl             
│
├── notebooks/
│   └── toxicity_microservice_lr.ipynb   
│
├── tests/
│   └── test_suite.py                    
│
├── .gitignore                           
├── config.json                          
├── Dockerfile                           
├── README.md                            
├── requirements.txt                     
```
## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/toxic-content-microservice.git
cd toxic-content-microservice
```


### 2. Build and Run with Docker

```bash
docker build -t toxic-content-api .
docker run -p 8000:8000 toxic-content-api
```

The API will be available at `http://localhost:8000`.


## API Endpoints

### `/analyze-text` (POST)

Analyze a text for toxicity.

**Request Example:**
```json
{
  "post_id": "123",
  "user_id": "user456",
  "text": "This is f***ing stupid."
}
```

**Response Example:**
```json
{
  "is_toxic": true,
  "reasons": ["toxic", "harrasment"]
}
```

### `/health` (GET)

Check if the service is running.

### `/version` (GET)

Get the current model and API version.


## Using Postman

1. **Open Postman** and create a new `POST` request to `http://localhost:8000/analyze-text`.
2. In the **Body** tab, select `raw` and `JSON`, then enter your test input:
    ```json
    {
      "post_id": "1",
      "user_id": "user001",
      "text": "You are such a loser, nobody likes you here."
    }
    ```
3. Click **Send** to see the API response.
4. You can also test the `/health` and `/version` endpoints with `GET` requests.



## Configuration

- **Thresholds and enabled categories** can be set in `config.json`.
- Example:
    ```json
    {
      "toxicity_threshold": 0.75,
      "flag_threshold": 0.5
    }
    ```


