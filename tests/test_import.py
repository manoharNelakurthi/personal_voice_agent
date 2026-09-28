from app.voice_agent import VoiceAgent
from app.memory import ConversationMemory


def test_voice_agent_import():
    assert VoiceAgent is not None
    assert ConversationMemory is not None


def test_memory():
    memory = ConversationMemory(":memory:")
    memory.save_conversation("hello", "hi there")
    convs = memory.get_all_conversations()
    assert len(convs) == 1
    assert convs[0]["user"] == "hello"
