import requests


def make_request(url):
    base_url = url
    response = requests.get(base_url)
    return response


def test_title():
    url = "https://poetrydb.org/title/Ozymandias/lines.json"
    response = make_request(url)
    expected_response = [
        {
            "lines": [
                "I met a traveller from an antique land",
                "Who said: Two vast and trunkless legs of stone",
                "Stand in the desert...Near them, on the sand,",
                "Half sunk, a shattered visage lies, whose frown,",
                "And wrinkled lip, and sneer of cold command,",
                "Tell that its sculptor well those passions read",
                "Which yet survive, stamped on these lifeless things,",
                "The hand that mocked them, and the heart that fed:",
                "And on the pedestal these words appear:",
                "'My name is Ozymandias, king of kings:",
                "Look on my works, ye Mighty, and despair!'",
                "Nothing beside remains. Round the decay",
                "Of that colossal wreck, boundless and bare",
                "The lone and level sands stretch far away."
            ]
        }
    ]
    assert response.status_code == 200
    data = response.json()
    assert expected_response == data


def test_author():
    url = "https://poetrydb.org/author/Ernest Dowson:abs/author"
    response = make_request(url)
    expected_response = [{'author': 'Ernest Dowson'}]
    assert response.status_code == 200
    data = response.json()
    assert expected_response == data


def test_cat():
    url = "https://cat-fact.herokuapp.com/facts/random"
    response = make_request(url)
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == 'cat'
    assert data["text"] is not None
