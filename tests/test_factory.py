from flask_tailwind import create_app


def test_config():
    """Test create_app without passing test config"""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_error_handling():
    """Test error handlers"""
    app = create_app()
    client = app.test_client()

    response = client.get('/bad')
    assert response.status_code == 404
