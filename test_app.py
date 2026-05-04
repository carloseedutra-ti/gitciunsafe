from app import load_config

def test_load_config():
    data = load_config("name: demo")
    assert data["name"] == "demo"