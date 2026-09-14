# Import the 3D Modeling module
from src.3d_modeling import ThreeDModeling

# Initialize the 3D Modeling module
three_d_modeling = ThreeDModeling()

# Add the 3D Modeling module to the allowed tools
ALLOWED_TOOLS = [
    # Existing tools
    "ask_user",
    "search_chats",
    "read_chat",
    "search_knowledge",
    "list",
    "read",
    "grep",
    "three_d_modeling"
]

# Add the 3D Modeling module to the tools dictionary
tools = {
    # Existing tools
    "ask_user": ask_user,
    "search_chats": search_chats,
    "read_chat": read_chat,
    "search_knowledge": search_knowledge,
    "list": list,
    "read": read,
    "grep": grep,
    "three_d_modeling": three_d_modeling
}
