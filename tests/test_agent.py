from content_team.agents import ContentTeam
import pytest


def test_content_creation():
    team = ContentTeam()
    result = team.create_post("Test Topic")
    assert isinstance(result, str)
    assert len(result) > 100
