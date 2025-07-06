from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_yt.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    '''
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - Executa a coisa (o SUT - System Under Test)
    - A: Assert - Granta que A é A
    '''

    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Ola Mundo !'}
